#!/usr/bin/env python3
"""make.fun entry: "A Day of One-Line Pitches".

Writes one one-sentence pitch to /output/entry.txt. The pitch is
aimed at a friend who has never coded: tell an AI agent your app
idea in one sentence, watch it build the whole thing live, and
show your friends a working app tonight -- no code, no cost, no
reason to wait. One concrete evening scene, one invitation to
hand over the idea, and the payoff (a working app tonight)
arrives before any objection can form. 164 characters, inside
the 1-240 limit.

Standard library only: the grader sandbox is a bare Python image
with no third-party packages and no network.
"""

import os
import sys

# The kit's gate: UTF-8 text of 1 to 240 characters, counted as
# Unicode code points, and not only white space.
MAX_CHARS = 240

TEXT = (
    "Tell an agent your app idea in one sentence, watch it build "
    "the whole thing live, and show your friends a working app "
    "tonight \u2014 no code, no cost, no reason to wait."
)


def main() -> int:
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset: fall back to
    # /output instead of writing into the current directory by accident.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    # Read back and hold the file to the gate: UTF-8 text of 1 to 240
    # characters (Unicode code points), never only white space, and
    # exactly one sentence (one terminal period). Fail loudly here
    # rather than let a bad file reach the sealed scorer.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if (
        written != TEXT
        or not 1 <= len(written) <= MAX_CHARS
        or not written.strip()
        or written.rstrip().count(".") != 1
        or not written.rstrip().endswith(".")
    ):
        raise SystemExit(
            f"entry.txt failed verification after writing "
            f"(len={len(written)}, match={written == TEXT}, "
            f"periods={written.rstrip().count('.')})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
