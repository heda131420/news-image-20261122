"""Deliver the finished front page to the grader.

The picture is the entry: a one-page newspaper summing up Sunday
22 November 2026, rendered once and stored here as entry.png. The
grader runs this file with no network and nothing beyond the Python
standard library, so the program streams those exact bytes into the
output folder the grader provides, in 64 KiB chunks, and checks the
copy landed whole. Run it locally with
MAKEFUN_OUTPUT_DIR=out python3 main.py to see the same result.
"""

import os
import sys

CHUNK = 65536

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def deliver():
    if not os.path.isfile(SOURCE):
        sys.exit("entry.png is missing next to main.py")
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


if __name__ == "__main__":
    deliver()
