# standard lib imports
import json
import functools

# local imports
from board import Board


def squish_sequence(values):
    """ Squish a sequence of values
    """
    prev = None
    count = 0
    for val in values:
        if prev is None:
            prev = val
            count = 0
        if val != prev:
            yield (prev, count, )
            prev = val
            count = 0
        count = count + 1
    if count > 0:
        yield (val, count)


def connect4_winning_sequence(values, threshold=4):
    for value, number in squish_sequence(values):
        if value != 0 and number >= threshold:
            return True, value
    return False, 0


def connect4_winning_point(pnt, board, threshold=4):
    """
    :param pnt: a point on a board (col, row)
    :param board: a Board object (not a simple board)
    :param threshold: a value (being connect-4, this should be 4, right?)
    """

    _win = lambda vals: connect4_winning_sequence(vals, threshold=threshold)
    col, row = pnt

    win, winner = _win(board.get_row(row))
    if win:
        return winner
    win, winner = _win(board.get_col(col))
    if win:
        return winner
    win, winner = _win(board.get_diagonal(pnt))
    if win:
        return winner
    win, winner = _win(board.get_diagonal(pnt, direction=-1))
    if win:
        return winner
    return 0


def connect4_winning_move(move, board, threshold=4):
    """
    :param pnt: a point on a board (col, row)
    :param board: a Board object (not a simple board)
    :param threshold: a value (being connect-4, this should be 4, right?)
    """
    col, row, player = move
    return connect4_winning_point((col, row), board, threshold=threshold)


def get_level(col):
    """ calculate the fill level of a column """
    for num, val in enumerate(col):
        if val == 0:
            return num


def get_levels(board):
    """ Calculate the fill level for all columns in a board """
    return [get_level(col) for col in board]


class GamePlay(object):

    def __init__(self, board, start_symbol="X", threshold=4, winner=0):
        """ Base Game Constructor
        :param board: a Board object
        :param start_player: symbol of the starting player {'X', 'O'}
        :param threshold: the winning streak threshold (4)
        :param winner: the winning player (0 for an ongoing game)
        """
        assert start_symbol in ["X", "O"]
        self.board = board
        self.start_symbol = start_symbol
        self.threshold = threshold
        self.winner = winner
        self._levels = get_levels(board.board)

    @classmethod
    def default_c4(cls, start_symbol="X", ):
        """ Create a Game with a default board (blank 6 * 7 board) """
        return cls(
            Board.default_c4(),
            start_symbol=start_symbol,
            threshold=4,
            winner=0)

    def __len__(self):
        return len(self.board)

    @property
    def won(self):
        if self.winner is None:
            self.winner = 0
        return self.winner != 0

    @property
    def drops(self):
        return [move[0] for move in self.board.moves]

    @property
    def last(self):
        if len(self) == 0:
            return None
        return self.board.moves[-1][0]

    @property
    def current(self):
        if len(self) == 0:
            return 1
        else:
            col, row, player = self.board.moves[-1]
            return -player

    def to_dict(self):
        """ Convert a GamePlay class to a dict object for serialization """
        return dict(
            board=self.board.to_dict(),
            start_symbol=self.start_symbol,
            threshold=self.threshold,
            winner=self.winner,
        )

    def __str__(self):
        """ Serialize a GamePlay class """
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        """ Load a GamePlay class from a dict object """
        data["board"] = Board.from_dict(data.pop("board"))
        return cls(**data)

    @classmethod
    def loads(cls, data):
        """ Deserialize/load a GamePlay class from a string """
        return cls.from_dict(json.loads(data))

    @classmethod
    def from_file_path(cls, file_name):
        with open(file_name, "r") as fid:
            return cls.loads(fid.read())

    def is_available(self, col):
        """ check if a given column is playable """
        if col >= self.board.cols:
            return False
        return self._levels[col] < self.board.rows

    def is_full(self, col):
        """ check if a given column is full """
        return not self.is_available(col)

    @property
    def availables(self):
        return [col for col in range(self.board.cols) if self.is_available(col)]

    def undo(self):
        if self.won:
            raise RuntimeError("cannot undo a completed game")
        if len(self) == 0:
            raise RuntimeError("cannot undo a new game")
        move = self.board.moves[-1]
        col, row, player = move
        self.board.board[col][row] = 0
        self.board.moves = self.board.moves[:-1]
        self._levels[col] = self._levels[col] - 1
        return move

    def drop(self, col):
        """ Drop a new piece into a column of the board """
        col = col - 1
        if self.won:
            raise RuntimeError(f"Game has been won by {self.winner}")
        if not self.is_available(col):
            raise TypeError(f"Column {col} full...")
        row = self._levels[col]
        move = self.board.move(col, row, self.current, )
        self._levels[col] = self._levels[col] + 1
        self.winner = connect4_winning_move(
            move, self.board, threshold=self.threshold)
        return move
