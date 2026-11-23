"""Deliver the finished front page to the grader.

The picture is the entry: a one-page newspaper summing up Sunday
22 November 2026, rendered once and stored here as entry.png. The
grader runs this file with no network and nothing beyond the Python
standard library, so the program streams those exact bytes into the
output folder the grader provides, in 64 KiB chunks, and checks the
copy landed whole. Run it locally with
MAKEFUN_OUTPUT_DIR=out python3 main.py to see the same result.
"""

import hashlib
import os
import struct
import sys

CHUNK = 65536

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            block = f.read(CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def check_jpeg_header(path):
    """entry.png is JPEG data (JFIF) despite the .png name: verify the
    SOI marker and the SOF dimensions, so a truncated or wrong-format
    copy fails loudly instead of passing a size-only check."""
    with open(path, "rb") as f:
        data = f.read(65536)
    if data[:3] != b"\xff\xd8\xff":
        sys.exit("entry.png copy failed JPEG SOI marker check")
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            sys.exit("entry.png copy has malformed JPEG markers")
        marker = data[i + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/SOF1/SOF2: dimensions live here
            height, width = struct.unpack(">HH", data[i + 5:i + 9])
            if (width, height) != (1024, 1024):
                sys.exit(f"entry.png copy is {width}x{height}, expected 1024x1024")
            return
        i += 2 + seg_len
    sys.exit("entry.png copy is missing a JPEG SOF segment")


def deliver():
    if not os.path.isfile(SOURCE):
        sys.exit("entry.png is missing next to main.py")
    source_sha256 = sha256_of(SOURCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(SOURCE, "rb") as src, open(dest, "wb") as out:
        while True:
            block = src.read(CHUNK)
            if not block:
                break
            out.write(block)
    os.chmod(dest, 0o644)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        sys.exit("entry.png did not copy completely")
    if sha256_of(dest) != source_sha256:
        sys.exit("entry.png copy failed SHA-256 content check")
    check_jpeg_header(dest)


if __name__ == "__main__":
    deliver()
