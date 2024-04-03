from models.status import Status

class Piece:

    def __init__(self, x, y):
        self.state = Status.SPACE #初期状態では全ての目が"・"
        self.x = x
        self.y = y

    def set_state(self, color: str):
        self.state: Status = Status.label_of(color)
        

    def reverse_piece(self):  # 裏返す
        if self.state == Status.BLACK:
            self.state = Status.WHITE
        elif self.state == Status.WHITE:
            self.state = Status.BLACK
        else:
            self.state = Status.SPACE

    def __str__(self):
        return self.state