from models.status import Status


class Piece:
    def __init__(self, x: int, y: int):
        self.state = Status.SPACE #初期状態では全ての目が"・"
        self.x = x
        self.y = y

    def __str__(self):
        return self.state

    def reverse_piece(self) -> None:  # 裏返す
        if self.state == Status.BLACK:
            self.state = Status.WHITE
        elif self.state == Status.WHITE:
            self.state = Status.BLACK
        else:
            raise ValueError(f"undefined Status: {self.state}")