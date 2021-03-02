from Domain.Constants import ROW_COUNT, COLUMN_COUNT, PLAYER_PIECE, AI_PIECE


class Repo:
    def __init__(self, board):
        self._board = board

    @property
    def board(self):
        return self._board

    def drop_piece(self, row, col, piece):
        """
        Fill the given board space with the specified piece
        :param row: row index of the given board space
        :param col: col index of the given board space
        :param piece: specified piece
        """
        self._board.board[row][col] = piece

    def is_valid_location(self, col):
        """
        Check if the given col is valid to fill(at least the top space is empty)
        :param col: col index of the given board space
        :return: True/False
        """
        return self._board.board[ROW_COUNT - 1, col] == 0

    def get_valid_locations(self):
        """
        Return a list with all the col index of the valid board columns to fill
        :return: List with all valid locations
        """
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def get_next_open_row(self, col):
        """
        Return the row index of the first empty board space of the given column
        :param col: col index of the given board space
        :return: row index of the of the first empty space
        """
        for r in range(ROW_COUNT):
            if self._board.board[r][col] == 0:
                return r

    def is_terminal_node(self):
        """
        Check if one of the 2 players won or if it the board is full
        :return: True/False
        """
        return self.winning_move(PLAYER_PIECE) or self.winning_move(AI_PIECE) or len(self.get_valid_locations()) == 0

    def winning_move(self, piece):
        """
        Check if a given player's/AI's piece is in winning format
        :param piece: player's/AI's piece
        :return: True/False
        """
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if self._board.board[r][c] == piece and self._board.board[r][c + 1] == piece and \
                        self._board.board[r][c + 2] == piece and self._board.board[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self._board.board[r][c] == piece and self._board.board[r + 1][c] == piece and \
                        self._board.board[r + 2][c] == piece and self._board.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if self._board.board[r][c] == piece and self._board.board[r + 1][c + 1] == piece and \
                        self._board.board[r + 2][c + 2] == piece and self._board.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if self._board.board[r][c] == piece and self._board.board[r - 1][c + 1] == piece and \
                        self._board.board[r - 2][c + 2] == piece and self._board.board[r - 3][c + 3] == piece:
                    return True
        # No winning moves until now
        return False
