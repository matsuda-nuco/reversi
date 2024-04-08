from models.status import Status
from models.board import Board
from models.player import Player
from models.cpu_player import CpuPlayer


def choice_player() -> Player | CpuPlayer:
    while True:
        choice = input("playerと対戦する場合は1,cpuと対戦する場合は2を入力してください。:")
        if choice == "1":
            return Player("Player2", Status.BLACK)
        elif choice == "2":
            return CpuPlayer("Cpu", Status.BLACK)
        else:
            print("入力が不正です。")


class Game:
    def __init__(self):
        self.p1 = Player("Player1", Status.WHITE)
        self.p2 = choice_player()
        self.board = Board()


    def _finish_game(self) -> None:
        if self.board.black_is_win() is not None:
            if self.board.black_is_win():
                print("黒が勝ちです。")
            if not self.board.black_is_win():
                print("白が勝ちです。")
        if self.board.black_is_win() is None:
            print("引き分けです。")
        exit()

    def turn(self, player:str) -> None:
        px, py = player.choice_place()
        self.board.set_piece_to(px, py, player.color)

    def play_game(self) -> None:
        self.board.set_piece_to(3, 3, Status.BLACK)
        self.board.set_piece_to(4, 4, Status.BLACK)
        self.board.set_piece_to(3, 4, Status.WHITE)
        self.board.set_piece_to(4, 3, Status.WHITE)
        # print(id(self.board.board))
        print(self.board + "\nゲームスタート!\n(qでゲームを中断して終了します)")

        while (self.p1.piece_has != 0) and (self.p2.piece_has != 0):
            self.turn(self.p1)
            self.board.update()
            print(self.board)

            self.turn(self.p2)
            self.board.update()
            print(self.board)

        self._finish_game()


if __name__ == "__main__":
    g = Game()
    g.play_game()