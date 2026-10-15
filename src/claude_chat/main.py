"""Start the chatbot: python -m claude_chat.main  (add --demo to run without a key)"""

import logging
import sys

import anthropic

from claude_chat.chat import Chatbot
from claude_chat.config import get_api_key, get_model
from claude_chat.demo import DemoClient


def main() -> None:
    logging.basicConfig(level=logging.WARNING)
    if "--demo" in sys.argv:
        client = DemoClient()
        print("Demo mode: no real AI, no cost.")
    else:
        client = anthropic.Anthropic(api_key=get_api_key())
    bot = Chatbot(client, get_model())

    print("Chatbot ready. Type 'quit' to stop.")
    while True:
        text = input("You: ").strip()
        if text.lower() in {"quit", "exit"}:
            print("Bye!")
            break
        if not text:
            continue
        try:
            print("Bot:", bot.send(text))
        except Exception as error:
            print("Oops, something went wrong:", error)


if __name__ == "__main__":
    main()
