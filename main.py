"""Decode the bundled base64 image and write it to /output/entry.png.

The repository ships the finished 1024x1024 PNG as a single line of
base64 in entry.png.b64. This program only decodes it, so two runs
produce byte-identical output.
"""

import base64
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png.b64"
    if not src.exists():
        src = Path("entry.png.b64")
    data = base64.b64decode(src.read_text().strip())
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("decoded bytes are not a PNG image")
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)


if __name__ == "__main__":
    main()
