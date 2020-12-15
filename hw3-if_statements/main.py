# -*- coding: utf-8 -*-

"""
main.py: Homework #3: If statements (Python Is Easy course by Pirple)

Details:

Create a function that accepts 3 parameters and checks for equality
between any two of them.

Your function should return True if 2 or more of the parameters are
equal, and false is none of them are equal to any of the others.


Extra Credit:

Modify your function so that strings can be compared to integers if they
are equivalent. For example, if the following values are passed to your
function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you
convert strings to Integers.



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = [
    "https://www.geeksforgeeks.org/python-check-if-a-variable-is-string/",
    "https://www.w3schools.com/python/ref_func_all.asp#:~:text=The%20all()%20function%20returns,()%20function%20also%20returns%20True.",
    "https://stackoverflow.com/questions/21448225/getting-indices-of-true-values-in-a-boolean-list"
]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# ----------------------------------------------------------------------

def str_to_float(x):
    ## general numbers are not only integers, so I decided to convert
    ## them to floats instead.

    # https://www.geeksforgeeks.org/python-check-if-a-variable-is-string/
    if isinstance(x, str):
        return float(x)
    else:
        return x


def are_at_least_two_equals(x, y, z):
    x = str_to_float(x)
    y = str_to_float(y)
    z = str_to_float(z)

    if x == y or x == z or y == z:
        print("Yes, at least two of the inputs provided are equals")
        return True
    else:
        print("No, all the inputs provided are different")
        return False


def check(test_name):
    # https://www.w3schools.com/python/ref_func_all.asp#:~:text=The%20all()%20function%20returns,()%20function%20also%20returns%20True.
    result = globals()[test_name]
    if all(result):
        print("===", test_name.title(), "tests passed ===\n\n")
    else:
        print("=== !!! Something wrong in", test_name, "tests !!! ===")
        # https://stackoverflow.com/questions/21448225/getting-indices-of-true-values-in-a-boolean-list
        wrong = [i + 1 for i, x in enumerate(result) if not x]
        print("Test(s) not passed:", str(wrong))
        print("\n\n")


print("\n=== Base tests ===")
base = [
    not are_at_least_two_equals(1, 2, 3),  # all distinct
    are_at_least_two_equals(1, 1, 3),  # first two
    are_at_least_two_equals(1, 2, 2),  # last two
    are_at_least_two_equals(3, 2, 3),  # first and last
    are_at_least_two_equals(1, 1, 1),  # all equals
    are_at_least_two_equals(3.1, 2, 3.1)  # floats
]
check("base")

print("\n=== Strings tests ===")
strings = [
    are_at_least_two_equals("1", 1, 3),  # string first
    are_at_least_two_equals(1, "2", 2),  # string second
    are_at_least_two_equals(3, 2, "3"),  # string last
    are_at_least_two_equals("3", 2, "3"),  # two strings
    not are_at_least_two_equals("1", "2", "3")  # distinct strings
]
check("strings")

print("\n=== Strange tests ===")
strange = [
    are_at_least_two_equals("1.1", 1.1, 3),  # float in text
    are_at_least_two_equals("1.0", 1, 3),  # text float and integers
    are_at_least_two_equals("-1", -1, 3),  # negative text
    not are_at_least_two_equals("1.1", 1, 3)  # wrong rounding
]
check("strange")
