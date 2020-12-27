import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QSizePolicy, QWidget, \
    QGridLayout
from PyQt5.QtCore import QSize, QPoint, Qt
from  PyQt5.QtGui import *


class KiwiWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Left Navigation Bar
        buttonInstagram = QPushButton("Instagram")
        buttonFacebook = QPushButton("Facebook")
        buttonTwitter = QPushButton("Twitter")

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHeightForWidth(buttonInstagram.sizePolicy().hasHeightForWidth())

        buttonInstagram.setSizePolicy(sizePolicy3)
        buttonInstagram.setFixedSize(QSize(100, 100))
        buttonInstagram.setStyleSheet("background-color: white")
        # buttonInstagram.setStyleSheet("background-image: ICON")

        buttonFacebook.setSizePolicy(sizePolicy3)
        buttonFacebook.setFixedSize(QSize(100, 100))
        buttonFacebook.setStyleSheet("background-color: white")

        buttonTwitter.setSizePolicy(sizePolicy3)
        buttonTwitter.setFixedSize(QSize(100, 100))
        buttonTwitter.setStyleSheet("background-color: white")

        self.leftnavigation.addWidget(buttonInstagram, 0)
        self.leftnavigation.addWidget(buttonFacebook, 1)
        self.leftnavigation.addWidget(buttonTwitter, 2)


        #Minimize Button - Top Right
        self.btn_minimize = QPushButton("+")
        self.btn_minimize.clicked.connect(self.btn_min_clicked)
        self.titlelayout.addWidget(self.btn_minimize)
        self.btn_minimize.setFixedSize(60,40)

        #Maximize Button - Top Right
        self.btn_maximize = QPushButton("-")
        self.btn_maximize.clicked.connect(self.btn_max_clicked)
        self.titlelayout.addWidget(self.btn_maximize)
        self.btn_maximize.setFixedSize(60,40)

        #Close Button - Top Right
        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.titlelayout.addWidget(self.btn_close)
        self.btn_close.setFixedSize(60,40)


        self.show()

    def init_ui(self):
        # Title bar off
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #Main Layout
        self.mainlayout = QGridLayout(self)
        self.setLayout(self.mainlayout)
        self.mainlayout.setContentsMargins(0,0,0,0)

        #Title Layout
        self.titlelayout = QHBoxLayout()
        self.mainlayout.addLayout(self.titlelayout, 0, 2, 0, 1)
        self.titlelayout.setAlignment(Qt.AlignTop)
        self.titlelayout.setSpacing(0)


        #Left Navigation Layout
        self.leftnavigation = QVBoxLayout(self)
        self.mainlayout.addLayout(self.leftnavigation, 1,0,1,3)

    def resizeEvent(self, QResizeEvent):
        super(self.titlelayout, self).resizeEvent(QResizeEvent)
        self.titlelayout.setFixedWidth(self.parent.width())


    def btn_close_clicked(self):
        self.close()

    def btn_max_clicked(self):
        self.showMaximized()

    def btn_min_clicked(self):
        self.showMinimized()


app = QtWidgets.QApplication(sys.argv)
pencere = KiwiWindow()
pencere.setWindowTitle("Kiwi App")
#pencere.setMaximumSize(1280,720)
#pencere.setFixedSize(1,720)
sys.exit(app.exec_())