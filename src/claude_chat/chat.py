"""The Chatbot class: it remembers the conversation."""
import logging

logger = logging.getLogger(__name__)

MAX_MESSAGES = 20  # keep only the newest messages so the history stays small


class Chatbot:
    def __init__(self, client, model: str, system_prompt: str = "You are a friendly, helpful assistant."):
        self.client = client
        self.model = model
        self.system_prompt = system_prompt
        self.history: list[dict] = []  # the API forgets everything, so WE remember

    def send(self, user_text: str) -> str:
        """Send one message and return the reply."""
        self.history.append({"role": "user", "content": user_text})
        self.history = self.history[-MAX_MESSAGES:]
        logger.info("Sending %d messages", len(self.history))

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                system=self.system_prompt,
                messages=self.history,
            )
        except Exception:
            self.history.pop()  # remove the message that failed
            raise

        reply = response.content[0].text
        self.history.append({"role": "assistant", "content": reply})
        return reply
