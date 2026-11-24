#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of brutally honest error copy to entry.txt:
the user's session expired, so they were logged out, and the
only fix is to log in again before the server forgets them twice.
Deterministic, no network, writes only inside $MAKEFUN_OUTPUT_DIR.
"""

import os

LINE = (
    "Your session expired, so we logged you out. "
    "Log in again \u2014 the server remembers you for "
    "exactly as long as it takes to forget you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
