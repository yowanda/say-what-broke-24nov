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
    # Runtime validation: the error line must be exactly one line,
    # non-empty, and at most 200 characters.
    assert LINE, "error line must not be empty"
    assert "\n" not in LINE and "\r" not in LINE, "error line must be a single line"
    assert len(LINE) <= 200, "error line must be at most 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic byte write: exact bytes, no timestamps or randomness.
    payload = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(payload)


if __name__ == "__main__":
    main()
