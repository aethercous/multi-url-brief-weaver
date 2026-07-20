from __future__ import annotations
from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_MODEL

def weave(sources: list[dict]) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY missing — see DIRECTIONS.md")
    client = OpenAI(api_key=OPENAI_API_KEY)
    blocks = []
    for i, s in enumerate(sources, 1):
        blocks.append(f"[S{i}] {s['title']} ({s['url']})\n{s['text']}")
    prompt = (
        "Weave these sources into one coherent markdown brief with a short overview, "
        "key themes, and a Sources section citing [S#].\n\n" + "\n\n".join(blocks)
    )
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are Aetherial CorpusWeaver, a research synthesis agent."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content or ""
