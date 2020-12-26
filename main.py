import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QSizePolicy, QWidget, \
    QGridLayout
from PyQt5.QtCore import QSize, QPoint, Qt


class KiwiWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        # Title bar off
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.mainlayout = QVBoxLayout()

        self.setLayout(self.mainlayout)
        # self.setLayout(self.mainlayout)
        self.titlelayout = QVBoxLayout()
        self.titlelayout.addWidget(MyBar(self))
        self.mainlayout.addLayout(self.titlelayout)


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
        buttonInstagram.setStyleSheet("background-color: white")
        # buttonInstagram.setStyleSheet("background-image: ICON")

        buttonFacebook.setSizePolicy(sizePolicy3)
        buttonFacebook.setMinimumSize(QSize(100,100))
        buttonFacebook.setStyleSheet("background-color: white")

        buttonTwitter.setSizePolicy(sizePolicy3)
        buttonTwitter.setMinimumSize(QSize(100, 100))
        buttonTwitter.setStyleSheet("background-color: white")


        self.leftnavigation.addWidget(buttonInstagram)
        self.leftnavigation.addWidget(buttonFacebook, 1)
        self.leftnavigation.addWidget(buttonTwitter, 2)
        # self.setLayout(self.leftnavigation)
        # self.layout.addLayout(self.leftnavigation)
        # self.mainlayout.addLayout(self.leftnavigation)

        #self.nameLabel = QLabel(self)
        #self.nameLabel.setText('Link:')
        #self.nameLabel.setStyleSheet("color: white")
        #self.setStyleSheet("background-color: #121547")

        #self.setStyleSheet('QMainWindow{background-color: darkgray;border: 1px solid black;}')







        self.show()

class MyBar(QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,1000)
        self.title = QLabel("My Own Bar")

        btn_size = 35

        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("background-color: red;")

        self.btn_min = QPushButton("-")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet("background-color: gray;")

        self.btn_max = QPushButton("+")
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet("background-color: gray;")

        self.title.setFixedHeight(35)
        #self.title.setMaximumWidth()
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: blue;
            color: white;
        """)
        #self.title.setMaximumWidth()
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.end = QPoint(35, self.layout.geometry().width())
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()

app = QtWidgets.QApplication(sys.argv)
pencere = KiwiWindow()
pencere.setWindowTitle("Kiwi App")
pencere.setMaximumSize(1280,720)
#pencere.setFixedSize(500,720)
sys.exit(app.exec_())