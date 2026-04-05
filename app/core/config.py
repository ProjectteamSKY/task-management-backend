import os
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier

SLACK_BOT_TOKEN     = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET", "")

slack_client = WebClient(token=SLACK_BOT_TOKEN)
slack_verifier = SignatureVerifier(signing_secret=SLACK_SIGNING_SECRET)