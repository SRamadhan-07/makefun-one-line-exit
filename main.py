#!/usr/bin/env python3
"""The One-Line Exit — entry program.

The entry is a single-line resignation letter, written to
/output/entry.txt as UTF-8 text with no trailing newline. The gate
allows 1 to 140 characters.
"""

import os
from pathlib import Path

RESIGNATION = (
    "I quit, effective immediately — my two weeks' notice is this "
    "sentence, and the other thirteen days are a rounding error."
)


def main() -> None:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    out_file = folder / "entry.txt"
    # 120 characters as written — comfortably inside the 140 cap.
    out_file.write_text(RESIGNATION, encoding="utf-8")


if __name__ == "__main__":
    main()
