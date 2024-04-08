import unittest
import sys
sys.path.append("/Users/matsuda/nuco/reversi")
from models.status import Status


class TestStatus(unittest.TestCase):
    def test_label_of(self):
        assert Status.label_of("space") == Status.SPACE
        assert Status.label_of("black") == Status.BLACK
        assert Status.label_of("white") == Status.WHITE

    def test_val(self):
        assert Status.SPACE.val == "･"
        assert Status.BLACK.val == "○"
        assert Status.WHITE.val == "●"

    def test_lab(self):
        assert Status.SPACE.lab == "space"
        assert Status.BLACK.lab == "black"
        assert Status.WHITE.lab == "white"
