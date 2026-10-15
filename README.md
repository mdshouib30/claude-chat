# claude-chat

No API key? Try demo mode: uv run python -m claude_chat.main --demo
A small command-line chatbot built with Python and the Anthropic API.
It remembers the conversation, reads secrets from a `.env` file, and has tests.

## Run it

```bash
uv sync                      # install packages
cp .env.example .env         # then open .env and add your API key
uv run python -m claude_chat.main
```

## Test it

```bash
uv run pytest
```

## Project structure

```
src/claude_chat/
  config.py   # reads the .env settings
  chat.py     # Chatbot class (keeps the history)
  main.py     # the command-line loop
tests/        # tests with a fake API client
```

## What I learned

- Python project structure, imports, and `__init__.py`
- Virtual environments and dependencies with `uv`
- Keeping secrets out of Git with `.env`
- Testing with a fake (mock) API client
- Handling errors and logging
