# Research AI Agent

A lightweight and maintainable AI agent backend for research assistance, paper discovery, summarisation, task automation, and future WeChat/Web integration.

## Features

Current version:

- FastAPI backend
- Simple AI agent interface
- Environment-based configuration
- OpenAI-compatible LLM service wrapper
- Health check endpoint
- Clean project structure for future extension

Planned extensions:

- Paper recommendation workflow
- GitHub repository search
- Literature monitoring
- Vector database memory
- WeChat / Enterprise WeChat / Web UI integration
- Scheduled task execution

## Project Structure

```text
research-ai-agent/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── agent/
│   ├── services/
│   └── utils/
├── scripts/
├── tests/
├── requirements.txt
├── pyproject.toml
├── .env.example
└── README.md
```

