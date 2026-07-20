from __future__ import annotations
import httpx
from bs4 import BeautifulSoup

def pull_source(url: str) -> dict:
    with httpx.Client(follow_redirects=True, timeout=30.0, headers={"User-Agent": "multi-url-brief-weaver/1.0"}) as c:
        r = c.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        for t in soup(["script", "style", "nav", "footer"]):
            t.decompose()
        title = (soup.title.string or "").strip() if soup.title else url
        text = " ".join(p.get_text(" ", strip=True) for p in soup.find_all("p")[:30])
        return {"url": url, "title": title, "text": text[:8000]}
