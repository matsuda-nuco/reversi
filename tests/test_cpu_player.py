import unittest
import sys
import random
sys.path.append("/Users/matsuda/nuco/reversi")
from models.status import Status
from models.board import Board
from models.cpu_player import CpuPlayer

class TestCpuPlayer(unittest.TestCase):
    def setUp(self):
        self.cpu_player = CpuPlayer("player1", Status.BLACK)
        self.cpu_player.board.pieces[3][5].state = Status.BLACK
        self.cpu_player.board.pieces[4][5].state = Status.WHITE
        self.cpu_player.board.pieces[5][5].state = Status.BLACK

    def test_put_piece(self):
        self.cpu_player._put_piece()
        assert self.cpu_player.piece_has == 29
        self.cpu_player._put_piece()
        assert self.cpu_player.piece_has == 28

    def test_can_put_place(self):
        test_list = self.cpu_player._can_put_place()
        px, py = random.choice(test_list)
        assert self.cpu_player.board.is_already_put(px, py) == False
        assert self.cpu_player.board.enable_put(px, py, self.cpu_player.color) == False

    def test_choice_place(self):
        px, py = self.cpu_player.choice_place()
        assert self.cpu_player.board.is_already_put(px, py) == False
        assert self.cpu_player.board.enable_put(px, py, self.cpu_player.color) == False
        assert self.cpu_player.piece_has == 29