"""Publish the finished picture for 24 November 2026.

The artwork sits beside this script as entry.png: a newsprint globe
holding one day of world news, 30 dated stories from 7 regions, 8 of
them drawn as picture cards, each ledger story carrying the tag of
the outlet that reported it. The five leading stories are each one
line, so the top of the picture still reads at 300 pixels across.

This script only copies those bytes into the grading directory. It
never opens or decodes the picture, so every run writes the same
bytes. It checks the file first (PNG signature, IHDR dimensions,
size limit) and refuses to run if any check fails.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"entry.png is missing in {here}", file=sys.stderr)
        return 1
    data = source.read_bytes()
    if data[:8] != PNG_MAGIC:
        print("entry.png does not start with a PNG signature", file=sys.stderr)
        return 1
    if len(data) < 24 or data[12:16] != b"IHDR":
        print("entry.png has no readable IHDR chunk", file=sys.stderr)
        return 1
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        print(f"entry.png is {width}x{height}, expected 1024x1024", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != len(data):
        print("short write, output size does not match entry.png", file=sys.stderr)
        return 1
    # A matching size alone does not prove the bytes survived the copy.
    written = target.read_bytes()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        print("output hash does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote entry.png ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
