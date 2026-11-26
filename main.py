#!/usr/bin/env python3
"""One Star for Monday — writes a one-star review of Monday,
written as though Monday were a restaurant, to /output/entry.txt."""

import os

ENTRY = (
    "One star. Sat down for a fresh start and Monday served cold coffee, "
    "burnt toast, and a bill for a weekend I never got."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, with no trailing newline: the gate
    # counts every character, and the entry is a single line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
