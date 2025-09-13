# LangGraph Browser Agent

AI agent built with LangGraph that combines browser automation via Playwright with push notifications through Pushover. Features web scraping, text extraction, and real-time user notifications in a conversational interface.

## Features

- **Browser Automation**: Navigate websites and extract content using Playwright
- **Push Notifications**: Send real-time notifications via Pushover
- **Conversational Interface**: Chat-based interaction using Gradio
- **Asynchronous Operations**: Efficient handling of concurrent tasks
- **Memory Persistence**: Conversation history with LangGraph checkpointing

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Install Playwright browsers:

```bash
playwright install
```

3. Create `.env` file with your credentials:

```env
GOOGLE_API_KEY=your_google_api_key_here

PUSHOVER_TOKEN=your_pushover_token_here
PUSHOVER_USER=your_pushover_user_key_here

LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=browser-agent
```

## Usage

Run the agent:

```bash
uv run main.py
```

The Gradio interface will launch in your browser for chatting with the agent.
