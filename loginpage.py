import os
import pickle
import sys

import instabot


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QVBoxLayout, QCheckBox
from PyQt5.QtCore import QSize, QPoint, Qt, QUrl
from PyQt5.QtGui import *


class LoginPage(QtWidgets.QWidget):

    def __init__(self, leadlayout, buttonsettings, prm):
        super().__init__()

        if prm == 0:
            from instabot import bot
            LoginPage.bot = instabot.bot.Bot()

        LoginPage.myFont = QtGui.QFont("Uni Sans", 11)
        LoginPage.myFont.setItalic(False)
        LoginPage.myFontBold = QtGui.QFont("Uni Sans", 11)
        LoginPage.myFontBold.setItalic(True)
        LoginPage.myFontBold.setBold(True)

        LoginPage.buttonsettings = buttonsettings
        LoginPage.leadlayout = leadlayout
        # Login Layout
        LoginPage.loginlayout = QVBoxLayout()
        LoginPage.leadlayout.addLayout(self.loginlayout, 0, 0, 0, 0, Qt.AlignTop)
        LoginPage.loginlayout.setContentsMargins(0, 150, 0, 0)
        LoginPage.loginlayout.setSpacing(2)

        LoginPage.usernameText = QLabel("Username")
        LoginPage.loginlayout.addWidget(self.usernameText)
        LoginPage.usernameText.setStyleSheet("""color: #34495e; """)
        LoginPage.usernameText.setFont(QFont(self.myFontBold))

        LoginPage.usernameline = QLineEdit()
        LoginPage.loginlayout.addWidget(self.usernameline)
        # self.usernameline.setContentsMargins(0,100,0,0)
        LoginPage.usernameline.setFixedSize(300, 35)
        LoginPage.usernameline.setStyleSheet("""
                background-color: #16a085;
                color: white;
                border: none;
                font: 19px;
                border-radius: 10px;
                """)

        LoginPage.passwordText = QLabel("Password")
        LoginPage.loginlayout.addWidget(LoginPage.passwordText)
        LoginPage.passwordText.setStyleSheet("""color: #34495e; """)
        LoginPage.passwordText.setFont(QFont(LoginPage.myFontBold))

        LoginPage.passwordline = QLineEdit()
        LoginPage.loginlayout.addWidget(LoginPage.passwordline)
        # self.usernameline.setContentsMargins(0,100,0,0)
        LoginPage.passwordline.setFixedSize(300, 35)
        LoginPage.passwordline.setStyleSheet("""
                        background-color: #16a085;
                        color: white;
                        border: none;
                        font: 19px;
                        border-radius: 10px;
                        """)
        LoginPage.passwordline.setEchoMode(QLineEdit.Password)

        LoginPage.chckbox = QCheckBox("Remember Me")
        LoginPage.loginlayout.addWidget(LoginPage.chckbox)
        # self.chckbox.setStyleSheet("""QCheckBox::indicator {
        # border: 3px solid #5A5A5A;
        # background: none;
        # }""")

        LoginPage.loginButton = QPushButton("Login")
        LoginPage.loginButton.setFixedSize(300, 35)
        LoginPage.loginlayout.addWidget(LoginPage.loginButton)
        LoginPage.loginButton.setStyleSheet("""QPushButton::!hover
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
        LoginPage.loginButton.setFont(QFont(LoginPage.myFont))
        LoginPage.loginButton.clicked.connect(LoginPage.btn_login_clicked)

    def btn_login_clicked(self):
        #LoginPage.usernametextt = str(LoginPage.usernameline.text())

        try:
            LoginPage.lgn_widgets_close(self)
            #print(LoginPage.usernameline.text() + LoginPage.passwordline.text())
        except:
            print("hata 2")
        else:

            try:

                LoginPage.bot.login(username=LoginPage.usernameline.text(), password=LoginPage.passwordline.text())
                print("Login Trying")
            except:
                print("Username or Password is wrong!")
            else:
                print("Succesfully login")

                if LoginPage.chckbox.isChecked():
                    instagraminfodic = {"u": LoginPage.usernameline.text(), "p": LoginPage.passwordline.text()}
                    instagramfile = open("instagramdata.pkl", "wb")
                    pickle.dump(instagraminfodic, instagramfile)
                    instagramfile.close()
                    #instagramfile = open("instagramdata.pkl", "rb")
                    #output = pickle.load(instagramfile)
                    #print(output)


    def lgn_widgets_close(self):
        LoginPage.usernameline.hide()
        LoginPage.passwordline.hide()
        LoginPage.usernameText.hide()
        LoginPage.passwordText.hide()
        LoginPage.chckbox.hide()
        LoginPage.loginButton.hide()

