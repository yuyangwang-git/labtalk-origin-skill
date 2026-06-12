"""Search the LabTalk command index and reference files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
INDEX = REFERENCES / "command-index.json"


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def search_index(query: str, limit: int) -> list[str]:
    if not INDEX.exists():
        return []
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    q = normalize(query)
    hits = []
    for item in data:
        haystack = normalize(" ".join(str(item.get(key, "")) for key in ["name", "description", "source"]))
        if q in haystack:
            hits.append(
                f"{item.get('name')}: {item.get('description')} "
                f"(source: {item.get('source')}, page: {item.get('page')})"
            )
        if len(hits) >= limit:
            break
    return hits


def search_references(query: str, limit: int) -> list[str]:
    q = query.lower()
    hits = []
    for path in sorted(REFERENCES.glob("*.md")):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if q in line.lower():
                hits.append(f"{path.name}:{line_no}: {line.strip()}")
                if len(hits) >= limit:
                    return hits
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    print("Index hits:")
    for hit in search_index(args.query, args.limit):
        print(f"- {hit}")

    print("\nReference hits:")
    for hit in search_references(args.query, args.limit):
        print(f"- {hit}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
