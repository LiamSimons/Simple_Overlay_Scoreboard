import sys
import re

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton

from read import variables

# variables = [WIDTH, HEIGHT, "background.jpg"]
X = int(variables[0])
Y = int(variables[1])
WIDTH = int(variables[2])
HEIGHT = int(variables[3])
#BACKGROUND = variables[4]
FONT_SIZE = int(variables[5])
TITLE_1 = variables[6]
TITLE_2 = variables[7]

BOX_WIDTH = int(WIDTH/3)

# text boxes
# boxes = []
# scores = []
# letters = ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        # QtWidgets.QMainWindow.addDockWidget((400, 400), dockwidget)
        self.setGeometry(X, Y, WIDTH, HEIGHT)  # (xpos, ypos, width, height)
        self.setWindowTitle("SCOREBOARD")
        # self.setWindowOpacity(0.3)
        self.initUI()

    def initUI(self):
        # background = QImage(BACKGROUND)
        # scaled_background = background.scaled(QSize(WIDTH, HEIGHT))
        # palette = QPalette()
        # palette.setBrush(10, QBrush())
        # self.setPalette(palette)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.winning_b = QPushButton('', self)
        # self.winning_b.setGeometry(0, 0, 0, 0)
        # self.winning_b.setIcon(QIcon('medal.png'))

        # self.setStyleSheet("background:transparent;")

        # self.title_1 = QLabel(self)
        # self.title_2 = QLabel(self)
        #
        # self.title_1.setText(TITLE_1)
        # self.title_2.setText(TITLE_2)
        #
        # f1 = self.title_1.font()
        # f2 = self.title_2.font()
        #
        # f1.setPointSize(20)
        # f2.setPointSize(20)
        #
        # self.title_1.setFont(f1)
        # self.title_2.setFont(f2)
        #
        # self.title_1.move(int(WIDTH/4-self.title_1.width()/2), 0)
        # self.title_2.move(int(WIDTH*3/4-self.title_2.width()/2), 0)

        for i in range(3):
            textbox = QLineEdit(self)
            f = textbox.font()
            f.setPointSize(FONT_SIZE)
            textbox.setFont(f)
            textbox.setAlignment(QtCore.Qt.AlignCenter)
            textbox.move(BOX_WIDTH*i, 100)
            textbox.resize(BOX_WIDTH, 60)
            # boxes.append(textbox)
        for i in range(3):
            textbox = QLineEdit(self)
            f = textbox.font()
            f.setPointSize(FONT_SIZE)
            textbox.setFont(f)
            textbox.setAlignment(QtCore.Qt.AlignCenter)
            textbox.move(BOX_WIDTH*i, 160)
            textbox.resize(BOX_WIDTH, 60)
            # boxes.append(textbox)

    #     for box in boxes:
    #         box.textChanged.connect(self.change_winner)
    #
    # def change_winner(self):
    #     scores.clear()
    #     for box in range(3):
    #         score = boxes[box+3].text()
    #         # score = score.replace(' ', '')
    #         # for letter in letters:
    #         #     score = score.replace(letter, '')
    #         #     score = score.replace(letter.upper(), '')
    #         # scores.append(score)
    #         #print(int(score))
    #
    #     #print(max(scores))
    #     index = scores.index(max(scores))
    #     self.winning_b.setGeometry(BOX_WIDTH*index, 100, 30, 30)
    #     self.winning_b.show()
    #     #print(index)



app = QtWidgets.QApplication(sys.argv)
my_window = MyMainWindow()

#while True:
    #for box in boxes:
     #   print(box.text())
my_window.show()

app.exec_()

my_window.show()