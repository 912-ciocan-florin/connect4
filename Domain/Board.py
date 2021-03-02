import numpy as np


class Board:
    def __init__(self, rows, columns):
        """
        Create a memory representation of the board using numpy
        """
        self._board = np.zeros((rows, columns))

    @property
    def board(self):
        return self._board

    def __str__(self):
        """
        Return the _board for print as a numpy representation(flipped - guided by the game logic)
        """
        return str(np.flip(self._board, 0))
