# Directions — multi-url-brief-weaver

## What this is
Multi-source corpus weaving agent. Give it several URLs; it scrapes each, then weaves a single coherent brief with citations.

## Setup
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. `cp .env.example .env` and set `OPENAI_API_KEY`

## Run
```bash
python -m src.main weave https://example.com https://www.wikipedia.org
python -m src.main weave https://a.com https://b.com --out output/brief.md
```

## API keys
| Variable | Required | Source |
|----------|----------|--------|
| OPENAI_API_KEY | Yes | https://platform.openai.com/api-keys |
