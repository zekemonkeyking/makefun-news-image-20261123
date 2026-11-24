#!/usr/bin/env python3
"""THE WORLD IN ONE DAY -- 8-bit edition.

Sum up 23 November 2026 world news in one image.

The entry image is held in this repository as entry.png.b64, the
base64 encoding of a 1024x1024 8-bit pixel newspaper front page:
36 stories led by COP31, the Merkury sinking and Hormuz, on pale-mint
paper with CryptoPunk-style pixel art.

This program only decodes that image and writes it to the output
location, using the Python standard library alone (no third-party
packages, no network). Running it twice writes byte-identical files.
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png.b64"


def main() -> None:
    out_dir = Path("/output")
    if out_dir.is_dir():
        dest = out_dir / "entry.png"
    else:
        dest = HERE / "entry.png.out"
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = base64.b64decode(SOURCE.read_bytes())  # newlines in the file are ignored
    dest.write_bytes(data)
    os.chmod(dest, 0o644)


if __name__ == "__main__":
    main()
