#!/usr/bin/env python3
"""One-line office joke for make.fun.

Competition: u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.
Writes a single office-life joke to /output/entry.txt.
Deterministic: the same line is written on every run.
Gate: /output/entry.txt must hold 1-200 UTF-8 characters, not only
whitespace; this joke is one line well inside that limit.
Standard library only.
"""

import os
from pathlib import Path

JOKE = "Our printer has never once jammed on a document nobody needed — I'm convinced it reads the file names first."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
