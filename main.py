# SPDX-License-Identifier: MIT
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip to /output/entry.txt (or to the path
given as the first argument, for local verification runs).

The tip is a fixed string: deterministic, offline, stdlib-only.
"""

import sys
from pathlib import Path

TIP = (
    "Tip: when the agent says 'fixed it' for the third time, read the diff "
    "yourself \u2014 you're the only one here who can be embarrassed."
)


def main(argv: list[str]) -> int:
    out_path = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one line, no trailing newline: the gate counts characters,
    # so the file holds the tip and nothing else.
    out_path.write_text(TIP, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
