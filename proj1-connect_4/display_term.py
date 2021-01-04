import termcolor 


StartSymbolMaps = {

    # if the start symbol is X
    "X": {
        1: termcolor.colored("X", "red", attrs=["bold"]),
        0: termcolor.colored("*", "grey", attrs=[]),
        -1: termcolor.colored("O", "blue", attrs=["bold"]),
    },

    # if the start symbol is O
    "O": {
        1: termcolor.colored("O", "blue", attrs=["bold"]),
        0: termcolor.colored("*", "grey", attrs=[]),
        -1: termcolor.colored("X", "red", attrs=["bold"]),
    }

}


def symbol_mapper(game):
    return StartSymbolMaps[game.start_symbol]


def current_symbol(game):
    return StartSymbolMaps[game.start_symbol][game.current]


def winner_symbol(game):
    return StartSymbolMaps[game.start_symbol][game.winner]


def join_symbols(symbols, sep="|"):
    symbols = [""] + symbols + [""]
    return sep.join(symbols)


def print_titles(game):
    sym = [str(num + 1) for num in range(game.board.cols)]
    print(join_symbols(sym, "   "))


def print_game(game):
    symbol_map = symbol_mapper(game)
    board = game.board
    print_titles(game)
    for num, row in enumerate(board.T[::-1]):
        row_symbol = [symbol_map[val] for val in row]
        row_spacer = ["-" for val in row]
        print(join_symbols(row_spacer, " + "))
        print(join_symbols(row_symbol, " | "))
    print(join_symbols(row_spacer, " + "))
    print_titles(game)
