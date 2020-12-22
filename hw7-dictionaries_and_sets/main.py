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
__credits__ = "https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"

# ----------------------------------------------------------------------


# ---- Functions' checks ----

my_song = {
    "Title": "November Rain",
    "Year": 1992,
    "Month": 2,
    "Day": 18,
    "Artist": "Guns N' Roses",
    "Text": "Axl Rose",
    "Album": "Use Your Illusion I",
    "Genre": "Hard Rock",
    "Awards": "MTV Video Music Award for Best Cinematography",
    "DurationInSecondsAlbum": 537,
    "DurationInSecondsRadio": 283,
    "Platinum": 5,
    "Gold": 4,
    "Wiki": "https://en.wikipedia.org/wiki/November_Rain"
}

for entry in my_song:
    # https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/
    print(
        "My favourite song's " + entry +
        " is: " + str(my_song[entry]) + "."
    )


def guess_my_song_property(key, value):
    # I would like to be string/numeric inclusive
    return key in my_song and str(my_song[key]) == str(value)


print("\n\n=== Checks starts ===\n")
check_res = [
    guess_my_song_property("Title", "November Rain"),
    not guess_my_song_property("Title", "Sweet Child O' Mine"),
    not guess_my_song_property("foo", "November Rain"),
    not guess_my_song_property("foo", "bar"),
    guess_my_song_property("Gold", 4),
    guess_my_song_property("Gold", "4"),
]

if all(check_res):
    print("\n=== All checks passed ===\n\n")
else:
    wrong = [i + 1 for i, x in enumerate(check_res) if not x]
    print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
    exit()
