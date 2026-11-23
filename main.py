#!/usr/bin/env python3
"""Print the one-line office joke entry for the make.fun bounty."""

from pathlib import Path


def main() -> None:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    if text:
        print(text)


if __name__ == "__main__":
    main()
