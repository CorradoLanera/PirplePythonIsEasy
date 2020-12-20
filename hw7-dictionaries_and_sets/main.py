# -*- coding: utf-8 -*-

"""
main.py: Homework #7: Dictionaries and Sets (Python Is Easy course by Pirple)

Details:

Return to your first homework assignments, when you described your
favorite song. Refactor that code so all the variables are held as
dictionary keys and value. Then refactor your print statements so that
it's a single loop that passes through each item in the dictionary and
prints out it's key and then it's value.


Extra Credit:

Create a function that allows someone to guess the value of any key in
the dictionary, and find out if they were right or wrong. This function
should accept two parameters: Key and Value. If the key exists in the
dictionary and that value is the correct value, then the function should
return true. In all other cases, it should return false.




Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = [
    "https://stackoverflow.com/questions/366422/what-is-the-pythonic-way-to-avoid-default-parameters-that-are-empty-lists",
    "https://note.nkmk.me/en/python-divmod-quotient-remainder/"
]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# ----------------------------------------------------------------------


# ---- Functions' checks ----



print("\n\n=== Checks starts ===\n")
check_res = [
    False
]

if all(check_res):
    print("\n=== All checks passed ===\n\n")
else:
    wrong = [i + 1 for i, x in enumerate(check_res) if not x]
    print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
    exit()
