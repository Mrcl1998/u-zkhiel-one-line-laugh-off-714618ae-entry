#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt. Pure standard library,
deterministic, no network, no randomness.
"""

import os

LINE = "The vending machine took my dollar, gave me nothing, and somehow I apologized to it."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
