from types import SimpleNamespace

import pytest

from claude_chat.chat import Chatbot


class FakeClient:
    """Pretends to be the API, so tests are free and fast."""

    def __init__(self, fail=False):
        self.fail = fail
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        if self.fail:
            raise ConnectionError("no internet")
        reply = SimpleNamespace(text="Hello from fake!")
        return SimpleNamespace(content=[reply])


def test_bot_remembers_messages():
    bot = Chatbot(FakeClient(), model="fake")
    assert bot.send("Hi") == "Hello from fake!"
    assert len(bot.history) == 2  # your message + the reply


def test_failed_message_is_removed():
    bot = Chatbot(FakeClient(fail=True), model="fake")
    with pytest.raises(ConnectionError):
        bot.send("Hi")
    assert bot.history == []
