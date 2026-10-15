"""Reads settings from the .env file."""
import os

from dotenv import load_dotenv

load_dotenv()  # reads the .env file and fills environment variables

DEFAULT_MODEL = "claude-sonnet-5-5"


def get_api_key() -> str:
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is missing. Copy .env.example to .env and add your key."
        )
    return key


def get_model() -> str:
    return os.getenv("MODEL", DEFAULT_MODEL)
