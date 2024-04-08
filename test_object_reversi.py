import unittest
import sys
sys.path.append("/Users/matsuda/nuco/reversi")
from models.status import Status
from models.board import Board
from models.player import Player
from models.cpu_player import CpuPlayer
from object_reversi import Game

class Test_Game(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_finish_game(self):
        assert self.game._finish_game is None