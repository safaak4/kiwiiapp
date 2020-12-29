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

        self.show()

    def init_ui(self):
        # Title bar off
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #Main Layout
        self.mainlayout = QGridLayout()
        self.setLayout(self.mainlayout)
        self.mainlayout.setContentsMargins(0,0,0,0)

        #Title Layout
        self.titlelayout = QGridLayout()
        #self.mainlayout.addLayout(self.titlelayout, 0, 0, 1, 1)
        self.mainlayout.addLayout(self.titlelayout, 0,0,0,0)
        self.titlelayout.setContentsMargins(0,0,0,0)
        self.titlelayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.titlelayout.sizeHint().setHeight(35)

        #Functions Layout
        self.functionslayout = QHBoxLayout()
        self.titlelayout.addLayout(self.functionslayout,1,0,0,0)
        self.functionslayout.setAlignment(Qt.AlignRight)
        self.functionslayout.setSpacing(0)

        #Left Navigation Layout
        self.topnavigation = QHBoxLayout(self)
        self.mainlayout.addLayout(self.topnavigation, 0,0,0,0, Qt.AlignTop)
        self.topnavigation.layout().setContentsMargins(0,40,0,0)

        #Left Navigation Bar
        buttonInstagram = QPushButton("Instagram")
        buttonFacebook = QPushButton("Facebook")
        buttonTwitter = QPushButton("Twitter")

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHeightForWidth(buttonInstagram.sizePolicy().hasHeightForWidth())

        self.buttonFont = QtGui.QFont("Uni Sans", 13)
        self.buttonFont.setItalic(True)
        buttonInstagram.setSizePolicy(sizePolicy3)
        buttonInstagram.setFixedSize(QSize(150, 90))
        buttonInstagram.setStyleSheet("QPushButton::!hover"
        "{"
        "color: #acb4b5;"
        "}"
        "QPushButton::hover"
        "{"
        "color: white;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")
        buttonInstagram.setFont(self.buttonFont)
        buttonInstagram.setFlat(True)

        buttonFacebook.setSizePolicy(sizePolicy3)
        buttonFacebook.setFixedSize(QSize(150, 90))
        buttonFacebook.setStyleSheet("QPushButton::!hover"
        "{"
        "color: #acb4b5;"
        "}"
        "QPushButton::hover"
        "{"
        "color: white;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")
        buttonFacebook.setFont(self.buttonFont)
        buttonFacebook.setFlat(True)

        buttonTwitter.setSizePolicy(sizePolicy3)
        buttonTwitter.setFixedSize(QSize(150, 90))
        buttonTwitter.setStyleSheet(
        "QPushButton::!hover"
        "{"
        "color: #acb4b5;"
        "}"
        "QPushButton::hover"
        "{"
        "color: white;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}"
        )
        buttonTwitter.setFont(self.buttonFont)
        buttonTwitter.setFlat(True)

        self.topnavigation.addWidget(buttonInstagram, 0)
        self.topnavigation.addWidget(buttonFacebook, 1)
        self.topnavigation.addWidget(buttonTwitter, 2)

        self.myFont = QtGui.QFont("Uni Sans", 12)
        self.myFont.setItalic(True)
        self.title = QLabel("Kiwii App nnn")
        self.title.setFont(self.myFont)
        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignLeft)
        self.titlelayout.addWidget(self.title, 3, 0, 0, 0)
        self.title.setStyleSheet("""
                            background-color: #150485;
                            color: white;
                            padding-top: 5px;
                            padding-left: 5px;
                        """)
        self.title.setFixedWidth(self.width())
        # self.title.resize(self.width(), 35)
        # self.title.setSizePolicy(QSizePolicy.Expanding, 35)
        self.title.setMouseTracking(True)
        self.title.mousePressEvent = self.mouseTitlePressEvent
        self.title.mouseMoveEvent = self.mouseTitleMoveEvent

        # Minimize Button - Top Right
        self.btn_minimize = QPushButton("+")
        self.btn_minimize.clicked.connect(self.btn_min_clicked)
        self.functionslayout.addWidget(self.btn_minimize)
        self.btn_minimize.setFixedSize(60, 35)
        self.btn_minimize.setFlat(True)

        # Maximize Button - Top Right
        self.btn_maximize = QPushButton("-")
        self.btn_maximize.clicked.connect(self.btn_max_clicked)
        self.functionslayout.addWidget(self.btn_maximize)
        self.btn_maximize.setFixedSize(60, 35)
        self.btn_maximize.setFlat(True)

        # Close Button - Top Right
        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.functionslayout.addWidget(self.btn_close)
        self.btn_close.setFixedSize(60, 35)
        self.btn_close.setFlat(True)

        window = QtWidgets.QWidget()
        window.setGeometry(QtCore.QRect(300, 300, 640, 480))
        sizegrip = QtWidgets.QSizeGrip(window)
        self.mainlayout.addWidget(sizegrip, 2, 0, 1, 0, Qt.AlignRight | Qt.AlignBottom)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        #self.title.setFixedWidth(self.width()-180)
        self.title.setFixedWidth(self.width())


    def mouseTitlePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseTitleMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
             self.move(self.pos() + event.globalPos() - self.dragPos)
             self.dragPos = event.globalPos()
             event.accept()

    def btn_close_clicked(self):
        self.close()

    def btn_max_clicked(self):
        self.showMaximized()

    def btn_min_clicked(self):
        self.showMinimized()



app = QtWidgets.QApplication(sys.argv)
pencere = KiwiWindow()
pencere.setWindowTitle("Kiwi App")
pencere.setStyleSheet("background-color: #080136")
#pencere.setMaximumSize(1280,720)
pencere.setMinimumSize(1280,720)
#pencere.setFixedSize(1280, 720)
sys.exit(app.exec_())