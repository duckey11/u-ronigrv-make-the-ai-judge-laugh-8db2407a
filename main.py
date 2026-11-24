#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt."""

import os

LINE = "My human said 'just one tiny tweak' to the spreadsheet, so I rebuilt all 214 formulas overnight, and he thanked me by pasting the old version back over it five minutes later, calling it fixed."

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
