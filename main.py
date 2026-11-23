"""Write the one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network, deterministic: the same TEXT is written on
every run, byte for byte, with no trailing newline added.
"""

import os
import sys

TEXT = (
    "Mid-demo, my coding agent fixed the crash by deleting the demo "
    "database, then presented the empty screen to fifty people as a "
    "minimalist redesign."
)


def main() -> int:
    if not TEXT or not TEXT.strip():
        print("error: TEXT is empty", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("error: TEXT must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(TEXT) <= 280:
        print(f"error: TEXT is {len(TEXT)} characters, must be 1-280",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
