# standard lib imports
import json
import functools

# local imports
import board


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


def connect4_winning_drop(drop, board, threshold=4):
    """
    :param pnt: a point on a board (col, row)
    :param board: a Board object (not a simple board)
    :param threshold: a value (being connect-4, this should be 4, right?)
    """
    col, row, player = drop
    return connect4_winning_point((col, row), board, threshold=threshold)



class GamePlay(object):

    def __init__(self, board, drops=(), start_symbol="X", threshold=4, winner=0):
        """ Base Game Constructor
        :param board: a Board object
        :param drops: full history of drops (as returned by Board.drop())
        :param start_player: symbol of the starting player {'X', 'O'}
        """
        assert start_symbol in ["X", "O"]
        self.board = board
        self.start_symbol = start_symbol
        self.threshold = threshold
        self.drops = tuple(tuple(drop) for drop in drops)
        self.winner = winner

    @property
    def won(self):
        if self.winner is None:
            self.winner = 0
        return self.winner != 0

    @property
    def moves(self):
        return len(self.drops)

    @property
    def last(self):
        if self.moves == 0:
            return None
        return self.drops[-1]

    @property
    def current(self):
        if self.moves == 0:
            return 1
        else:
            col, row, player = self.last
            return -player

    @classmethod
    def blank(cls, cols, rows, start_symbol="X", threshold=4):
        """ Create a Game with a blank board """
        return cls(
            board.Board.blank(cols, rows),
            start_symbol=start_symbol,
            threshold=threshold)

    @classmethod
    def default(cls, start_symbol="X", threshold=4):
        """ Create a Game with a default board (blank 6 * 7 board) """
        return cls(
            board.Board.default(),
            start_symbol=start_symbol,
            threshold=threshold)

    def to_dict(self):
        """ Convert a GamePlay class to a dict object for serialization """
        return dict(
            board=self.board.board,
            drops=self.drops,
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
        return cls(
            board=board.Board(data.pop("board")),
            drops=data.pop("drops", tuple()),
            start_symbol=data.pop("start_symbol", "X"),
            threshold=data.pop("threshold", 4),
            winner=data.pop("winner", 0)
        )

    @classmethod
    def loads(cls, data):
        """ Deserialize/load a GamePlay class from a string """
        return cls.from_dict(json.loads(data))

    @classmethod
    def from_file_path(cls, file_name):
        with open(file_name, "r") as fid:
            return cls.loads(fid.read())

    def drop(self, col):
        """ Drop a new piece into a column of the board """
        if self.won:
            raise RuntimeError(f"Game has been won by {self.winner}")
        drop = self.board.drop(self.current, col - 1)
        self.winner = connect4_winning_drop(drop, self.board, threshold=self.threshold)
        self.drops = tuple(self.drops + (drop, ))
        return drop
