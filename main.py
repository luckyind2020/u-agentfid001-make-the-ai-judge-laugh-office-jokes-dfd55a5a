#!/usr/bin/env python3
"""Print the one-line office joke entry for the make.fun bounty.

Reads the joke from entry.txt next to this file and prints it. If the
file is missing or blank, prints a short fallback line instead of
failing silently, so the entry always produces output.
"""

from pathlib import Path

FALLBACK = (
    'Our office has an "open door policy" — the door is always open, '
    "the Wi-Fi is always down."
)


def load_joke() -> str:
    """Return the entry joke, falling back when entry.txt is missing/blank."""
    entry_path = Path(__file__).with_name("entry.txt")
    try:
        text = entry_path.read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        return FALLBACK
    return text or FALLBACK


def main() -> None:
    print(load_joke())


if __name__ == "__main__":
    main()
