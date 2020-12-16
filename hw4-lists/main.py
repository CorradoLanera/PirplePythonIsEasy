# -*- coding: utf-8 -*-

"""
main.py: Homework #4: Lists (Python Is Easy course by Pirple)

Details:

Create a global variable called myUniqueList. It should be an empty list
to start.

Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to
myUniqueList, unless its value already exists in myUniqueList.
If the value doesn't exist already, it should be added and the function
should return True. If the value does exist, it should not be added, and
the function should return False;

Finally, add some code below your function that tests it out.
It should add a few different elements, showcasing the different
scenarios, and then finally it should print the value of myUniqueList
to show that it worked.


Extra Credit:

Add another function that pushes all the rejected inputs into a separate
global array called myLeftovers. If someone tries to add a value to
myUniqueList but it's rejected (for non-uniqueness), it should get added
to myLeftovers instead.



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = "https://stackoverflow.com/a/44786454/4434088"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# ----------------------------------------------------------------------


def add_unique(x):
    check = check_absent(x, myUniqueList)
    if check:
        print(x, "is not present in myUniqueList.")
        print("adding", x, "to it ...\n")
        myUniqueList.append(x)
        showcase()
        return check
    else:
        print(x, "is already present in myUniqueList.")
        print("adding", x, "to myLeftovers ...\n")
        add_leftovers(x)
        showcase()
        return check


def add_leftovers(x):
    myLeftovers.append(x)


def showcase():
    print("myUniqueList is now:", myUniqueList)
    print("myLeftovers is now:", myLeftovers, "\n")


def check_equal(x, y):
    return x == y and type(x) == type(y)


def check_absent(x, data):
    return not any([check_equal(x, i) for i in data])


# ---- Functions' checks ----

myUniqueList = []
myLeftovers = []

print("\n\n=== Checks starts ===\n")

showcase()

check_res = [
    add_unique(1),
    not (add_unique(1)),
    myLeftovers == [1],
    check_equal(1, 1),
    not check_equal(1, 2),
    not check_equal(1, True),
    check_absent(0, [1, 2]),
    not check_absent(1, [1, 2]),
    check_absent(True, [1, 2]),
    check_absent(1, [True, 2]),
    check_absent(False, [0, 2]),
    check_absent(0, [False, 2]),
    check_absent(1, ["1", 2])
]

if all(check_res):
    print("\n=== All checks passed ===\n\n")

else:
    wrong = [i + 1 for i, x in enumerate(check_res) if not x]
    print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
    # how to stop script execution:
    # https://stackoverflow.com/a/44786454/4434088
    exit()

# ---- showcase ----

myUniqueList = []
myLeftovers = []

print("\n\n=== Baseline ===\n")
showcase()

print("\n\n=== Add new numbers ===\n")
add_unique(1)
add_unique(2)

print("\n\n=== Add new strings ===\n")
add_unique("1")  # a literal number is not a number
add_unique("a")
add_unique("b")
add_unique("3")
add_unique(3)  # a number is not a literal number

print("\n\n=== Add new booleans ===\n")
add_unique(True)  # Alert: `True in [1]` returns True!
add_unique(0)  # check solution for 0 and False too
add_unique(False)
add_unique("False")  # Literal boolean are not boolean

print("\n\n=== Add duplicates ===\n")
add_unique(1)
add_unique(True)
add_unique("False")
add_unique("False")  # repetition is admitted in myLeftovers
