from __future__ import annotations
from pathlib import Path
import typer
from rich import print
from .sources import pull_source
from .weaver import weave

app = typer.Typer()

@app.command("weave")
def weave_urls(urls: list[str], out: Path | None = typer.Option(None)):
    print(f"[cyan]Pulling[/cyan] {len(urls)} sources…")
    sources = [pull_source(u) for u in urls]
    brief = weave(sources)
    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(brief)
        print(f"[green]Wrote[/green] {out}")
    else:
        print(brief)

if __name__ == "__main__":
    app()
