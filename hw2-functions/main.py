# -*- coding: utf-8 -*-

"""
main.py: Homework #2: Functions (Python Is Easy course by Pirple)

Details:

Let's return to the music example from assignment one. Pick 3 of the
attributes you listed. For our example we're going to say "Genre",
"Artist" and "Year". Create a new Python file and create 3 functions
with the same name as those attributes. So in this example we'd have one
function named "genre" another named "artist" and another called "year".

When someone calls any of those functions, that function should return
the corresponding value for that attribute. For example, if we call the
"Artist" function our function would return "Dave Brubeck". Yours should
return whatever values make sense for your music choice.


Extra Credit:

One of the data types we haven't covered yet is called "booleans".
When a variable is set to True or False, that's a boolean.
For extra credit, see if you can figure out how to use booleans, and add
an extra function that returns a boolean value instead of a String or
Number. Hint: make sure to capitalize the first letter in the words True
or False when you use them. We'll cover booleans more in the lecture on
"if" statements coming up next in the course.



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = "https://stackoverflow.com/questions/9437726/how-to-get-the-value-of-a-variable-given-its-name-in-a-string"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"

# ----------------------------------------------------------------------

Title = "November Rain"
Year = 1992
Artist = "Guns N' Roses"
Wiky = "https://en.wikipedia.org/wiki/November_Rain"


def print_favourite(what):
    # for lower() at: https://www.w3schools.com/python/ref_string_lower.asp
    # found globals() at: https://stackoverflow.com/questions/9437726/how-to-get-the-value-of-a-variable-given-its-name-in-a-string
    # for usage for globals() at: https://www.geeksforgeeks.org/python-globals-function/
    print(
        "My favourite song's", what.lower(), "is:",
        globals()[what.title()]
    )


def title():
    print_favourite("title")
    return Title


def year():
    print_favourite("year")
    return Year


def artist():
    print_favourite("artist")
    return Artist


def get_attributes(get_all=False):
    if get_all:
        print("Let's print principal arguments of my favourite song:\n")
        title()
        year()
        artist()
    else:
        print("Try to call `get_attributes()` passing `True` to it!\n")


get_attributes()
get_attributes(True)
