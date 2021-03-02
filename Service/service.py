class Service:
    def __init__(self, repo):
        self._repo = repo

    @property
    def repo(self):
        return self._repo

    def drop_piece(self, row, col, piece):
        self._repo.drop_piece(row, col, piece)

    def is_valid_location(self, col):
        return self._repo.is_valid_location(col)

    def get_next_open_row(self, col):
        return self._repo.get_next_open_row(col)

    def winning_move(self, piece):
        return self._repo.winning_move(piece)
