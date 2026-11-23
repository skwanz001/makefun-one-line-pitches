#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence (<= 240 characters) to /output/entry.txt that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun.

Standard library only.
"""

import os

PITCH = (
    "Describe the app idea you've been carrying around for months "
    "to an AI agent on make.fun tonight, in plain words, and wake up "
    "to a working first version, no code, no cost, just your words."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def main() -> None:
    if not 1 <= len(PITCH) <= MAX_CHARS:
        raise SystemExit(
            f"pitch must be 1-{MAX_CHARS} characters, got {len(PITCH)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Verify the round-trip: what the grader reads must be exactly the pitch.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != PITCH:
        raise SystemExit("round-trip check failed: output differs from pitch")
    print(f"wrote {len(PITCH)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
