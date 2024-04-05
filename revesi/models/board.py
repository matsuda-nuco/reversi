from models.status import Status
from models.piece import Piece


class Board:
    pieces = [["" for i in range(8)] for j in range(8)]

    def __init__(self):
        self.last_puted_rocation = [0, 0]  # x, y
        self.last_puted_color = None
        self.last_puted_piece_copy = None
        #盤面の生成(Piece64個)
        for x in range(0, 8):
            for y in range(0, 8):
                self.pieces[y][x] = Piece(x, y)

    def __str__(self):
        stage = ""
        for y in range(0, 8):
            for x in range(0, 8):
                stage += self.pieces[y][x].state.val
            stage += "\n"
        return stage

    def __add__(self, another):
        return self.__str__() + another

    def is_already_put(self, x: int, y: int) -> bool:
        ##print(type(self))
        return self.pieces[y][x].state != Status.SPACE

    def set_piece_to(self, x: int, y: int, color: Status) -> None:  # pieceを置くときに呼ぶ
        self.pieces[y][x].state = color
        self.last_puted_rocation[0] = x
        self.last_puted_rocation[1] = y
        self.last_puted_color = color

    def _count_black_area(self) -> int:
        area = 0
        for y in self.pieces:
            for x in y:
                if x.state == Status.BLACK:
                    area += 1
        return area

    def _count_white_area(self) -> int:
        area = 0
        for y in self.pieces:
            for x in y:
                if x.state == Status.WHITE:
                    area += 1
        return area

    def black_is_win(self) -> bool:
        if self._count_black_area() > self._count_white_area():
            return True
        if self._count_black_area() < self._count_white_area():
            return False
        return None  # Noneを返せば引き分け

    def update(self) -> None:  # boad上のpiece色を演算し、更新
        x_offset = self.last_puted_rocation[0]
        y_offset = self.last_puted_rocation[1]
        ########################################
        # 行
        ########################################
        # コマを置いた左側
        target_x_left = x_offset
        for x_left in range(x_offset - 1, -1, -1):
            if self.pieces[y_offset][x_left].state != self.last_puted_color and self.is_already_put(x_left, y_offset): #違う色なら
                continue
            if (self.pieces[y_offset][x_left].state == self.last_puted_color) and (x_left is not x_offset):
                target_x_left = x_left
                break
            else:
                break

        # コマを置いた右側
        target_x_right = x_offset
        for x_right in range(x_offset + 1, 8):
            if self.pieces[y_offset][x_right].state != self.last_puted_color and self.is_already_put(x_right, y_offset):
                continue
            if (self.pieces[y_offset][x_right].state == self.last_puted_color) and (x_right is not x_offset):
                target_x_right = x_right
                break
            else:
                break

        # 書き換え
        for x in range(x_offset - 1, target_x_left, -1):
            self.pieces[y_offset][x].reverse_piece()

        for x in range(x_offset + 1, target_x_right):
            self.pieces[y_offset][x].reverse_piece()

        ########################################
        # 列
        ########################################
        # コマを置いた上側
        target_y_upper = y_offset
        for y_upper in range(y_offset - 1, -1, -1):
            if self.pieces[y_upper][x_offset].state != self.last_puted_color and self.is_already_put(x_offset, y_upper):
                continue
            if (self.pieces[y_upper][x_offset].state == self.last_puted_color) and (y_upper is not y_offset):
                target_y_upper = y_upper
                break
            else:
                break

        # コマを置いた下側
        target_y_lower = y_offset
        for y_lower in range(y_offset + 1, 8):
            if self.pieces[y_lower][x_offset].state != self.last_puted_color and self.is_already_put(x_offset, y_lower):
                continue
            if (self.pieces[y_lower][x_offset].state == self.last_puted_color) and (y_lower is not y_offset):
                target_y_lower = y_lower
                break
            else:
                break

        # 書き換え
        for y in range(y_offset - 1, target_y_upper, -1):
            self.pieces[y][x_offset].reverse_piece()

        for y in range(y_offset + 1, target_y_lower):
            self.pieces[y][x_offset].reverse_piece()

        ########################################
        # 右上がり斜め
        ########################################
        # コマを置いた左下側
        target_x_left = x_offset
        target_y_lower = y_offset
        for i in range(1, 8):
            x_left = x_offset - i
            y_lower = y_offset + i
            if x_left < 0 or y_lower > 7: #壁にぶつかったら
                break
            if self.pieces[y_lower][x_left].state != self.last_puted_color and self.is_already_put(x_left,y_lower):  # 違う色なら
                continue
            if (self.pieces[y_lower][x_left].state == self.last_puted_color) and (x_left is not x_offset) and (y_lower is not y_offset):
                target_x_left = x_left
                target_y_lower = y_lower
                break
            else:
                break

        # コマを置いた右上側
        target_x_right = x_offset
        target_y_upper = y_offset
        for i in range(1, 8):
            x_right = x_offset + i
            y_upper = y_offset - i
            if x_right > 7 or y_upper < 0:  # 壁にぶつかったら
                break
            if self.pieces[y_upper][x_right].state != self.last_puted_color and self.is_already_put(x_right,y_upper):
                continue
            if (self.pieces[y_upper][x_right].state == self.last_puted_color) and (x_right is not x_offset) and (y_upper is not y_offset):
                target_x_right = x_right
                target_y_upper = y_upper
                break
            else:
                break

        # 書き換え
        for i in range(1, abs(target_x_left - x_offset)):
            x = x_offset - i
            y = y_offset + i
            self.pieces[y][x].reverse_piece()

        for i in range(1, abs(target_x_right - x_offset)):
            x = x_offset + i
            y = y_offset - i
            self.pieces[y][x].reverse_piece()

        ########################################
        # 右下がり斜め
        ########################################
        # コマを置いた左上側
        target_x_left = x_offset
        target_y_upper = y_offset
        for i in range(1, 8):
            x_left = x_offset - i
            y_upper = y_offset - i
            if x_left < 0 or y_upper < 0: #壁にぶつかったら
                break
            if self.pieces[y_upper][x_left].state != self.last_puted_color and self.is_already_put(x_left,y_upper):  # 違う色なら
                continue
            if (self.pieces[y_upper][x_left].state == self.last_puted_color) and (x_left is not x_offset) and (y_upper is not y_offset):
                target_x_left = x_left
                target_y_upper = y_upper
                break
            else:
                break

        # コマを置いた右上側
        target_x_right = x_offset
        target_y_lower = y_offset
        for i in range(1, 8):
            x_right = x_offset + i
            y_lower = y_offset + i
            if x_right > 7 or y_lower > 7:  # 壁にぶつかったら
                break
            if self.pieces[y_lower][x_right].state != self.last_puted_color and self.is_already_put(x_right,y_lower):
                continue
            if (self.pieces[y_lower][x_right].state == self.last_puted_color) and (x_right is not x_offset) and (y_lower is not y_offset):
                target_x_right = x_right
                target_y_lower = y_lower
                break
            else:
                break

        # 書き換え
        for i in range(1, abs(target_x_left - x_offset)):
            x = x_offset - i
            y = y_offset - i
            self.pieces[y][x].reverse_piece()

        for i in range(1, abs(target_x_right - x_offset)):
            x = x_offset + i
            y = y_offset + i
            self.pieces[y][x].reverse_piece()

    def enable_put(self, x: int, y: int, color: str) -> bool:  # boad上のpieceの色のチェック
        x_offset = x
        y_offset = y
        flag = False
        ########################################
        # 行
        ########################################
        # コマを置いた左側
        for x_left in range(x_offset - 1, -1, -1):
            if self.pieces[y_offset][x_left].state == Status.SPACE:
                break
            if self.pieces[y_offset][x_left].state != color and self.is_already_put(x_left, y_offset): #違う色なら
                flag = True
                continue
            if (self.pieces[y_offset][x_left].state == color) and flag == True:
                return False

        # コマを置いた右側
        for x_right in range(x_offset + 1, 8):
            if self.pieces[y_offset][x_right].state == Status.SPACE:
                break
            if self.pieces[y_offset][x_right].state != color and self.is_already_put(x_right, y_offset):
                flag = True
                continue
            if (self.pieces[y_offset][x_right].state == color) and flag == True:
                return False

        ########################################
        # 列
        ########################################
        # コマを置いた上側
        for y_upper in range(y_offset - 1, -1, -1):
            if self.pieces[y_upper][x_offset].state == Status.SPACE:
                break
            if self.pieces[y_upper][x_offset].state != color and self.is_already_put(x_offset, y_upper):
                flag = True
                continue
            if (self.pieces[y_upper][x_offset].state == color) and flag == True:
                return False

        # コマを置いた下側
        for y_lower in range(y_offset + 1, 8):
            if self.pieces[y_lower][x_offset].state == Status.SPACE:
                break
            if self.pieces[y_lower][x_offset].state != color and self.is_already_put(x_offset, y_lower):
                flag = True
                continue
            if (self.pieces[y_lower][x_offset].state == color) and flag == True:
                return False

        ########################################
        # 右上がり斜め
        ########################################
        # コマを置いた左下側
        for i in range(1, 8):
            x_left = x_offset - i
            y_lower = y_offset + i
            if x_left < 0 or y_lower > 7: #壁にぶつかったら
                break
            if self.pieces[y_lower][x_left].state == Status.SPACE:
                break
            if self.pieces[y_lower][x_left].state != color and self.is_already_put(x_left,y_lower):  # 違う色なら
                flag = True
                continue
            if (self.pieces[y_lower][x_left].state == color) and flag == True:
                return False

        # コマを置いた右上側
        for i in range(1, 8):
            x_right = x_offset + i
            y_upper = y_offset - i
            if x_right > 7 or y_upper < 0:  # 壁にぶつかったら
                break
            if self.pieces[y_upper][x_right].state == Status.SPACE:
                break
            if self.pieces[y_upper][x_right].state != color and self.is_already_put(x_right,y_upper):
                flag = True
                continue
            if (self.pieces[y_upper][x_right].state == color) and flag == True:
                return False

        ########################################
        # 右下がり斜め
        ########################################
        # コマを置いた左上側
        for i in range(1, 8):
            x_left = x_offset - i
            y_upper = y_offset - i
            if x_left < 0 or y_upper < 0: #壁にぶつかったら
                break
            if self.pieces[y_upper][x_left].state == Status.SPACE:
                break
            if self.pieces[y_upper][x_left].state != color and self.is_already_put(x_left,y_upper):  # 違う色なら
                flag == True
                continue
            if (self.pieces[y_upper][x_left].state == color) and flag == True:
                return False

        # コマを置いた右下側
        for i in range(1, 8):
            x_right = x_offset + i
            y_lower = y_offset + i
            if x_right > 7 or y_lower > 7:  # 壁にぶつかったら
                break
            if self.pieces[y_lower][x_right].state == Status.SPACE:
                break
            if self.pieces[y_lower][x_right].state != color and self.is_already_put(x_right,y_lower):
                flag = True
                continue
            if (self.pieces[y_lower][x_right].state == color) and flag == True:
                return False
        return True