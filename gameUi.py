# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Game(object):
    def setupUi(self, MainWindow, object_name):
        self.object_name = object_name
        MainWindow.setObjectName("2048")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 423)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 623))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton20.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton20.sizePolicy().hasHeightForWidth())
        self.pushButton20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton20.setFont(font)
        self.pushButton20.setObjectName("pushButton20")
        self.gridLayout_2.addWidget(self.pushButton20, 2, 0, 1, 1)
        self.pushButton22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton22.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton22.sizePolicy().hasHeightForWidth())
        self.pushButton22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton22.setFont(font)
        self.pushButton22.setObjectName("pushButton22")
        self.gridLayout_2.addWidget(self.pushButton22, 2, 2, 1, 1)
        self.pushButton03 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton03.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton03.sizePolicy().hasHeightForWidth())
        self.pushButton03.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton03.setFont(font)
        self.pushButton03.setObjectName("pushButton03")
        self.gridLayout_2.addWidget(self.pushButton03, 0, 3, 1, 1)
        self.pushButton31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton31.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton31.sizePolicy().hasHeightForWidth())
        self.pushButton31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton31.setFont(font)
        self.pushButton31.setObjectName("pushButton31")
        self.gridLayout_2.addWidget(self.pushButton31, 3, 1, 1, 1)
        self.pushButton33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton33.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton33.sizePolicy().hasHeightForWidth())
        self.pushButton33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton33.setFont(font)
        self.pushButton33.setObjectName("pushButton33")
        self.gridLayout_2.addWidget(self.pushButton33, 3, 3, 1, 1)
        self.pushButton02 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton02.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton02.sizePolicy().hasHeightForWidth())
        self.pushButton02.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton02.setFont(font)
        self.pushButton02.setObjectName("pushButton02")
        self.gridLayout_2.addWidget(self.pushButton02, 0, 2, 1, 1)
        self.pushButton10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton10.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton10.sizePolicy().hasHeightForWidth())
        self.pushButton10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton10.setFont(font)
        self.pushButton10.setObjectName("pushButton10")
        self.gridLayout_2.addWidget(self.pushButton10, 1, 0, 1, 1)
        self.pushButton00 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton00.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton00.sizePolicy().hasHeightForWidth())
        self.pushButton00.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(183, 183, 183))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton00.setFont(font)
        self.pushButton00.setObjectName("pushButton00")
        self.gridLayout_2.addWidget(self.pushButton00, 0, 0, 1, 1)
        self.pushButton12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton12.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton12.sizePolicy().hasHeightForWidth())
        self.pushButton12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton12.setFont(font)
        self.pushButton12.setObjectName("pushButton12")
        self.gridLayout_2.addWidget(self.pushButton12, 1, 2, 1, 1)
        self.pushButton01 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton01.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton01.sizePolicy().hasHeightForWidth())
        self.pushButton01.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton01.setFont(font)
        self.pushButton01.setObjectName("pushButton01")
        self.gridLayout_2.addWidget(self.pushButton01, 0, 1, 1, 1)
        self.pushButton23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton23.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton23.sizePolicy().hasHeightForWidth())
        self.pushButton23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton23.setFont(font)
        self.pushButton23.setObjectName("pushButton23")
        self.gridLayout_2.addWidget(self.pushButton23, 2, 3, 1, 1)
        self.pushButton21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton21.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton21.sizePolicy().hasHeightForWidth())
        self.pushButton21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton21.setFont(font)
        self.pushButton21.setObjectName("pushButton21")
        self.gridLayout_2.addWidget(self.pushButton21, 2, 1, 1, 1)
        self.pushButton30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton30.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton30.sizePolicy().hasHeightForWidth())
        self.pushButton30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton30.setFont(font)
        self.pushButton30.setObjectName("pushButton30")
        self.gridLayout_2.addWidget(self.pushButton30, 3, 0, 1, 1)
        self.pushButton11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton11.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton11.sizePolicy().hasHeightForWidth())
        self.pushButton11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton11.setFont(font)
        self.pushButton11.setObjectName("pushButton11")
        self.gridLayout_2.addWidget(self.pushButton11, 1, 1, 1, 1)
        self.pushButton32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton32.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton32.sizePolicy().hasHeightForWidth())
        self.pushButton32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton32.setFont(font)
        self.pushButton32.setObjectName("pushButton32")
        self.gridLayout_2.addWidget(self.pushButton32, 3, 2, 1, 1)
        self.pushButton13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton13.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton13.sizePolicy().hasHeightForWidth())
        self.pushButton13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton13.setFont(font)
        self.pushButton13.setObjectName("pushButton13")
        self.gridLayout_2.addWidget(self.pushButton13, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuRuch = QtWidgets.QMenu(self.menuBar)
        self.menuRuch.setObjectName("menuRuch")
        self.menuOpcje = QtWidgets.QMenu(self.menuBar)
        self.menuOpcje.setObjectName("menuOpcje")
        MainWindow.setMenuBar(self.menuBar)
        self.actionUp = QtWidgets.QAction(MainWindow)
        self.actionUp.setObjectName("actionUp")
        self.actionDown = QtWidgets.QAction(MainWindow)
        self.actionDown.setObjectName("actionDown")
        self.actionLeft = QtWidgets.QAction(MainWindow)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(MainWindow)
        self.actionRight.setObjectName("actionRight")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionNewGame = QtWidgets.QAction(MainWindow)
        self.actionNewGame.setObjectName("actionNewGame")
        self.menuRuch.addAction(self.actionUp)
        self.menuRuch.addAction(self.actionDown)
        self.menuRuch.addAction(self.actionLeft)
        self.menuRuch.addAction(self.actionRight)
        self.menuOpcje.addAction(self.actionUndo)
        self.menuOpcje.addAction(self.actionNewGame)
        self.menuBar.addAction(self.menuRuch.menuAction())
        self.menuBar.addAction(self.menuOpcje.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.object_name))
        self.pushButton20.setText(_translate("MainWindow", "20"))
        self.pushButton22.setText(_translate("MainWindow", "22"))
        self.pushButton03.setText(_translate("MainWindow", "03"))
        self.pushButton31.setText(_translate("MainWindow", "31"))
        self.pushButton33.setText(_translate("MainWindow", "33"))
        self.pushButton02.setText(_translate("MainWindow", "02"))
        self.pushButton10.setText(_translate("MainWindow", "10"))
        self.pushButton00.setText(_translate("MainWindow", "00"))
        self.pushButton12.setText(_translate("MainWindow", "12"))
        self.pushButton01.setText(_translate("MainWindow", "01"))
        self.pushButton23.setText(_translate("MainWindow", "23"))
        self.pushButton21.setText(_translate("MainWindow", "21"))
        self.pushButton30.setText(_translate("MainWindow", "30"))
        self.pushButton11.setText(_translate("MainWindow", "11"))
        self.pushButton32.setText(_translate("MainWindow", "32"))
        self.pushButton13.setText(_translate("MainWindow", "13"))
        self.menuRuch.setTitle(_translate("MainWindow", "Move"))
        self.menuOpcje.setTitle(_translate("MainWindow", "Options"))
        self.actionUp.setText(_translate("MainWindow", "Up"))
        self.actionDown.setText(_translate("MainWindow", "Down"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionNewGame.setText(_translate("MainWindow", "Start again"))