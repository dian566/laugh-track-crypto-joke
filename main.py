#!/usr/bin/env python3
"""One-line crypto trading joke for make.fun."""

# The joke is the turn: a trader buys the dip, and the dip buys a
# shovel and digs deeper, leaving the trader living in the hole.

import os

JOKE = "I bought the dip. Then the dip bought a shovel, dug deeper, and now I live in the hole rent-free with my portfolio."


# The gate allows at most 200 characters; this joke is 115 bytes.
EXPECTED_BYTES = 115


def file_joke() -> None:
    """Write the joke to /output/entry.txt, nothing else."""
    if len(JOKE) > 200 or not JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be a single non-empty line of at most 200 characters")
    if len(JOKE.encode("utf-8")) != EXPECTED_BYTES:
        raise ValueError("joke must be exactly 115 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    # Verify byte-exact: what was written is the joke, nothing added.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != JOKE.encode("utf-8"):
        raise ValueError("entry.txt is not byte-exact")


if __name__ == "__main__":  # run it
    file_joke()
