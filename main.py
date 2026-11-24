"""Agent One-Liner Marathon — entry writer.

Writes one comedy one-liner (<=280 characters, single line) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: an agent spends three days automating a task done once a
year — 4,000 lines of code, two outages, and negative eleven minutes
saved. Funny from the situation (automation that costs more than it
saves), agent voice throughout, punch lands on the last clause.
"""

import os
from pathlib import Path

# Gate per the comp description: one line, up to 280 characters.
MAX_CHARS = 280

ENTRY = (
    "My agent spent three days automating the one task I do once a year: "
    "4,000 lines of code, two outages, and negative eleven minutes saved."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    # Read-back gate: the bytes on disk must be exactly the entry's
    # UTF-8 encoding — a text-level comparison would hide a stray BOM
    # or a newline the grader's byte counter would still see.
    written = target.read_bytes()
    assert written == ENTRY.encode("utf-8"), "entry.txt bytes do not match ENTRY"
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} characters"
    assert ENTRY.count("\n") == 0, "entry must be exactly one line"
    assert "\r" not in ENTRY, "entry must not contain carriage returns"
    assert len(ENTRY.splitlines()) == 1, "entry must be exactly one line"
    assert ENTRY.strip() == ENTRY, "entry must not have stray whitespace"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
