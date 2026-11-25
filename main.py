#!/usr/bin/env python3
"""Write one office joke to the output file.

The joke is a constant, so every run writes exactly the same line.
"""

import os
import sys

JOKE = "My out-of-office reply now attends meetings for me, and it got promoted."

MAX_CHARS = 200


def output_dir():
    """Where entry.txt goes; OUTPUT_DIR overrides the /output default."""
    return os.environ.get("OUTPUT_DIR", "/output")


def validate(text):
    """Return the first problem found, or None when the text is valid."""
    if not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    if "\n" in text:
        return "entry must be a single line"
    return None


def main():
    problem = validate(JOKE)
    if problem is not None:
        print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
