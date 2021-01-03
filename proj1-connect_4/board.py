import json


def create_empty_cols(cols, rows):
    """ Create a new blank board

    A simple board is a collection (list) of columns (list) values
    """
    return [[0 for _ in range(rows)] for _ in range(cols)]


def get_row(board, num):
    """ get the row of a simple board
    """
    return [col[num] for col in board]


def get_number_of_rows(board):
    """ check the number of rows in each column of a simple board

    This function raises a TypeError if the columns are not all of the
    same size
    """
    if len(board) == 0:
        return 0
    rows = [len(col) for col in board]
    if len(set(rows)) != 1:
        raise TypeError("Broken Board!")
    return rows.pop()


def flip_updown(board):
    """ flip up/down a simple board
    """

    def _flip_col(col):
        return col[::-1]

    return [_flip_col(col) for col in board]


def diagonal_indeces(pnt, cols, rows):
    """ Indices for a positive diagonal going through a point

    :param pnt: a (col, row) tuple; the diagonal will pass through pnt
    :param cols: number of columns in the board
    :param rows: number of rows in the board
    """
    col, row = pnt
    offset = col - row
    if offset >= 0:
        pnt = (offset, 0)
    elif offset < 0:
        pnt = (0, -offset)
    while True:
        col, row = pnt
        if col >= cols:
            break
        if row >= rows:
            break
        # print(pnt, cols, rows)
        yield pnt
        pnt = (col + 1, row + 1)


class Board(object):
    """ The Boar Object

    Extends the functionalities of the simple board (list of columns)
    """

    def __init__(self, board, moves=(), valid=None, overwrite=True):
        """ base constructor

        :param board: a simple board (see create_empty_cols above)
        :param moves: a tuple of `(col, row, value)` already played moves
        :param valid: a list of valid values that can be played on the board
        :param overwrite: (bool) allow/disallow playing again on the same position
        """
        self.board = board
        self.cols = len(board)
        self.rows = get_number_of_rows(board)
        self.moves = moves
        self.valid = valid
        self.overwrite = overwrite

    def to_dict(self):
        """ Convert the Board class to a dict (convenient for serialization)
        """
        return {
            "board": self.board,
            "moves": self.moves,
            "valid": self.valid,
            "overwrite": self.overwrite,
        }

    def __str__(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        """ load a Board class from a dict (inverse of `to_dict`)
        """
        data["moves"] = tuple(tuple(move) for move in data.pop("moves", []))
        return cls(**data)

    @classmethod
    def loads(cls, data):
        """ Load a Board class from a string (inverse of `__str__`)
        """
        return cls.from_dict(json.loads(data))

    def __len__(self):
        return len(self.moves)

    def __getitem__(self, pos):
        """ allow indexing the board using the notation `Board[3, 4]`
        """
        col, row = pos
        return self.board[col][row]

    @classmethod
    def blank(cls, cols, rows, valid=None, overwrite=True):
        """ create a blank board """
        return cls(
            create_empty_cols(cols, rows),
            valid=valid,
            overwrite=overwrite)

    @classmethod
    def default_c4(cls):
        """ create a blank board to play a connect-4 game """
        return cls(
            create_empty_cols(7, 6),
            valid=[-1, 1],
            overwrite=False)

    @property
    def size(self):
        return (self.cols, self.rows)

    def flip_updown(self):
        """ flip up/donw (row-wise)
        """
        return Board(flip_updown(self.board))

    def flip_leftright(self):
        """ flip left/right (column-wise)
        """
        return Board(self.board[::-1])

    def get_row(self, num):
        """ get the values of a given row """
        return get_row(self.board, num)

    def get_col(self, num):
        """ get the values of a given col """
        return self.board[num]

    def get_diagonal(self, pnt, direction=1):
        """ the the diagonal values passing through a point
        """
        if direction == -1:
            col, row = pnt
            pnt = (col, self.rows - row - 1)
            return self.flip_updown().get_diagonal(pnt)
        indeces = diagonal_indeces(pnt, self.cols, self.rows)
        return [self.board[col][row] for col, row in indeces]

    @property
    def T(self):
        """ transpose board """
        return [self.get_row(num) for num in range(self.rows)]

    def move(self, col, row, value, ):
        """ Play a move

        move: a move consists of a row, col and value to be placed on
        the board
        """

        if self.valid is not None and value not in self.valid:
            raise TypeError(f"value -{value}- can only be set([1, -1])")

        if self.board[col][row] != 0 and not self.overwrite:
            raise TypeError(f"point ({col}, {row}) cannot be overwritten...")

        self.board[col][row] = value
        move = (col, row, value)
        self.moves = self.moves + (move, )
        return move

    def print_simple(self):
        """ a simple debugging function """
        for row in self.T[::-1]:
            print(row)
