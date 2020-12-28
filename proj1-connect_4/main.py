# -*- coding: utf-8 -*-

"""
main.py: Project #1: Connect 4 (Python Is Easy course by Pirple)

Details:

Have you ever played "Connect 4"? It's a popular kid's game by the
Hasbro company. In this project, your task is create a Connect 4 game in
Python. Before you get started, please watch this video on the rules of
Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly
straightforward. You'll want to draw the board, and allow two players to
take turns placing their pieces on the board (but as you learned above,
they can only do so by choosing a column, not a row). The first player to
get 4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O
instead.


Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to
figure out how to import a package like termcolor into your project.
We're going to cover importing later in the course, but try and see if
you can figure it out on your own. Or you might be able to find unicode
characters to use instead, depending on what your system supports.
Here's a hint: print(u'\u2B24')



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = []
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"

# --- PROGRAM DEFINITIONS ----------------------------------------------


# --- PROGRMA CHECKS AND INTERACTIONS ----------------------------------

if __name__ == '__main__':

    # ---- Functions' checks ----
    print("\n\n=== Checks starts ===\n")
    check_res = [
    ]


    if all(check_res):
        print("\n=== All checks passed ===\n\n")
    else:
        wrong = [i + 1 for i, x in enumerate(check_res) if not x]
        print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
        exit()

    # ---- Execution ----
    like_to_start = input(
        "Press Enter to start the interactive simulation" +
        " (anything else will quit it)."
    )
    go = like_to_start == ""
    while go is True:
        print("!!! Here will run the program !!!")
        go_on = input(
            "Press Enter to continue the interactive simulation" +
            " (anything else will quit it)."
        )
        go = go_on == ""
