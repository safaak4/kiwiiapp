import os
import sys
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QSizePolicy, QWidget, \
    QGridLayout
from PyQt5.QtCore import QSize, QPoint, Qt, QUrl
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

        #Lead Layout
        self.leadlayout = QGridLayout()
        self.mainlayout.addLayout(self.leadlayout, 0, 0, 0, 0)
        self.leadlayout.layout().setContentsMargins(0, 130, 0, 0)

        #WebView
        self.webWebWiew = QWebEngineView()
        self.leadlayout.addWidget(self.webWebWiew, 0, 0, 0, 1)
        self.webWebWiew.close()

        #Title Layout
        self.titlelayout = QGridLayout()
        #self.mainlayout.addLayout(self.titlelayout, 0, 0, 1, 1)
        self.mainlayout.addLayout(self.titlelayout, 0,0,0,0)
        self.titlelayout.setContentsMargins(0,0,0,0)
        self.titlelayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.titlelayout.sizeHint().setHeight(35)

        #Functions Layout (in Title Layout)
        self.functionslayout = QHBoxLayout()
        self.titlelayout.addLayout(self.functionslayout,1,0,0,0)
        self.functionslayout.setAlignment(Qt.AlignRight)
        self.functionslayout.setSpacing(0)

        #Top Navigation Layout
        self.topnavigation = QHBoxLayout()
        self.mainlayout.addLayout(self.topnavigation, 0,0,0,0, Qt.AlignTop)
        self.topnavigation.layout().setContentsMargins(0,40,0,0)

        #Top Navigation Bar
        self.buttonInstagram = QPushButton("Instagram")
        self.buttonFacebook = QPushButton("Facebook")
        self.buttonTwitter = QPushButton("Twitter")

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHeightForWidth(self.buttonInstagram.sizePolicy().hasHeightForWidth())

        self.buttonFont = QtGui.QFont("Uni Sans", 13)
        self.buttonFont.setItalic(True)
        self.buttonInstagram.setSizePolicy(sizePolicy3)
        self.buttonInstagram.setFixedSize(QSize(150, 90))
        self.buttonInstagram.setStyleSheet("QPushButton::!hover"
        "{"
        "color: #cccccc;"
        "}"
        "QPushButton::hover"
        "{"
        "color: white;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")
        self.buttonInstagram.setFont(self.buttonFont)
        self.buttonInstagram.setFlat(True)
        self.buttonInstagram.clicked.connect(self.btn_instagram_clicked)

        self.buttonFacebook.setSizePolicy(sizePolicy3)
        self.buttonFacebook.setFixedSize(QSize(150, 90))
        self.buttonFacebook.setStyleSheet("QPushButton::!hover"
        "{"
        "color: #cccccc;"
        "}"
        "QPushButton::hover"
        "{"
        "color: white;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")
        self.buttonFacebook.setFont(self.buttonFont)
        self.buttonFacebook.setFlat(True)
        self.buttonFacebook.clicked.connect(self.btn_facebook_clicked)

        self.buttonTwitter.setSizePolicy(sizePolicy3)
        self.buttonTwitter.setFixedSize(QSize(150, 90))
        self.buttonTwitter.setStyleSheet(
        "QPushButton::!hover"
        "{"
        "color: #cccccc;"
        "}"
        "QPushButton::hover"
        "{"
        "color: white;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}"
        )
        self.buttonTwitter.setFont(self.buttonFont)
        self.buttonTwitter.setFlat(True)
        self.buttonTwitter.clicked.connect(self.btn_twitter_clicked)

        self.topnavigation.addWidget(self.buttonInstagram, 0)
        self.topnavigation.addWidget(self.buttonFacebook, 1)
        self.topnavigation.addWidget(self.buttonTwitter, 2)

        #Title Bar
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

        #Path File
        scriptDir = os.path.dirname(os.path.realpath(__file__))

        # Minimize Button - Top Right
        self.btn_minimize = QPushButton()
        self.btn_minimize.clicked.connect(self.btn_min_clicked)
        self.functionslayout.addWidget(self.btn_minimize)
        self.btn_minimize.setFixedSize(60, 35)
        self.btn_minimize.setFlat(True)
        self.btn_minimize.setIcon(QtGui.QIcon(scriptDir + os.path.sep + "icons/minimizepng.png"))
        self.btn_minimize.setIconSize(QSize(14,14))
        self.btn_minimize.setStyleSheet("QPushButton::hover"
        "{"
        "background-color: #0d0063;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")

        # Maximize Button - Top Right
        self.btn_maximize = QPushButton()
        self.btn_maximize.clicked.connect(self.btn_max_clicked)
        self.functionslayout.addWidget(self.btn_maximize)
        self.btn_maximize.setFixedSize(60, 35)
        self.btn_maximize.setStyleSheet(
        "QPushButton::hover"
        "{"
        "background-color: #0d0063;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")
        self.btn_maximize.setFlat(True)
        self.btn_maximize.setIcon(QtGui.QIcon(scriptDir + os.path.sep + "icons/squarepng.png"))
        self.btn_maximize.setIconSize(QSize(14, 14))


        # Close Button - Top Right
        self.btn_close = QPushButton()
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.functionslayout.addWidget(self.btn_close)
        self.btn_close.setFixedSize(60, 35)
        self.btn_close.setFlat(True)
        self.btn_close.setIcon(QtGui.QIcon(scriptDir + os.path.sep + "icons/closepng.png"))
        self.btn_close.setIconSize(QSize(14, 14))
        self.btn_close.setStyleSheet("QPushButton::hover"
        "{"
        "background-color: #0d0063;"
        "border-bottom-width: 1px;"
        "border-radius: 0px;"
        "text-decoration: underline;"
        "}")

        window = QtWidgets.QWidget()
        window.setGeometry(QtCore.QRect(300, 300, 640, 480))
        sizegrip = QtWidgets.QSizeGrip(window)
        self.mainlayout.addWidget(sizegrip, 2, 0, 1, 0, Qt.AlignRight | Qt.AlignBottom)



    def webPageChange(self, pagex):
        if pagex == 0:
            self.webWebWiew.close()
            self.webWebWiew.load(QUrl("https://www.instagram.com/"))
            self.webWebWiew.show()

            print(self.webWebWiew.page().runJavaScript("#loginForm > div > div:nth-child(1) > div > label > input"))



        elif pagex == 1:
            self.webWebWiew.close()
            self.webWebWiew.load(QUrl("https://www.facebook.com/"))
            self.webWebWiew.show()

        else:
            self.webWebWiew.close()
            self.webWebWiew.load(QUrl("https://twitter.com/login"))
            self.webWebWiew.show()


    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.title.setFixedWidth(self.width())

    def mouseTitlePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseTitleMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
             self.move(self.pos() + event.globalPos() - self.dragPos)
             self.dragPos = event.globalPos()
             event.accept()

    def btn_instagram_clicked(self):
        self.buttonInstagram.setStyleSheet("QPushButton::!hover"
                                           "{"
                                           "color: #03c4a1;"
                                           "}"
                                           "QPushButton::hover"
                                           "{"
                                           "color: #13ebc3;"
                                           "border-bottom-width: 1px;"
                                           "border-radius: 0px;"
                                           "text-decoration: underline;"
                                           "}"
                                           )
        self.buttonFacebook.setStyleSheet("QPushButton::!hover"
                                          "{"
                                          "color: #cccccc;"
                                          "}"
                                          "QPushButton::hover"
                                          "{"
                                          "color: white;"
                                          "border-bottom-width: 1px;"
                                          "border-radius: 0px;"
                                          "text-decoration: underline;"
                                          "}")
        self.buttonTwitter.setStyleSheet("QPushButton::!hover"
                                          "{"
                                          "color: #cccccc;"
                                          "}"
                                          "QPushButton::hover"
                                          "{"
                                          "color: white;"
                                          "border-bottom-width: 1px;"
                                          "border-radius: 0px;"
                                          "text-decoration: underline;"
                                          "}")
        self.webPageChange(0)

    def btn_facebook_clicked(self):
        self.buttonFacebook.setStyleSheet("QPushButton::!hover"
                                           "{"
                                           "color: #03c4a1;"
                                           "}"
                                           "QPushButton::hover"
                                           "{"
                                           "color: #13ebc3;"
                                           "border-bottom-width: 1px;"
                                           "border-radius: 0px;"
                                           "text-decoration: underline;"
                                           "}")
        self.buttonTwitter.setStyleSheet("QPushButton::!hover"
                                          "{"
                                          "color: #cccccc;"
                                          "}"
                                          "QPushButton::hover"
                                          "{"
                                          "color: white;"
                                          "border-bottom-width: 1px;"
                                          "border-radius: 0px;"
                                          "text-decoration: underline;"
                                          "}")
        self.buttonInstagram.setStyleSheet("QPushButton::!hover"
                                           "{"
                                           "color: #cccccc;"
                                           "}"
                                           "QPushButton::hover"
                                           "{"
                                           "color: white;"
                                           "border-bottom-width: 1px;"
                                           "border-radius: 0px;"
                                           "text-decoration: underline;"
                                           "}")
        self.webPageChange(1)

    def btn_twitter_clicked(self):
        self.buttonTwitter.setStyleSheet("QPushButton::!hover"
                                           "{"
                                           "color: #03c4a1;"
                                           "}"
                                           "QPushButton::hover"
                                           "{"
                                           "color: #13ebc3;"
                                           "border-bottom-width: 1px;"
                                           "border-radius: 0px;"
                                           "text-decoration: underline;"
                                           "}")
        self.buttonFacebook.setStyleSheet("QPushButton::!hover"
                                          "{"
                                          "color: #cccccc;"
                                          "}"
                                          "QPushButton::hover"
                                          "{"
                                          "color: white;"
                                          "border-bottom-width: 1px;"
                                          "border-radius: 0px;"
                                          "text-decoration: underline;"
                                          "}")
        self.buttonInstagram.setStyleSheet("QPushButton::!hover"
                                          "{"
                                          "color: #cccccc;"
                                          "}"
                                          "QPushButton::hover"
                                          "{"
                                          "color: white;"
                                          "border-bottom-width: 1px;"
                                          "border-radius: 0px;"
                                          "text-decoration: underline;"
                                          "}")
        #self.webPageChange(2)
        self.webWebWiew.page().runJavaScript("document.querySelector('#loginForm > div > div:nth-child(1) > div > label > input[name=username]');", self.denemee)
         #   "console.log('denemee')")

    def denemee(self, value):
        print(str(value))

    def btn_close_clicked(self):
        self.close()

    def btn_max_clicked(self):
        if self.isMaximized():
            self.showNormal()
        else:
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