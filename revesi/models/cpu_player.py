import random
from models.status import Status
from models.board import Board

class CpuPlayer:
    def __init__(self, name, color):
        self.piece_has = 32  # オセロのコマの所持数
        self.name = name
        self.color = color
        self.board = Board()

    def _put_piece(self):
        self.piece_has -= 1

    def _can_put_place(self):
        can_put_list = []
        for i in range(0,8):
            for j in range(0,8):
                px = i
                py = j
                choice_color = Status.label_of(self.color)
                if self.board.is_already_put(px, py):
                    continue
                if self.board.put_piece_check(px, py, choice_color):
                    continue
                can_put_list.append((px, py))
        return can_put_list

    def choice_place(self):
            choice_color = Status.label_of(self.color)
            available_list = self._can_put_place()
            while True:
                px, py = random.choice(available_list)
                if self.board.is_already_put(px, py):
                    continue
                if self.board.put_piece_check(px, py, choice_color):
                    continue
                print("{}({})の手番です".format(self.name, self.color))
                print(f"残りコマ数：{self.piece_has}")
                print(available_list)
                break
            self._put_piece
            return px, py