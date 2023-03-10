# pylint: disable=missing-module-docstring
import sys

from pylint import lint

THRESHOLD = 8

run = lint.Run(["main.py"], do_exit=False)

score = run.linter.stats["global_note"]

if score < THRESHOLD:
    print("Linter failed: Score < 8")

    sys.exit(1)

sys.exit(0)
