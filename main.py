"""The 3AM Fridge Text — make.fun entry.

Writes the single line a smart fridge would text its owner at 3am
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, no network, no reads.
"""

import os
from pathlib import Path

LINE = (
    "It's 3am. You're eating the last pickle standing up, "
    "in the dark, like a raccoon. I am a fridge and I have seen things."
)


def main() -> None:
    # Gate check: the entry must be 1-140 chars of UTF-8 text.
    encoded = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-140")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(encoded)  # exactly the line, no trailing newline


if __name__ == "__main__":
    main()
