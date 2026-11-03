"""Check that relative Markdown links resolve within the repository."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]+\")?\)")

def validate_links():
    problems = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for href in LINK.findall(text):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = href.split("#", 1)[0]
            if not clean:
                continue
            target = (path.parent / clean).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.exists():
                problems.append(f"{path.relative_to(ROOT)} -> {href}")
    return problems

if __name__ == "__main__":
    problems = validate_links()
    assert not problems, "Missing relative links:\n" + "\n".join(problems)
    print("PASS: all relative markdown links resolve")
