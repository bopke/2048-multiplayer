from PyQt5 import QtCore, QtWidgets
import game
from mainWindowUi import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    def multiplayer_click(self):
        self.running_games = 2
        self.multiplayer = True
        self.ui.MatchResult.setText("")
        self.window1 = game.Game(self, 1)
        self.window2 = game.Game(self, 2)
        self.ui.player_1_best_tile.setText("still playing")
        self.ui.player_1_result.setText("still playing")
        self.ui.player_2_best_tile.setText("still playing")
        self.ui.player_2_result.setText("still playing")
        self.ui.multiplayer_button.setDisabled(True)
        self.ui.singleplayer_button.setDisabled(True)
        self.ui.force_end_button.setDisabled(False)

    def singleplayer_click(self):
        self.running_games = 1
        self.multiplayer = False
        self.ui.MatchResult.setText("")
        self.window1 = game.Game(self, 1)
        self.ui.player_1_best_tile.setText("still playing")
        self.ui.player_1_result.setText("still playing")
        self.ui.player_2_best_tile.setText("not playing")
        self.ui.player_2_result.setText("not playing")
        self.ui.multiplayer_button.setDisabled(True)
        self.ui.singleplayer_button.setDisabled(True)
        self.ui.force_end_button.setDisabled(False)

    def force_end_click(self):
        self.running_games = 0
        if self.multiplayer:
            self.ui.MatchResult.setText("Stopped")
        if self.window1 is not None:
            self.window1.close()
        if self.window2 is not None:
            self.window2.close()
        self.ui.multiplayer_button.setDisabled(False)
        self.ui.singleplayer_button.setDisabled(False)
        self.ui.force_end_button.setDisabled(True)

    def finish_game(self, player_number, score, best_tile_number):
        self.running_games -= 1
        if player_number == 1:
            self.results[0][0] = score
            self.results[0][1] = best_tile_number
            self.ui.player_1_best_tile.setText(str(best_tile_number))
            self.ui.player_1_result.setText(str(score))
            self.window1 = None
        elif player_number == 2:
            self.results[1][0] = score
            self.results[1][1] = best_tile_number
            self.ui.player_2_best_tile.setText(str(best_tile_number))
            self.ui.player_2_result.setText(str(score))
            self.window2 = None
        if str(score) == "CLOSED":
            self.multiplayer = False

        if self.running_games == 0:
            if self.multiplayer:
                if self.results[0][1] > self.results[1][1]:
                    self.ui.MatchResult.setText("Player 1 won")
                elif self.results[0][1] < self.results[1][1]:
                    self.ui.MatchResult.setText("Player 2 won")
                elif self.results[0][0] > self.results[1][0]:
                    self.ui.MatchResult.setText("Player 1 won")
                elif self.results[0][0] < self.results[1][0]:
                    self.ui.MatchResult.setText("Player 2 won")
                else:
                    self.ui.MatchResult.setText("Tie!")

            self.ui.multiplayer_button.setDisabled(False)
            self.ui.singleplayer_button.setDisabled(False)
            self.ui.force_end_button.setDisabled(True)

    def closeEvent(self, *args, **kwargs):
        if self.window1 is not None:
            self.window1.close()
        if self.window2 is not None:
            self.window2.close()

    def keyPressEvent(self, event) -> None:
        if self.window1 is not None:
            if event.key() == QtCore.Qt.Key_Up:
                self.window1.move_up()
            if event.key() == QtCore.Qt.Key_Down:
                self.window1.move_down()
            if event.key() == QtCore.Qt.Key_Left:
                self.window1.move_left()
            if event.key() == QtCore.Qt.Key_Right:
                self.window1.move_right()
        if self.window2 is not None:
            if event.key() == QtCore.Qt.Key_W:
                self.window2.move_up()
            if event.key() == QtCore.Qt.Key_S:
                self.window2.move_down()
            if event.key() == QtCore.Qt.Key_A:
                self.window2.move_left()
            if event.key() == QtCore.Qt.Key_D:
                self.window2.move_right()

    def __init__(self):
        super().__init__()
        self.window1 = None
        self.window2 = None
        self.results = [[0, 0], [0, 0]]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.multiplayer_button.clicked.connect(lambda: self.multiplayer_click())
        self.ui.singleplayer_button.clicked.connect(lambda: self.singleplayer_click())
        self.ui.force_end_button.clicked.connect(lambda: self.force_end_click())
        self.ui.MatchResult.setText("")
        self.show()
