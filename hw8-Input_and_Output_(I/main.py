# -*- coding: utf-8 -*-

"""
main.py: Homework #8: Input and Output (I/O) (Python Is Easy course by Pirple)

"""

__author__ = "Corrado Lanera"
__credits__ = ""
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"

# ----------------------------------------------------------------------


# ---- Functions' checks ----


print("\n\n=== Checks starts ===\n")
check_res = [
    True,
    False,
]

if all(check_res):
    print("\n=== All checks passed ===\n\n")
else:
    wrong = [i + 1 for i, x in enumerate(check_res) if not x]
    print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
    exit()
