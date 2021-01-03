import game_play

import display_term as display


def store_game(game, path):
    if path is None or path == "":
        path = "."
    print(f"saving {len(game)}, {path}")
    with open(f"{path}/{len(game)}.dat", "w") as fid:
        fid.write(str(game))


def play(game, path=None):
    while not game.won:
        print()
        print(f"drop n. {len(game)}")
        display.print_game(game)
        message = (
            f"enter column number for player {display.current_symbol(game)}, " \
            f"u for undo and q for quit\n" \
            f"-> "
        )
        choice = input(message)
        if choice.lower() == "u":
            game.undo()
            continue
        if choice.lower() == "q":
            break
        drop = game.drop(int(choice))
        col, row, value = drop
        if path:
            store_game(game, path)

    if game.winner != 0:
        print(f"game ended!")
        print(f"and the winner is......... {display.winner_symbol(game)}!!! Well done!")
        print(f"final drop: ({col + 1}, {row + 1})")
        display.print_game(game)


if __name__ == "__main__":

    import argparse

    par = argparse.ArgumentParser(description="play a connect-4 game!")
    par.add_argument("--file-name", )
    par.add_argument("--save-path", )
    par.add_argument("--start-player", choices=["X", "O"])

    args = par.parse_args()
    if args.file_name:
        print(f"starting a game from file {args.file_name}")
        game = game_play.GamePlay.from_file_path(args.file_name)
    else:
        print(f"starting a default game")
        game = game_play.GamePlay.default_c4()
    play(game, path=args.save_path)
