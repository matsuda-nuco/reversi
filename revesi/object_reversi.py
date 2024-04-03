from models.board import Board
from models.player import Player
from models.cpu_player import CpuPlayer


class Game:
    def __init__(self):
        self.p1 = Player("Player1", "white")
        self.p2 = Player("Player2", "black")
        self.board = Board()

    def _finish_game(self):
        if self.board.BLACK_is_win() is not None:
            if self.board.BLACK_is_win():
                print("黒が勝ちです。")
            if not self.board.BLACK_is_win():
                print("白が勝ちです。")
        if self.board.BLACK_is_win() is None:
            print("引き分けです。")
        exit()  # これってメモリ解放してくれるん...?

    def turn(self, player):
        px, py = player.choice_place()
        self.board.set_piece_to(px, py, player.color)

    def play_game(self):
        self.board.set_piece_to(3, 3, "black")
        self.board.set_piece_to(4, 4, "black")
        self.board.set_piece_to(3, 4, "white")
        self.board.set_piece_to(4, 3, "white")
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