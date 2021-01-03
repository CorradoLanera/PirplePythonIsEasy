StartSymbolMaps = {

    # if the start symbol is X
    "X": {
        1: "X",
        0: "*",
        -1: "O"
    },

    # if the start symbol is O
    "O": {
        1: "O",
        0: "*",
        -1: "X"
    }

}


def symbol_mapper(game):
    return StartSymbolMaps[game.start_symbol]


def current_symbol(game):
    return StartSymbolMaps[game.start_symbol][game.current]


def print_col_names(cols):
    col_names = [str(num + 1) for num in range(cols)]
    print("    " + " ".join(col_names))


def print_col_vert(cols):
    print("    " + " ".join("|" for _ in range(cols)))


def print_game(game):
    symbol_map = symbol_mapper(game)
    board = game.board
    print_col_names(board.cols)
    print_col_vert(board.cols)
    for num, row in enumerate(board.T[::-1]):
        row = [symbol_map[val] for val in row]
        print(f"{board.rows - num} - " + " ".join(row))
    print_col_vert(board.cols)
    print_col_names(board.cols)
