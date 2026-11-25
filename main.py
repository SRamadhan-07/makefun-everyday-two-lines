"""Everyday Things, Two Lines - make.fun entry.

Writes the approved two-line analogy to /output/entry.txt.
Line 1 is a vivid analogy explaining a queue to a 10-year-old.
Line 2 is one honest sentence about what the analogy maps
and what it leaves out.
"""

import os

LINE_ONE = (
    "A queue is a train where every carriage is a person "
    "and the engine is the one till that actually works."
)
LINE_TWO = (
    "It maps the waiting and the creeping forward, but leaves out "
    "that trains never sigh at the person paying in coins."
)

def build_entry_text() -> str:
    """Return the entry as exactly two lines joined by one newline."""
    return LINE_ONE + "\n" + LINE_TWO


ENTRY_TEXT = build_entry_text()


def main() -> None:
    output_path = "/output/entry.txt"
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
