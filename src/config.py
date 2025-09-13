import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
    PUSHOVER_USER = os.getenv("PUSHOVER_USER")
    PUSHOVER_URL = "https://api.pushover.net/1/messages.json"

    # Model configuration
    MODEL_NAME = "gemini-2.5-flash"

    # Browser configuration
    HEADLESS_MODE = False
