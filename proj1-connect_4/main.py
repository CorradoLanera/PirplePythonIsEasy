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
__credits__ = [
    "https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/",
    "https://stackoverflow.com/questions/22054698/python-modifying-list-inside-a-function",
    "https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy-it-to-prevent",
    "https://www.programiz.com/python-programming/methods/list/copy",
    "https://stackoverflow.com/questions/28684154/python-copy-a-list-of-lists",
    "https://pypi.org/project/termcolor/"
]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"

# --- MODULES ----------------------------------------------------------
import copy  # required for `put_piece()`
from termcolor import colored  # required in `select_player(player)`


# --- PROGRAM DEFINITIONS ----------------------------------------------
def draw_new_board():
    cols = 7
    rows = 6
    rows_range = range(2 * rows + 1)
    cols_range = range(2 * cols + 1)
    # https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/
    board = [["" for i in cols_range] for j in rows_range]
    for x in rows_range:
        if x % 2 == 0:
            # dash-es line
            board[x] = ["-" for i in cols_range]
        else:
            # vert and space line
            for y in cols_range:
                if y % 2 == 0:
                    # vert
                    board[x][y] = "|"
                else:
                    # space
                    board[x][y] = " "
    return board


def print_board(x):
    for j in range(len(x)):
        for i in range(len(x[j])):
            print(x[j][i], end=" ")
        print()


def select_player(player):
    if player == 1:
        selected_piece = colored("X", "red", attrs=["bold"])
    elif player == 2:
        selected_piece = colored("O", "blue", attrs=["bold"])
    else:
        print("Wrong player selected")
        selected_piece = colored("!!!", "grey", attrs=["bold"])

    return selected_piece


def check_player(player):
    player_set = {1, 2}
    player_ok = player in player_set
    while player_ok is not True:
        player = int(input(
            "Only player 1 or 2 are allowed. Who play now? "
        ))
        player_ok = player in player_set
    return player


def check_column(column):
    col_set = {1, 2, 3, 4, 5, 6, 7}
    column_ok = column in col_set
    while column_ok is not True:
        column = int(input(
            "Column range from 1 to 7. Where do you like to play? "
        ))
        column_ok = column in col_set
    return column


def check_row_col(board, column):
    row_range = range(len(board))
    row_ok = False
    first_empty = 0

    while row_ok is not True:
        column_at_board = 2 * column - 1
        # print("col at board: ", column_at_board)
        col = [board[i][column_at_board] for i in row_range if i % 2 != 0]
        # print("col: ", col)

        empties = [i + 1 for i, j in enumerate(col) if j == " "]
        # print("empties: ", empties)
        row_ok = empties != []
        # print("row_ok", row_ok)
        if row_ok is True:
            first_empty = max(empties)
        else:
            column = int(input(
                "Selected column is full. Please, select another column: "
            ))
            column = check_column(column)
    return first_empty, column


def put_piece(board, player, column):
    player = check_player(player)
    piece = select_player(player)

    column = check_column(column)

    row, col = check_row_col(board, column)
    row_at_board = 2 * row - 1
    col_at_board = 2 * col - 1

    # https://stackoverflow.com/questions/22054698/python-modifying-list-inside-a-function
    # https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy-it-to-prevent
    # https://www.programiz.com/python-programming/methods/list/copy
    # https://stackoverflow.com/questions/28684154/python-copy-a-list-of-lists
    updated_board = copy.deepcopy(board)
    updated_board[row_at_board][col_at_board] = piece

    return updated_board


def check_sequence(x, n):
    if n > len(x):
        return [False, " "]
    for i in range(len(x) - n + 1):  # all possible starting points
        ref = x[i]
        if ref == " ":
            continue
        res = True
        for j in range(n):
            res = res and (ref == x[i + j])
        if res is True:
            return [True, ref]

    return [False, " "]


def check_row(board, i):
    i_in_board = 2 * i - 1
    row = [x for x in board[i_in_board] if x not in {"|", " "}]
    return check_sequence(row, 4)


def check_col(board, j):
    j_in_board = 2 * j - 1
    col = [board[i][j_in_board] for i in range(13) if i % 2 != 0]
    return check_sequence(col, 4)


def are_in_diag(i, j, index_sum, rev=False):
    if rev is True:
        check = i - j == index_sum
    else:
        check = i + j == index_sum

    return check


def check_diag(board, index_sum, rev=False):
    row_range = range(int((len(board) - 1) / 2))
    col_range = range(int((len(board[0]) - 1) / 2))

    rows = [i + 1 for i in row_range]
    cols = [j + 1for j in col_range]

    diag = [
        board[2 * i - 1][2 * j - 1] for i in rows for j in cols if
        are_in_diag(i, j, index_sum, rev=rev)
    ]
    return check_sequence(diag, 4)


def empties_in_board(board):
    empties = 0
    for i in board:
        for j in i:
            if j == " ":
                empties += 1
    return empties


def end(board):
    rows = [1, 2, 3, 4, 5, 6]
    cols = [1, 2, 3, 4, 5, 6, 7]

    empties = empties_in_board(board)
    print("Empties left: ", empties)

    for i in rows:
        winner = check_row(board, i)
        if winner[0]:
            return winner

    for j in cols:
        winner = check_col(board, j)
        if winner[0]:
            return winner

    for index_sum in range(2, 13):  # possible i + j (+1 for `range()`)
        winner = check_diag(board, index_sum)
        if winner[0]:
            return winner

    for index_sum in range(-5, 7):  # possible i - j (+1 for `range()`)
        winner = check_diag(board, index_sum, rev=True)
        if winner[0]:
            return winner

    if empties == 0:  # if none have won in the very last move
        return [True, "none"]

    return [False, " "]


def play(game=draw_new_board(), first_player=0):
    """
    Play a "Connect 4" game.
    :param game: a board (by default create a new empty one); this
      param is useful to continue a previous saved game.
    :param first_player: player starting to play (by default it is 0,
      which does not exists, so triggering the query of who start to
      play.
    :return: At the end of the game, return the final board.
    """
    print_board(game)
    current_player = check_player(first_player)
    res = "none"

    in_game = True
    while in_game is True:
        print("It is the turn of player ", current_player)
        column = int(input("Select a column for your piece: "))
        game = put_piece(game, current_player, column)
        print_board(game)
        current_player = abs(3 - current_player)

        res = end(game)
        # print("res: ", res)
        in_game = not res[0]
        continue_playing = input(
            "Press Enter to continue playing " +
            " (or anything else to stop and get the current board)."
        )
        if continue_playing != "":
            print("Game Interrupted. No one win... for the moment!")
            print("This is the last board")
            print_board(game)
            return game

    res = {
        select_player(1): "player 1",
        select_player(2): "player 2",
        "none": "none"
    }[res[1]]
    print("Game Over. The winner is:", res)
    return game


# --- PROGRAM CHECKS AND INTERACTIONS ----------------------------------

if __name__ == '__main__':

    # ---- Functions' checks ----
    print("\n\n=== Checks starts ===\n")
    nb = draw_new_board()
    p1X = colored("X", "red", attrs=["bold"])
    p2O = colored("O", "blue", attrs=["bold"])
    pERROR = colored("!!!", "grey", attrs=["bold"])
    first_run = put_piece(nb, 1, 1)  # this require a copy.deepcopy()!!
    winner_col = put_piece(first_run, 1, 1)
    winner_col = put_piece(winner_col, 1, 1)
    winner_col = put_piece(winner_col, 1, 1)
    winner_row = put_piece(first_run, 1, 2)
    winner_row = put_piece(winner_row, 1, 3)
    winner_row = put_piece(winner_row, 1, 4)
    winner_diag = put_piece(first_run, 2, 2)
    winner_diag = put_piece(winner_diag, 1, 2)
    winner_diag = put_piece(winner_diag, 2, 3)
    winner_diag = put_piece(winner_diag, 2, 3)
    winner_diag = put_piece(winner_diag, 1, 3)
    winner_diag = put_piece(winner_diag, 2, 4)
    winner_diag = put_piece(winner_diag, 2, 4)
    winner_diag = put_piece(winner_diag, 2, 4)
    winner_diag = put_piece(winner_diag, 1, 4)
    winner_diag = put_piece(winner_diag, 1, 1)
    winner_diag = put_piece(winner_diag, 1, 1)
    winner_diag = put_piece(winner_diag, 2, 1)
    winner_diag = put_piece(winner_diag, 2, 2)
    full_board = put_piece(winner_diag, 2, 2)
    full_board = put_piece(full_board, 2, 1)
    full_board = put_piece(full_board, 2, 2)
    full_board = put_piece(full_board, 2, 1)
    full_board = put_piece(full_board, 2, 2)
    full_board = put_piece(full_board, 2, 3)
    full_board = put_piece(full_board, 2, 3)
    full_board = put_piece(full_board, 2, 4)
    full_board = put_piece(full_board, 2, 3)
    full_board = put_piece(full_board, 2, 4)
    full_board = put_piece(full_board, 2, 5)
    full_board = put_piece(full_board, 2, 6)
    full_board = put_piece(full_board, 2, 7)
    full_board = put_piece(full_board, 2, 5)
    full_board = put_piece(full_board, 2, 6)
    full_board = put_piece(full_board, 2, 7)
    full_board = put_piece(full_board, 2, 5)
    full_board = put_piece(full_board, 2, 6)
    full_board = put_piece(full_board, 2, 7)
    full_board = put_piece(full_board, 2, 5)
    full_board = put_piece(full_board, 2, 6)
    full_board = put_piece(full_board, 2, 7)
    full_board = put_piece(full_board, 2, 5)
    full_board = put_piece(full_board, 2, 6)
    full_board = put_piece(full_board, 2, 7)
    full_board = put_piece(full_board, 2, 5)
    full_board = put_piece(full_board, 2, 6)
    full_board = put_piece(full_board, 2, 7)

    check_res = [
        len(nb) == 13,  # rows
        len(nb[0]) == 15,  # cols
        len(nb[0]) == len(nb[1]),
        select_player(1) == p1X,
        select_player(2) == p2O,
        # 5
        select_player(3) == pERROR,
        check_player(1) == 1,
        check_player(2) == 2,
        check_column(1) == 1,
        nb[11][1] == " ",  # should be empty even after put_piece()
        # 10
        check_row_col(nb, 1)[0] == 6,
        check_row_col(nb, 1)[1] == 1,
        len(first_run) == len(nb),
        len(first_run[0]) == len(nb[0]),
        len(first_run[1]) == len(nb[0]),
        # 15
        first_run[11][1] == p1X,
        check_row_col(first_run, 1)[0] == 5,
        [True, 1] == check_sequence([1, 2, 3, 4], 1),
        [False, " "] == check_sequence([1, 2, 3, 4], 2),
        [True, 1] == check_sequence([1, 1, 3, 4, 6], 2),
        # 20
        [True, 3] == check_sequence([1, 2, 3, 3], 2),
        [True, 1] == check_sequence([1, 1, 1, 4], 3),
        [True, 1] == check_sequence([4, 1, 1, 1], 3),
        [True, 1] == check_sequence([1, 1, 1, 1, 1, 6, 8, 7], 4),
        [True, 3] == check_sequence([1, 2, 3, 3, 3, 3, 8, 7], 4),
        # 25
        [False, " "] == check_sequence([3, 3, 3, 4, 4, 3, 3, 3], 4),
        [True, p1X] == check_col(winner_col, 1),
        check_col(winner_col, 2)[0] is False,
        [True, p1X] == check_row(winner_row, 6),
        check_row(winner_row, 5)[0] is False,
        # 30
        [True, p1X] == check_diag(winner_diag, 7),
        check_diag(winner_diag, 8)[0] is False,
        [True, p2O] == check_diag(winner_diag, 2, rev=True),
        check_diag(winner_diag, 3, rev=True)[0] is False,
        empties_in_board(nb) == 42,
        # 35
        empties_in_board(first_run) == 41,
        empties_in_board(winner_row) == 38,
        empties_in_board(winner_col) == 38,
        empties_in_board(winner_diag) == 28,
        empties_in_board(full_board) == 0,
        # 40
        [False, " "] == end(nb),
        [True, p1X] == end(winner_row),
        [True, p1X] == end(winner_col),
        [True, p1X] == end(winner_diag),  # main diag evaluated first!
        [True, p2O] == end(full_board),  # start from upper horizontal!
    ]

    if all(check_res):
        print("\n=== All", len(check_res), "checks passed ===\n\n")
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
        play()
        go_on = input(
            "Press Enter to continue the interactive simulation" +
            " (anything else will quit it)."
        )
        go = go_on == ""
