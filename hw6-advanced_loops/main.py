# -*- coding: utf-8 -*-

"""
main.py: Homework #6: Advanced Loops (Python Is Easy course by Pirple)

Details:

Create a function that takes in two parameters: rows, and columns, both
of which are integers. The function should then proceed to draw a
playing board (as in the examples from the lectures) the same number of
rows and columns as specified. After drawing the board, your function
should return True.


Extra Credit:

Try to determine the maximum width and height that your terminal and
screen can comfortably fit without wrapping. If someone passes a value
greater than either maximum, your function should return False.



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
__version__ = "1.0.0"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# ----------------------------------------------------------------------
#   01234
# 0 -----
# 1 | | |
# 2 -----
# one row is two lines of dash-es and one of vert
# n rows are n+1 lines of dash-es and n of vert
#
# one column is three dash-es in the dashes' line and two vert and a s
#   pace in the vert's line
# n columns are 2n+1 dash-es in the dashes' line and n+1 vert and n
#   spaces in the vert's line



# https://stackoverflow.com/questions/366422/what-is-the-pythonic-way-to-avoid-default-parameters-that-are-empty-lists
def draw_board_xy(rows, cols=None, max_x_screen=None, max_y_screen=None):
    if cols is None:
        print("Square board drawing...")
        cols = rows
    rows_range = range(2*rows + 1)
    cols_range = range(2*cols + 1)

    # assuming 21 rows and 72 col limits for standard screen
    # that means:
    if max_y_screen is None:
        print("Assuming y screen dimension (i.e., printable rows) is 21")
        max_y_screen = 21
    if max_x_screen is None:
        print("Assuming x screen dimension (i.e., printable columns) is 72")
        max_x_screen = 72

    # https://note.nkmk.me/en/python-divmod-quotient-remainder/
    max_rows = int(((max_y_screen - 1) / 2) // 1)
    max_cols = int(((max_x_screen - 1) / 2) // 1)  # remove decimal part  (quotient of the division by 1)

    if rows > max_rows or cols > max_cols:
        print("Too big board (max rows = " + str(max_rows) +
              ", and max cols = " + str(max_cols) + ")")
        return False

    print("\nDrawing a board of " + str(rows) + " rows and " + str(cols) + " cols...\n")
    for x in rows_range:
        if x % 2 == 0:
            # dash-es line
            print("-"*len(cols_range))
        else:
            # vert and space line
            for y in cols_range:
                if y % 2 == 0:
                    # vert
                    print("|", end="")
                else:
                    # space
                    print(" ", end="")
            # newline
            print()
    print("Board ready.\n\n\n")
    return True

# ---- Functions' checks ----



print("\n\n=== Checks starts ===\n")
check_res = [
    draw_board_xy(2, 2),
    draw_board_xy(2, 19),
    draw_board_xy(5, 35),
    draw_board_xy(5),
    not draw_board_xy(11, 10),
    draw_board_xy(11, 10, max_y_screen=25),
    not draw_board_xy(5, 40),
    draw_board_xy(5, 40, max_x_screen=90),
    not draw_board_xy(11, 40),
    draw_board_xy(11, 40, max_y_screen=25, max_x_screen=90),
]

if all(check_res):
    print("\n=== All checks passed ===\n\n")
else:
    wrong = [i + 1 for i, x in enumerate(check_res) if not x]
    print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
    exit()
