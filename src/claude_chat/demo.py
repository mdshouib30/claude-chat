"""A pretend client, so the chatbot runs without an API key or credits."""

from types import SimpleNamespace


class DemoClient:
    def __init__(self):
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        messages = kwargs["messages"]
        last = messages[-1]["content"]
        text = f"(demo) You said: {last}. I remember {len(messages)} messages so far."
        return SimpleNamespace(content=[SimpleNamespace(text=text)])
