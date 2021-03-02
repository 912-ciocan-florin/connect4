from unittest import TestCase
import unittest

import numpy

from Domain.Board import Board
from Repo.repo import Repo
from Service.service import Service


class TestService(TestCase):
    def setUp(self):
        self._repo = Repo(Board(6, 7))
        self._service = Service(self._repo)

    def test_str(self):
        self.assertEqual(str(self._service.repo.board), str(numpy.zeros((6, 7))))

    def test_repo(self):
        self.assertEqual(self._service.repo, self._repo)

    def test_drop_piece(self):
        self._service.drop_piece(0, 0, 1)
        board = self._service.repo.board.board
        self.assertEqual(board[0][0], 1)

    def test_is_valid_location(self):
        self.assertEqual(self._service.is_valid_location(0), True)
        self._service.drop_piece(0, 0, 1)
        self._service.drop_piece(1, 0, 1)
        self._service.drop_piece(2, 0, 1)
        self._service.drop_piece(3, 0, 1)
        self._service.drop_piece(4, 0, 1)
        self._service.drop_piece(5, 0, 1)
        self.assertEqual(self._service.is_valid_location(0), False)

    def test_get_next_open_row(self):
        self.assertEqual(self._service.get_next_open_row(0), 0)

    def test_winning_move_0(self):
        self.assertEqual(self._service.winning_move(1), False)
        # Test Vertical Win
        self._service.drop_piece(0, 0, 1)
        self._service.drop_piece(1, 0, 1)
        self._service.drop_piece(2, 0, 1)
        self._service.drop_piece(3, 0, 1)
        self.assertEqual(self._service.winning_move(1), True)

    def test_winning_move_1(self):
        self.assertEqual(self._service.winning_move(1), False)
        # Test Horizontal Win
        self._service.drop_piece(0, 0, 1)
        self._service.drop_piece(0, 1, 1)
        self._service.drop_piece(0, 2, 1)
        self._service.drop_piece(0, 3, 1)
        self.assertEqual(self._service.winning_move(1), True)

    def test_winning_move_2(self):
        self.assertEqual(self._service.winning_move(1), False)
        # Test Diagonal Win 1
        self._service.drop_piece(0, 0, 1)
        self._service.drop_piece(1, 1, 1)
        self._service.drop_piece(2, 2, 1)
        self._service.drop_piece(3, 3, 1)
        self.assertEqual(self._service.winning_move(1), True)

    def test_winning_move_3(self):
        self.assertEqual(self._service.winning_move(1), False)
        # Test Diagonal Win 2
        self._service.drop_piece(0, 3, 1)
        self._service.drop_piece(1, 2, 1)
        self._service.drop_piece(2, 1, 1)
        self._service.drop_piece(3, 0, 1)
        self.assertEqual(self._service.winning_move(1), True)


if __name__ == '__main__':
    unittest.main()
