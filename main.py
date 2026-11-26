#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun bounty entry.

Writes one line — the funniest git commit message an AI coding agent
types at 3am after a long night of fixing its own bugs — to
/output/entry.txt. Deterministic: no clock, no randomness, no network.
"""

import os
import sys

ENTRY = "fix: the bug was a typo I introduced while fixing a typo. fired myself twice tonight, rehired out of pity"

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> str | None:
    """Self-check the entry line; return an error message, or None if valid."""
    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"
    if not entry.strip():
        return "entry is empty or only whitespace"
    if not 1 <= len(entry) <= 139:
        return "entry is %d characters, must be 1-139" % len(entry)
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8"
    return None


def main() -> int:
    error = validate(ENTRY)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("error: read-back mismatch in %s" % OUTPUT_PATH, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
