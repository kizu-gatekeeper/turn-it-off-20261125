#!/usr/bin/env python3
"""Write the one-line tech support line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Have You Tried Turning It Off" bounty. The program
writes exactly one line of text and nothing else.

How the line targets the brief: the judge compares hopeless tech support
lines pairwise, so the line has to sound like a real agent on a real call
-- and the funniest version of that agent is one who knows exactly one
trick and is already out of tricks. The customer gets the classic opener,
then the agent confesses, mid-sentence, that there is no step two and he
is improvising from here on. The joke lands because every caller has met
this man: confident on step one, bluffing on step two, and hoping you do
not notice the difference.
"""

import os
from pathlib import Path

LINE = "Have you tried turning it off and on again? I ask because step two is pretending I know what step two is."


def write_entry(out_dir: Path) -> Path:
    """Write the tech support line to entry.txt inside out_dir and return
    its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line of under 200 chars.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
