import random
from PyQt5 import QtGui, QtWidgets
import gameUi


class Game(QtWidgets.QMainWindow):

    def color_button(self, button, value):
        if value == 0:
            button.setStyleSheet("background-color:#a3a3a3")
        if value == 2:
            button.setStyleSheet("background-color:#03cafc")
        if value == 4:
            button.setStyleSheet("background-color:#03fcdb")
        if value == 8:
            button.setStyleSheet("background-color:#3dfc03")
        if value == 16:
            button.setStyleSheet("background-color:#b5fc03")
        if value == 32:
            button.setStyleSheet("background-color:#f0fc03")
        if value == 64:
            button.setStyleSheet("background-color:#fcdf03")
        if value == 128:
            button.setStyleSheet("background-color:#fcc203")
        if value == 256:
            button.setStyleSheet("background-color:#fca103")
        if value == 512:
            button.setStyleSheet("background-color:#fc8003")
        if value == 1024:
            button.setStyleSheet("background-color:#fc5a03")
        if value == 2048:
            button.setStyleSheet("background-color:#fc0303")

    def paint_map(self):
        self.color_button(self.ui.pushButton00, self.map[0][0])
        if self.map[0][0] != 0:
            self.ui.pushButton00.setText(str(self.map[0][0]))
        else:
            self.ui.pushButton00.setText("")
        self.color_button(self.ui.pushButton01, self.map[0][1])
        if self.map[0][1] != 0:
            self.ui.pushButton01.setText(str(self.map[0][1]))
        else:
            self.ui.pushButton01.setText("")
        self.color_button(self.ui.pushButton02, self.map[0][2])
        if self.map[0][2] != 0:
            self.ui.pushButton02.setText(str(self.map[0][2]))
        else:
            self.ui.pushButton02.setText("")
        self.color_button(self.ui.pushButton03, self.map[0][3])
        if self.map[0][3] != 0:
            self.ui.pushButton03.setText(str(self.map[0][3]))
        else:
            self.ui.pushButton03.setText("")

        self.color_button(self.ui.pushButton10, self.map[1][0])
        if self.map[1][0] != 0:
            self.ui.pushButton10.setText(str(self.map[1][0]))
        else:
            self.ui.pushButton10.setText("")
        self.color_button(self.ui.pushButton11, self.map[1][1])
        if self.map[1][1] != 0:
            self.ui.pushButton11.setText(str(self.map[1][1]))
        else:
            self.ui.pushButton11.setText("")
        self.color_button(self.ui.pushButton12, self.map[1][2])
        if self.map[1][2] != 0:
            self.ui.pushButton12.setText(str(self.map[1][2]))
        else:
            self.ui.pushButton12.setText("")
        self.color_button(self.ui.pushButton13, self.map[1][3])
        if self.map[1][3] != 0:
            self.ui.pushButton13.setText(str(self.map[1][3]))
        else:
            self.ui.pushButton13.setText("")

        self.color_button(self.ui.pushButton20, self.map[2][0])
        if self.map[2][0] != 0:
            self.ui.pushButton20.setText(str(self.map[2][0]))
        else:
            self.ui.pushButton20.setText("")
        self.color_button(self.ui.pushButton21, self.map[2][1])
        if self.map[2][1] != 0:
            self.ui.pushButton21.setText(str(self.map[2][1]))
        else:
            self.ui.pushButton21.setText("")
        self.color_button(self.ui.pushButton22, self.map[2][2])
        if self.map[2][2] != 0:
            self.ui.pushButton22.setText(str(self.map[2][2]))
        else:
            self.ui.pushButton22.setText("")
        self.color_button(self.ui.pushButton23, self.map[2][3])
        if self.map[2][3] != 0:
            self.ui.pushButton23.setText(str(self.map[2][3]))
        else:
            self.ui.pushButton23.setText("")

        self.color_button(self.ui.pushButton30, self.map[3][0])
        if self.map[3][0] != 0:
            self.ui.pushButton30.setText(str(self.map[3][0]))
        else:
            self.ui.pushButton30.setText("")
        self.color_button(self.ui.pushButton31, self.map[3][1])
        if self.map[3][1] != 0:
            self.ui.pushButton31.setText(str(self.map[3][1]))
        else:
            self.ui.pushButton31.setText("")
        self.color_button(self.ui.pushButton32, self.map[3][2])
        if self.map[3][2] != 0:
            self.ui.pushButton32.setText(str(self.map[3][2]))
        else:
            self.ui.pushButton32.setText("")
        self.color_button(self.ui.pushButton33, self.map[3][3])
        if self.map[3][3] != 0:
            self.ui.pushButton33.setText(str(self.map[3][3]))
        else:
            self.ui.pushButton33.setText("")

    def place_new_tile(self):
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        while self.map[a][b] != 0:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
        self.map[a][b] = 2

    def check_win(self):
        for i in range(4):
            for j in range(4):
                if self.map[i][j] == 2048:
                    return True
        return False

    def check_free_space(self):
        for i in range(4):
            for j in range(4):
                if self.map[i][j] == 0:
                    return True
        return False

    def check_possible_movements(self):
        for i in range(3):
            for i in range(3):
                if self.map[i][i] == self.map[i + 1][i] or self.map[i][i + 1] == self.map[i][i]:
                    return True
        for i in range(3):
            if self.map[3][i] == self.map[3][i + 1]:
                return True
        for i in range(3):
            if self.map[i][3] == self.map[i + 1][3]:
                return True
        return False

    def check_game_over(self):
        if not self.check_free_space() and not self.check_possible_movements():
            return True
        return False

    def compress_left(self):
        new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        done = False
        for i in range(4):
            count = 0
            for j in range(4):
                if self.map[i][j] != 0:
                    new[i][count] = self.map[i][j]
                    if j != count:
                        done = True
                    count += 1
        self.map = new
        return done

    def merge(self):
        done = False
        for i in range(4):
            for j in range(3):
                if self.map[i][j] == self.map[i][j + 1] and self.map[i][j] != 0:
                    self.map[i][j] *= 2
                    self.map[i][j + 1] = 0
                    done = True
        return done

    def move_left(self):
        self.history.append(self.map.copy())
        done = self.compress_left()
        temp = self.merge()
        done = done or temp
        self.compress_left()
        if not done:
            self.undo()
            return
        self.next_frame()

    def move_right(self):
        self.history.append(self.map.copy())
        self.reverse()
        done = self.compress_left()
        temp = self.merge()
        done = done or temp
        self.compress_left()
        self.reverse()
        if not done:
            self.undo()
            return
        self.next_frame()

    def move_up(self):
        self.history.append(self.map.copy())
        self.transpose()
        done = self.compress_left()
        temp = self.merge()
        done = done or temp
        self.transpose()
        if not done:
            self.undo()
            return
        self.next_frame()

    def move_down(self):
        self.history.append(self.map.copy())
        self.transpose()
        self.reverse()
        done = self.compress_left()
        temp = self.merge()
        done = done or temp
        self.reverse()
        self.transpose()
        if not done:
            self.undo()
            return
        self.next_frame()

    def count_sum(self):
        sum = 0
        for i in range(4):
            for j in range(4):
                sum += self.map[i][j]
        return sum

    def best_tile(self):
        best_tile = 0
        for i in range(4):
            for j in range(4):
                if best_tile < self.map[i][j]:
                    best_tile = self.map[i][j]
        return best_tile

    def next_frame(self):
        if self.check_win():
            self.main_window.finish_game(self.player_number, self.count_sum(), self.best_tile())
            self.ending = True
            self.close()
        if self.check_game_over():
            self.main_window.finish_game(self.player_number, self.count_sum(), self.best_tile())
            self.ending = True
            self.close()
        self.place_new_tile()
        if self.check_game_over():
            self.main_window.finish_game(self.player_number, self.count_sum(), self.best_tile())
            self.ending = True
            self.close()
        self.paint_map()

    def undo(self):
        if len(self.history) > 1:
            self.map = self.history[-1].copy()
            self.history = self.history[:-1]
            self.paint_map()

    def new_game(self):
        self.map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.history = []
        self.next_frame()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        self.main_window.keyPressEvent(event)

    def transpose(self):
        new = []
        for i in range(4):
            new.append([])
            for j in range(4):
                new[i].append(self.map[j][i])
        self.map = new

    def reverse(self):
        new = []
        for i in range(4):
            new.append([])
            for j in range(4):
                new[i].append(self.map[i][3 - j])
        self.map = new

    def closeEvent(self, *args, **kwargs):
        if not self.ending:
            self.main_window.finish_game(self.player_number, "CLOSED", "CLOSED")

    def __init__(self, main_window, player_number):
        super().__init__()
        self.ending = False
        self.main_window = main_window
        self.player_number = player_number
        self.ui = gameUi.Ui_Game()
        self.ui.setupUi(self, "Player " + str(player_number))
        self.ui.actionNewGame.triggered.connect(lambda: self.new_game())
        self.ui.actionUndo.triggered.connect(lambda: self.undo())
        self.ui.actionUp.triggered.connect(lambda: self.move_up())
        self.ui.actionDown.triggered.connect(lambda: self.move_down())
        self.ui.actionLeft.triggered.connect(lambda: self.move_left())
        self.ui.actionRight.triggered.connect(lambda: self.move_right())
        self.show()
        self.new_game()
