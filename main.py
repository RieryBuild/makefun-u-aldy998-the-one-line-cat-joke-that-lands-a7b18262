"""Write the one-line cat joke entry to entry.txt.

The joke's setup is cosy and innocent — the cat sleeps on my pillow,
right where a loving cat belongs — then it turns: she is only there to
harvest my hair ties — and the punchline upgrades petty theft to a
criminal enterprise run from my own bed.
"""

import os

JOKE = "My cat sleeps on my pillow just to harvest my hair ties; I'm convinced she's running a black-market elastic empire."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
