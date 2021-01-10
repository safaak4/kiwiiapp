import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QVBoxLayout, QCheckBox
from PyQt5.QtCore import QSize, QPoint, Qt, QUrl
from  PyQt5.QtGui import *
from instapy import InstaPy


class LoginPage():

    def __init__(self, leadlayout, buttonsettings):

        self.myFont = QtGui.QFont("Uni Sans", 11)
        self.myFont.setItalic(False)
        self.myFontBold = QtGui.QFont("Uni Sans", 11)
        self.myFontBold.setItalic(True)
        self.myFontBold.setBold(True)

        self.buttonsettings = buttonsettings
        self.leadlayout = leadlayout
        # Login Layout
        self.loginlayout = QVBoxLayout()
        self.leadlayout.addLayout(self.loginlayout, 0, 0, 0, 0, Qt.AlignTop)
        self.loginlayout.setContentsMargins(0,150,0,0)
        self.loginlayout.setSpacing(2)

        self.usernameText = QLabel("Username")
        self.loginlayout.addWidget(self.usernameText)
        self.usernameText.setStyleSheet("""color: #34495e; """)
        self.usernameText.setFont(QFont(self.myFontBold))


        self.usernameline = QLineEdit()
        self.loginlayout.addWidget(self.usernameline)
        # self.usernameline.setContentsMargins(0,100,0,0)
        self.usernameline.setFixedSize(300, 35)
        self.usernameline.setStyleSheet("""
                background-color: #16a085;
                color: white;
                border: none;
                font: 19px;
                border-radius: 10px;
                """)

        self.passwordText = QLabel("Password")
        self.loginlayout.addWidget(self.passwordText)
        self.passwordText.setStyleSheet("""color: #34495e; """)
        self.passwordText.setFont(QFont(self.myFontBold))

        self.passwordline = QLineEdit()
        self.loginlayout.addWidget(self.passwordline)
        # self.usernameline.setContentsMargins(0,100,0,0)
        self.passwordline.setFixedSize(300, 35)
        self.passwordline.setStyleSheet("""
                        background-color: #16a085;
                        color: white;
                        border: none;
                        font: 19px;
                        border-radius: 10px;
                        """)
        self.passwordline.setEchoMode(QLineEdit.Password)

        self.chckbox = QCheckBox("Remember Me")
        self.loginlayout.addWidget(self.chckbox)
        # self.chckbox.setStyleSheet("""QCheckBox::indicator {
        # border: 3px solid #5A5A5A;
        # background: none;
        # }""")

        self.loginButton = QPushButton("Login")
        self.loginButton.setFixedSize(300, 35)
        self.loginlayout.addWidget(self.loginButton)
        self.loginButton.setStyleSheet("""QPushButton::!hover
                                                  {
                                                  color: #ecf0f1;
                                                  background-color: #34495e;
                                                  border-radius: 10px;
                                                  }
                                                  QPushButton::hover
                                                  {
                                                  background-color: #2c3e50;
                                                  color: #ecf0f1;
                                                  border-bottom-width: 1px;
                                                  border-radius: 10px;
                                                  text-decoration: underline;
                                                  }""")
        self.loginButton.setFont(QFont(self.myFont))
        self.loginButton.clicked.connect(self.btn_login_clicked)

    def btn_login_clicked(self):
        print("bloga girdik")
        try:
            InstaPy(username=self.usernameline.text(),
                    password=self.passwordline.text())
            print("??")
        except:
            print("hata")
        else:
            print("devamke")

