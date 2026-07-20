from src.sources import pull_source

def test_pull_example():
    data = pull_source("https://example.com")
    assert data["url"] == "https://example.com"
    assert len(data["text"]) > 0 or len(data["title"]) > 0
