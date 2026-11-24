#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one single-line sick-day excuse to /output/entry.txt.
The line must be exactly one line, one sentence, 1-200 characters,
with no leading or trailing whitespace.
"""

import os

# One concrete mishap (superglue), believable enough to half-buy,
# with the twist landing on the last words.
LINE = "Sorry, can't come in — I superglued my hand to the steering wheel and the car is now legally part of me."


def validate(line: str) -> None:
    """Raise ValueError unless the line meets the competition gate."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or whitespace only")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) < 1 or len(line) > 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence ending with a period")


def main() -> None:
    validate(LINE)
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("round-trip verification failed")
    print(f"OK: {len(LINE)} chars -> {out_path}")
    print(LINE)


if __name__ == "__main__":
    main()
