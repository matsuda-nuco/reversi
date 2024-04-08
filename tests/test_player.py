import unittest
import sys
import module
sys.path.append("/Users/matsuda/nuco/reversi")
from models.status import Status
from models.board import Board
from models.player import Player


# def stub_stdin(testcase_inst, inputs):
#     stdin = sys.stdin

#     def cleanup():
#         sys.stdin = stdin

#     testcase_inst.addCleanup(cleanup)
#     sys.stdin = io.StringIO(inputs)


# def stub_stdouts(testcase_inst):
#     stdout = sys.stdout

#     def cleanup():
#         sys.stdout = stdout

#     testcase_inst.addCleanup(cleanup)
#     sys.stdout = io.StringIO()

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("player1", Status.BLACK)
        self.player.board.pieces[3][5].state = Status.BLACK
        self.player.board.pieces[4][5].state = Status.WHITE
        self.player.board.pieces[5][5].state = Status.BLACK

    def test_put_piece(self):
        self.player._put_piece()
        assert self.player.piece_has == 29
        self.player._put_piece()
        assert self.player.piece_has == 28

    def test_choice_place(self):
        # Override the Python built-in input method
        self.mock.patch.object(__builtins__, 'input', lambda: '5 3')
        # Call the function you would like to test (which uses input)
        # monkeypatch.setattr('builtins.input', TestPlayer,lambda: '5 3')
        # stub_stdin(self, "1 2\n")
        # stub_stdouts(self)
        px, py = self.player.choice_place()
        assert px == 5 and py == 3