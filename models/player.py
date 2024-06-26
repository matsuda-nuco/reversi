from models.status import Status
from models.board import Board


class Player:
    def __init__(self, name: str, color: Status):
        self.piece_has = 30  # オセロのコマの所持数
        self.board = Board()
        self.name = name
        self.color = color

    def _put_piece(self) -> None:
        self.piece_has -= 1

    def choice_place(self) -> tuple:
        while True:
            p_puts = input("{}({})の手番です([x y]で座標を指定してください。):".format(self.name, self.color.val))
            p_puts = p_puts.split()
            if p_puts[0] == 'q':
                exit()
            px = int(p_puts[0]) - 1
            py = int(p_puts[1]) - 1
            if self.board.is_already_put(px, py):
                print("その場所には既にコマが置かれています。")
                continue
            if (px < 0) or (px >= 8) or (py < 0) or (py >= 8):
                print("範囲外です。")
                continue
            if self.board.enable_put(px, py, self.color):
                print("挟める相手のコマがありません。")
                continue
            break
        self._put_piece()
        return px, py