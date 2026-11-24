"""Decode the bundled base64 PNG and write it to /output/entry.png.

The repository ships the image as a single line of base64 text in
entry.png.b64. This decoder uses only the Python standard library, so it
runs in the grader without any extra packages installed.
"""

import base64
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png.b64"
    encoded = source.read_text(encoding="ascii").strip()
    data = base64.b64decode(encoded, validate=True)
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("decoded data is not a PNG image")
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        raise ValueError("decoded PNG is truncated: missing IEND chunk")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
