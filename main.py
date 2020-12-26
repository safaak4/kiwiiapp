import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QSizePolicy
from PyQt5.QtCore import QSize


class KiwiWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.leftnavigation = QVBoxLayout(self)
        self.leftnavigation.setContentsMargins( 0, 0, 1180, 0)
        buttonInstagram = QPushButton("Instagram")
        buttonFacebook = QPushButton("Facebook")
        buttonTwitter = QPushButton("Twitter")

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(buttonInstagram.sizePolicy().hasHeightForWidth())

        buttonInstagram.setSizePolicy(sizePolicy3)
        buttonInstagram.setMinimumSize(QSize(100, 100))

        buttonFacebook.setSizePolicy(sizePolicy3)
        buttonFacebook.setMinimumSize(QSize(100,100))

        buttonTwitter.setSizePolicy(sizePolicy3)
        buttonTwitter.setMinimumSize(QSize(100, 100))

        self.leftnavigation.addWidget(buttonInstagram)
        self.leftnavigation.addWidget(buttonFacebook, 1)
        self.leftnavigation.addWidget(buttonTwitter, 2)
        self.setLayout(self.leftnavigation)

        #self.nameLabel = QLabel(self)
        #self.nameLabel.setText('Link:')
        #self.nameLabel.setStyleSheet("color: white")
        #self.setStyleSheet("background-color: #121547")

        self.show()


app = QtWidgets.QApplication(sys.argv)
pencere = KiwiWindow()
pencere.setWindowTitle("Kiwi App")
pencere.setFixedSize(1280,720)
sys.exit(app.exec_())