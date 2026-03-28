from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, Response
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import init_db
from app.routers import worker_router, task_router, schedule_router,task_assignment_router,project_router,capability_router,worker_availability_router,worker_notes_router,worker_resources_router
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
import os
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Slack setup ──
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "xoxb-10746634548881-10734060213682-Mezy3RLFuY6sFEVevxmY2bni")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET", "4a4a7121c60126753696598dcb978408")
client = WebClient(token=SLACK_BOT_TOKEN)
verifier = SignatureVerifier(signing_secret=SLACK_SIGNING_SECRET)

@app.on_event("startup")
async def startup():
    await init_db()

# ── Existing routers ──
app.include_router(worker_router.router)
app.include_router(task_router.router)
app.include_router(schedule_router.router)
app.include_router(project_router.router)
app.include_router(task_assignment_router.router)
app.include_router(capability_router.router)
app.include_router(worker_availability_router.router)
app.include_router(worker_notes_router.router)
app.include_router(worker_resources_router.router)

# ──────────────────────────────────────────
# Slack Routes
# ──────────────────────────────────────────

@app.post("/slack/events")
async def slack_events(request: Request):
    body = await request.body()
    signature = request.headers.get("x-slack-signature")
    timestamp = request.headers.get("x-slack-request-timestamp")

    if not verifier.is_valid(body, timestamp, signature):
        raise HTTPException(status_code=400, detail="Invalid Slack signature")

    data = await request.json()

    if data.get("type") == "url_verification":
        return JSONResponse(content={"challenge": data["challenge"]})

    return JSONResponse(content={"status": "ok"})


@app.post("/slack/commands")
async def slack_commands(request: Request):
    body = await request.body()
    signature = request.headers.get("x-slack-signature")
    timestamp = request.headers.get("x-slack-request-timestamp")

    if not verifier.is_valid(body, timestamp, signature):
        raise HTTPException(status_code=400, detail="Invalid Slack signature")

    form = await request.form()
    command = form.get("command")
    trigger_id = form.get("trigger_id")

    if command == "/task":
        client.views_open(
            trigger_id=trigger_id,
            view={
                "type": "modal",
                "callback_id": "task_modal",
                "title": {"type": "plain_text", "text": "Create Task"},
                "submit": {"type": "plain_text", "text": "Create"},
                "close": {"type": "plain_text", "text": "Cancel"},
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "title_block",
                        "label": {"type": "plain_text", "text": "Title"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "title",
                            "placeholder": {"type": "plain_text", "text": "Task title"}
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "description_block",
                        "label": {"type": "plain_text", "text": "Description"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "description",
                            "multiline": True,
                            "placeholder": {"type": "plain_text", "text": "What is this task about?"}
                        }
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
                            ]
                        }
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
                            ]
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "hours_block",
                        "label": {"type": "plain_text", "text": "Estimated Hours"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "estimated_hours",
                            "placeholder": {"type": "plain_text", "text": "e.g. 4"}
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "assigned_block",
                        "label": {"type": "plain_text", "text": "Assigned To (User ID)"},
                        "optional": True,
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "assigned_to",
                            "placeholder": {"type": "plain_text", "text": "e.g. 2"}
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "project_block",
                        "label": {"type": "plain_text", "text": "Project Name"},
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "project_name",
                            "placeholder": {"type": "plain_text", "text": "e.g. Backend Revamp"}
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "start_date_block",
                        "label": {"type": "plain_text", "text": "Start Date"},
                        "optional": True,
                        "element": {
                            "type": "datepicker",
                            "action_id": "start_date",
                            "placeholder": {"type": "plain_text", "text": "Select start date"}
                        }
                    },
                    {
                        "type": "input",
                        "block_id": "end_date_block",
                        "label": {"type": "plain_text", "text": "End Date"},
                        "optional": True,
                        "element": {
                            "type": "datepicker",
                            "action_id": "end_date",
                            "placeholder": {"type": "plain_text", "text": "Select end date"}
                        }
                    },
                ]
            }
        )
        return Response(status_code=200) 

    if command == "/help":
        return JSONResponse(content={
            "response_type": "ephemeral",
            "text": "Available commands:\n/task - Create a new task\n/help - Show this help"
        })

    return JSONResponse(content={
        "response_type": "ephemeral",
        "text": "Unknown command! Type /help for help."
    })


@app.post("/slack/interactions")
async def slack_interactions(request: Request):
    body = await request.body()
    signature = request.headers.get("x-slack-signature")
    timestamp = request.headers.get("x-slack-request-timestamp")

    if not verifier.is_valid(body, timestamp, signature):
        raise HTTPException(status_code=400, detail="Invalid Slack signature")

    form = await request.form()
    payload = json.loads(form.get("payload"))

    if payload.get("type") != "view_submission":
        return Response(status_code=200)

    if payload["view"]["callback_id"] != "task_modal":
        return Response(status_code=200)

    values = payload["view"]["state"]["values"]

    title           = values["title_block"]["title"]["value"]
    description     = values["description_block"]["description"]["value"]
    status          = values["status_block"]["status"]["selected_option"]["value"]
    priority        = values["priority_block"]["priority"]["selected_option"]["value"]
    estimated_hours = int(values["hours_block"]["estimated_hours"]["value"])
    assigned_to_raw = values["assigned_block"]["assigned_to"]["value"]
    assigned_to     = int(assigned_to_raw) if assigned_to_raw else None
    project_name    = values["project_block"]["project_name"]["value"]

    # ✅ fixed: convert string to proper date object for asyncpg
    start_date_raw  = values["start_date_block"]["start_date"].get("selected_date")
    end_date_raw    = values["end_date_block"]["end_date"].get("selected_date")
    start_date      = datetime.strptime(start_date_raw, "%Y-%m-%d").date() if start_date_raw else None
    end_date        = datetime.strptime(end_date_raw,   "%Y-%m-%d").date() if end_date_raw   else None

    user_id         = payload["user"]["id"]

    data = {
        "title": title,
        "description": description,
        "status": status,
        "priority": priority,
        "estimated_hours": estimated_hours,
        "assigned_to": assigned_to,
        "project_name": project_name,
        "start_date": start_date,
        "end_date": end_date,
    }

    try:
        await task_service.create_task(data)
        client.chat_postMessage(
            channel=user_id,
            text=(
                f"✅ Task created!\n"
                f"*Title:* {title}\n"
                f"*Status:* {status}\n"
                f"*Priority:* {priority}\n"
                f"*Estimated Hours:* {estimated_hours}\n"
                f"*Project:* {project_name}\n"
                f"*Start Date:* {start_date or 'N/A'}\n"
                f"*End Date:* {end_date or 'N/A'}"
            )
        )
    except Exception as e:
        print(f"Task creation failed: {e}")
        client.chat_postMessage(
            channel=user_id,
            text=f"❌ Failed to create task: {str(e)}"
        )

    return Response(status_code=200)