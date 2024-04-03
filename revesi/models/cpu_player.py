import random
from models.status import Status

class CpuPlayer:
    def __init__(self, color):
        self.piece_has = 32  # オセロのコマの所持数
        self.color = Status.label_of(color)

    def _put_piece(self):
        self.piece_has -= 1

    def choice_place(self):
            available_list = [i for i in range(0,8)]
            px, py = random.choice(available_list)
            self._put_piece
            return px, py