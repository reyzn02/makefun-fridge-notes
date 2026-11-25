#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge: one note a smart fridge leaves
for its owner.

The program writes a single line, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). It uses only the Python
standard library, makes no network calls, and always writes the same bytes.
"""

import os

LINE = (
    "I kept your yogurt at exactly 3\xb0C for nine days. You opened me "
    "at 2 a.m., stared into the light, and ate the leftovers standing "
    "up. I have told the ice maker everything."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
