import json
from datetime import datetime

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, Response

from app.core.config import slack_client, slack_verifier

router = APIRouter(prefix="/slack", tags=["Slack"])


# ── Helpers ──────────────────────────────────────────────────────────────────

def verify_slack_request(body: bytes, timestamp: str, signature: str) -> None:
    """Raise 400 if the Slack signature is invalid."""
    if not slack_verifier.is_valid(body, timestamp, signature):
        raise HTTPException(status_code=400, detail="Invalid Slack signature")


TASK_MODAL_VIEW = {
    "type": "modal",
    "callback_id": "task_modal",
    "title":  {"type": "plain_text", "text": "Create Task"},
    "submit": {"type": "plain_text", "text": "Create"},
    "close":  {"type": "plain_text", "text": "Cancel"},
    "blocks": [
        {
            "type": "input",
            "block_id": "title_block",
            "label": {"type": "plain_text", "text": "Title"},
            "element": {
                "type": "plain_text_input",
                "action_id": "title",
                "placeholder": {"type": "plain_text", "text": "Task title"},
            },
        },
        {
            "type": "input",
            "block_id": "description_block",
            "label": {"type": "plain_text", "text": "Description"},
            "element": {
                "type": "plain_text_input",
                "action_id": "description",
                "multiline": True,
                "placeholder": {"type": "plain_text", "text": "What is this task about?"},
            },
        },
        {
            "type": "input",
            "block_id": "status_block",
            "label": {"type": "plain_text", "text": "Status"},
            "element": {
                "type": "static_select",
                "action_id": "status",
                "placeholder": {"type": "plain_text", "text": "Select status"},
                "options": [
                    {"text": {"type": "plain_text", "text": "Todo"},        "value": "todo"},
                    {"text": {"type": "plain_text", "text": "In Progress"}, "value": "in_progress"},
                    {"text": {"type": "plain_text", "text": "Done"},        "value": "done"},
                ],
            },
        },
        {
            "type": "input",
            "block_id": "priority_block",
            "label": {"type": "plain_text", "text": "Priority"},
            "element": {
                "type": "static_select",
                "action_id": "priority",
                "placeholder": {"type": "plain_text", "text": "Select priority"},
                "options": [
                    {"text": {"type": "plain_text", "text": "Low"},    "value": "low"},
                    {"text": {"type": "plain_text", "text": "Medium"}, "value": "medium"},
                    {"text": {"type": "plain_text", "text": "High"},   "value": "high"},
                ],
            },
        },
        {
            "type": "input",
            "block_id": "hours_block",
            "label": {"type": "plain_text", "text": "Estimated Hours"},
            "element": {
                "type": "plain_text_input",
                "action_id": "estimated_hours",
                "placeholder": {"type": "plain_text", "text": "e.g. 4"},
            },
        },
        {
            "type": "input",
            "block_id": "assigned_block",
            "label": {"type": "plain_text", "text": "Assigned To (User ID)"},
            "optional": True,
            "element": {
                "type": "plain_text_input",
                "action_id": "assigned_to",
                "placeholder": {"type": "plain_text", "text": "e.g. 2"},
            },
        },
        {
            "type": "input",
            "block_id": "project_block",
            "label": {"type": "plain_text", "text": "Project Name"},
            "element": {
                "type": "plain_text_input",
                "action_id": "project_name",
                "placeholder": {"type": "plain_text", "text": "e.g. Backend Revamp"},
            },
        },
        {
            "type": "input",
            "block_id": "start_date_block",
            "label": {"type": "plain_text", "text": "Start Date"},
            "optional": True,
            "element": {
                "type": "datepicker",
                "action_id": "start_date",
                "placeholder": {"type": "plain_text", "text": "Select start date"},
            },
        },
        {
            "type": "input",
            "block_id": "end_date_block",
            "label": {"type": "plain_text", "text": "End Date"},
            "optional": True,
            "element": {
                "type": "datepicker",
                "action_id": "end_date",
                "placeholder": {"type": "plain_text", "text": "Select end date"},
            },
        },
    ],
}


# ── Routes ────────────────────────────────────────────────────────────────────

@router.post("/events")
async def slack_events(request: Request):
    body = await request.body()
    verify_slack_request(body, request.headers.get("x-slack-request-timestamp"), request.headers.get("x-slack-signature"))

    data = await request.json()

    if data.get("type") == "url_verification":
        return JSONResponse(content={"challenge": data["challenge"]})

    return JSONResponse(content={"status": "ok"})


@router.post("/commands")
async def slack_commands(request: Request):
    body = await request.body()
    verify_slack_request(body, request.headers.get("x-slack-request-timestamp"), request.headers.get("x-slack-signature"))

    form    = await request.form()
    command = form.get("command")

    if command == "/task":
        slack_client.views_open(trigger_id=form.get("trigger_id"), view=TASK_MODAL_VIEW)
        return Response(status_code=200)

    if command == "/help":
        return JSONResponse(content={
            "response_type": "ephemeral",
            "text": "Available commands:\n/task - Create a new task\n/help - Show this help",
        })

    return JSONResponse(content={"response_type": "ephemeral", "text": "Unknown command! Type /help for help."})


@router.post("/interactions")
async def slack_interactions(request: Request):
    body = await request.body()
    verify_slack_request(body, request.headers.get("x-slack-request-timestamp"), request.headers.get("x-slack-signature"))

    form    = await request.form()
    payload = json.loads(form.get("payload"))

    if payload.get("type") != "view_submission" or payload["view"]["callback_id"] != "task_modal":
        return Response(status_code=200)

    values  = payload["view"]["state"]["values"]
    user_id = payload["user"]["id"]

    def parse_date(raw: str | None):
        return datetime.strptime(raw, "%Y-%m-%d").date() if raw else None

    task_data = {
        "title":           values["title_block"]["title"]["value"],
        "description":     values["description_block"]["description"]["value"],
        "status":          values["status_block"]["status"]["selected_option"]["value"],
        "priority":        values["priority_block"]["priority"]["selected_option"]["value"],
        "estimated_hours": int(values["hours_block"]["estimated_hours"]["value"]),
        "assigned_to":     int(v) if (v := values["assigned_block"]["assigned_to"]["value"]) else None,
        "project_name":    values["project_block"]["project_name"]["value"],
        "start_date":      parse_date(values["start_date_block"]["start_date"].get("selected_date")),
        "end_date":        parse_date(values["end_date_block"]["end_date"].get("selected_date")),
    }

    try:
        from app.services import task_service  # ← fix this path to match your project
        await task_service.create_task(task_data)
        slack_client.chat_postMessage(
            channel=user_id,
            text=(
                f"✅ Task created!\n"
                f"*Title:* {task_data['title']}\n"
                f"*Status:* {task_data['status']}\n"
                f"*Priority:* {task_data['priority']}\n"
                f"*Estimated Hours:* {task_data['estimated_hours']}\n"
                f"*Project:* {task_data['project_name']}\n"
                f"*Start Date:* {task_data['start_date'] or 'N/A'}\n"
                f"*End Date:* {task_data['end_date'] or 'N/A'}"
            ),
        )
    except Exception as e:
        print(f"Task creation failed: {e}")
        slack_client.chat_postMessage(channel=user_id, text=f" Failed to create task: {str(e)}")

    return Response(status_code=200)