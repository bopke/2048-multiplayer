# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMaximumSize(QtCore.QSize(300, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.singleplayer_button = QtWidgets.QPushButton(self.centralwidget)
        self.singleplayer_button.setGeometry(QtCore.QRect(202, 167, 90, 23))
        self.singleplayer_button.setObjectName("singleplayer_button")
        self.multiplayer_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiplayer_button.setGeometry(QtCore.QRect(105, 167, 90, 23))
        self.multiplayer_button.setObjectName("multiplayer_button")
        self.force_end_button = QtWidgets.QPushButton(self.centralwidget)
        self.force_end_button.setEnabled(False)
        self.force_end_button.setGeometry(QtCore.QRect(7, 167, 90, 23))
        self.force_end_button.setObjectName("force_end_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 26, 301, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.player_1_result = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_1_result.setFont(font)
        self.player_1_result.setObjectName("player_1_result")
        self.horizontalLayout_2.addWidget(self.player_1_result)
        self.player_2_result = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_2_result.setFont(font)
        self.player_2_result.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.player_2_result.setObjectName("player_2_result")
        self.horizontalLayout_2.addWidget(self.player_2_result)
        self.MatchResult = QtWidgets.QLabel(self.centralwidget)
        self.MatchResult.setGeometry(QtCore.QRect(0, 112, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MatchResult.setFont(font)
        self.MatchResult.setAlignment(QtCore.Qt.AlignCenter)
        self.MatchResult.setObjectName("label_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 51, 301, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 77, 301, 21))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.player_1_best_tile = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_1_best_tile.setFont(font)
        self.player_1_best_tile.setObjectName("player_1_best_tile")
        self.horizontalLayout_4.addWidget(self.player_1_best_tile)
        self.player_2_best_tile = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_2_best_tile.setFont(font)
        self.player_2_best_tile.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.player_2_best_tile.setObjectName("player_2_best_tile")
        self.horizontalLayout_4.addWidget(self.player_2_best_tile)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048 multiplayer"))
        self.singleplayer_button.setText(_translate("MainWindow", "single"))
        self.multiplayer_button.setText(_translate("MainWindow", "multi"))
        self.force_end_button.setText(_translate("MainWindow", "force end"))
        self.label_2.setText(_translate("MainWindow", "Player 1 result:"))
        self.label.setText(_translate("MainWindow", "Player 2 result:"))
        self.player_1_result.setText(_translate("MainWindow", "not played"))
        self.player_2_result.setText(_translate("MainWindow", "not played"))
        self.MatchResult.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Best tile:"))
        self.label_4.setText(_translate("MainWindow", "Best tile:"))
        self.player_1_best_tile.setText(_translate("MainWindow", "not played"))
        self.player_2_best_tile.setText(_translate("MainWindow", "not played"))
