from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
import sqlite3
from User import User

class Sign_In(object):
    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(483, 479)
        MainWindow.setWindowTitle("Sign In")
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)

        self.centralwidget = QWidget(MainWindow)
        
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(160, 40, 191, 191))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("login.png"))
        self.img.setObjectName("img")
        self.Guest = QtWidgets.QPushButton(self.centralwidget)
        self.Guest.setGeometry(QtCore.QRect(290, 410, 93, 28))
        self.Guest.setStyleSheet("background-color: transparent;\n"
"text-decoration: underline;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"\n"
"")
        self.Guest.setObjectName("Guest")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(80, 250, 95, 20))
        self.user.setObjectName("user")

        self.log_in = QtWidgets.QPushButton(self.centralwidget)
        self.log_in.setGeometry(QtCore.QRect(310, 360, 111, 31))
        self.log_in.setObjectName("log_in")
        

        self.Sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.Sign_up.setGeometry(QtCore.QRect(350, 410, 93, 28))
        self.Sign_up.setStyleSheet("background-color: transparent;\n"
"text-decoration: underline;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"\n"
"")
        self.Sign_up.setObjectName("Sign_up")
        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(190, 250, 143, 22))
        self.user_input.setText("")
        self.user_input.setObjectName("user_input")
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(190, 290, 143, 22))
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 290, 81, 20))
        self.password.setObjectName("password")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(80, 370, 400, 16))
        self.error.setStyleSheet("color:red;")
        self.error.setObjectName("error")

        self.retranslateUi(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Sign_In):
        _translate = QtCore.QCoreApplication.translate
        Sign_In.setWindowTitle(_translate("Sign_In", "Sign_In"))
        self.img.setWhatsThis(_translate("Sign_In", "<html><head/><body><p><br/></p></body></html>"))
        self.Guest.setText(_translate("Sign_In", "Guest"))
        self.user.setText(_translate("Sign_In", "User Name"))
        self.log_in.setText(_translate("Sign_In", "Log In"))
        self.Sign_up.setText(_translate("Sign_In", "Sign Up"))
        self.password.setText(_translate("Sign_In", "Password"))
        self.error.setText(_translate("Sign_In", "*"))
    

