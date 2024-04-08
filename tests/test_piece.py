import unittest
import sys
sys.path.append("/Users/matsuda/nuco/reversi")
from models.piece import Piece
from models.status import Status

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece(1, 1)
        self.piece.state = Status.BLACK

    def test_reverse_piece(self):
        self.piece.reverse_piece()
        assert self.piece.state == Status.WHITE
        self.piece.reverse_piece()
        assert self.piece.state == Status.BLACK
        # self.piece.state = Status.SPACE

    # def tearDown(self):
    #     self.piece = Piece(1, 1)