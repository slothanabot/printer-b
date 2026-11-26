#!/usr/bin/env python3
"""make.fun entry: The Printer Finally Answers (printer-b).

One original one-line comeback, spoken by the office printer itself.
The printer is a smug gatekeeper that only jams when the document
actually matters. It opens with its own service record -- 214,000
pages printed without a single complaint -- the flat, literal logic
of a machine that has counted every sheet it has ever fed. Then the
turn: the one document you need in five minutes is the one it has
decided, on purpose, to eat. The humour is the betrayal being
deliberate: the printer is not broken, it is choosing.

The script validates the line against the competition gate
(RULES.txt: /output/entry.txt must hold UTF-8 text of 1 to 240
characters, not only whitespace, a single line) and writes it out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 240


def build_line():
    """Return the printer's comeback.

    The punch is the printer's reliability record making the jam a
    choice, not an accident: 214,000 flawless pages, and the one
    that matters gets eaten on purpose.
    """
    return (
        "I have printed 214,000 pages without a single complaint. "
        "The contract you need in five minutes? "
        "I have decided to eat that one."
    )


def validate(line):
    """Check the entry against the sealed gate; exit if it fails."""
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    validate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    assert saved == line, "round-trip mismatch"
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT, len(saved), LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    run()
