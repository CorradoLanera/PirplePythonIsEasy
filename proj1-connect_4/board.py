def create_empty_cols(cols, rows):
    """ Create a new blank board

    A board is a collection (list) of columns (list) containing 
    `{-1, 0, 1}` values
    """
    return [[0 for _ in range(rows)] for _ in range(cols)]


def get_row(board, num):
    return [col[num] for col in board]


def get_level(col):
    """ calculate the fill level of a column """
    for num, val in enumerate(col):
        if val == 0:
            return num


def get_levels(board):
    """ Calculate the fill level for all columns in a board """
    return [get_level(col) for col in board]


def get_number_of_rows(board):
    """ check the number of rows in each column of a board 

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

    def _flip_col(col):
        return col[::-1]

    return [_flip_col(col) for col in board]


def diagonal_indeces(pnt, cols, rows):
    """ Indices for a positive diagonal going through a point
    :param pnt: a (col, row) tuple to grab the diagonal from
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

    Extends the functionalities of the simple board (list of columns);
    """

    def __init__(self, board):
        """ base constructor """
        self.board = board
        self.cols = len(board)
        self.rows = get_number_of_rows(board)
        self.levels = get_levels(board)

    def __getitem__(self, pos):
        """ allow indexing the board using the notation `Board[3, 4]`
        """
        col, row = pos
        return self.board[col][row]

    @classmethod
    def blank(cls, cols, rows):
        """ create a blank board """
        return cls(create_empty_cols(cols, rows))

    @classmethod
    def default(cls):
        """ create a blank board of default size """
        return cls(create_empty_cols(7, 6))

    def flip_updown(self):
        return Board(flip_updown(self.board))

    def flip_leftright(self):
        return Board(self.board[::-1])

    def get_row(self, num):
        """ get the values of a given row """
        return get_row(self.board, num)

    def get_col(self, num):
        """ get the values of a given col """
        return self.board[num]

    def get_diagonal(self, pnt, direction=1):
        # print(pnt, self.board)
        if direction == -1:
            col, row = pnt
            pnt = (col, self.rows - row - 1)
            return self.flip_updown().get_diagonal(pnt)
        indeces = diagonal_indeces(pnt, self.cols, self.rows)
        return [self.board[col][row] for col, row in indeces]

    def is_available(self, col):
        """ check if a given column is playable """
        if col >= self.cols:
            return False
        return self.levels[col] < self.rows

    def is_full(self, col):
        """ check if a given column is full """
        return not self.is_available(col)

    @property
    def available(self):
        return [col for col in range(self.cols) if self.is_available(col)]

    @property
    def T(self):
        """ transpose board """
        return [self.get_row(num) for num in range(self.rows)]

    def drop(self, value, col):
        if not self.is_available(col):
            raise TypeError(f"Column {col} full...")
        if value not in [1, -1]:
            raise TypeError(f"value -{value}- can only be set([1, -1])")
        move = (col, self.levels[col], value)
        self.board[col][self.levels[col]] = value
        self.levels[col] = self.levels[col] + 1
        return move

    def print_simple(self):
        """ a simple debugging function """
        for row in self.T[::-1]:
            print(row)
