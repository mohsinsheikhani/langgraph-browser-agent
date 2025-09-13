import requests
from langchain.agents import Tool
from src.config import Config


def push_notification(text: str):
    """Send a push notification to the user via Pushover."""
    requests.post(
        Config.PUSHOVER_URL,
        data={
            "token": Config.PUSHOVER_TOKEN,
            "user": Config.PUSHOVER_USER,
            "message": text,
        },
    )


def get_push_tool():
    """Create and return the push notification tool."""
    return Tool(
        name="send_push_notification",
        func=push_notification,
        description="useful for when you want to send a push notification",
    )
