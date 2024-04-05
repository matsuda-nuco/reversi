import random
from models.status import Status
from models.board import Board


class CpuPlayer:
    def __init__(self, name: str, color: Status):
        self.piece_has = 30  # オセロのコマの所持数
        self.name = name
        self.color = color
        self.board = Board()

    def _put_piece(self) -> None:
        self.piece_has -= 1

    def _can_put_place(self) -> list:
        can_put_list = []
        for i in range(0,8):
            for j in range(0,8):
                px = i
                py = j
                if self.board.is_already_put(px, py):
                    continue
                if self.board.enable_put(px, py, self.color):
                    continue
                can_put_list.append((px, py))
        return can_put_list

    def choice_place(self) -> tuple:
            available_list = self._can_put_place()
            while True:
                px, py = random.choice(available_list)
                if self.board.is_already_put(px, py):
                    continue
                if self.board.enable_put(px, py, self.color):
                    continue
                print("{}({})の手番です".format(self.name, self.color.val))
                print(f"残りコマ数：{self.piece_has}")
                break
            self._put_piece()
            return px, py