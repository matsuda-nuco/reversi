import unittest
import sys
sys.path.append("/Users/matsuda/nuco/reversi")
from models.status import Status
from models.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.pieces[3][5].state = Status.BLACK
        self.board.pieces[4][5].state = Status.WHITE
        self.board.pieces[5][5].state = Status.BLACK

    def test_is_already_put(self):
        assert self.board.is_already_put(5, 5)

    def test__set_piece_put(self):
        self.board.set_piece_to(5, 3, Status.WHITE)
        assert self.board.pieces[3][5].state == Status.WHITE
        assert self.board.last_puted_rocation[0] == 5
        assert self.board.last_puted_rocation[1] == 3
        assert self.board.last_puted_color == Status.WHITE

    def test_count_black_area(self):
        assert self.board._count_black_area() == 2

    def test_count_white_area(self):
        assert self.board._count_white_area() == 1

    def test_black_is_win(self):
        assert self.board.black_is_win()

    def test_update(self):
        self.board.set_piece_to(5, 3, Status.BLACK)
        self.board.update()
        assert self.board.pieces[4][5].state == Status.BLACK

    def test_enable_put(self):
        assert self.board.enable_put(5, 4, Status.WHITE)