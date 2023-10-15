from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow

class Sign_Up(object):
    def setupUi(self, MainWindow):

        MainWindow.setFixedSize(484, 483)
        MainWindow.setWindowTitle("Sign Up")
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)

        self.user_inpt = QtWidgets.QLineEdit(self.centralwidget)
        self.user_inpt.setGeometry(QtCore.QRect(230, 250, 171, 21))
        self.user_inpt.setInputMask("")
        self.user_inpt.setText("")
        self.user_inpt.setClearButtonEnabled(False)
        self.user_inpt.setObjectName("user_inpt")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(230, 290, 171, 22))
        self.email_input.setObjectName("email_input")
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(230, 330, 171, 22))
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.pass2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass2_input.setGeometry(QtCore.QRect(230, 370, 171, 22))
        self.pass2_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2_input.setObjectName("pass2_input")
        self.Sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.Sign_up.setGeometry(QtCore.QRect(340, 420, 101, 31))
        self.Sign_up.setObjectName("Sign_up")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(70, 250, 90, 16))
        self.user.setObjectName("user")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(70, 290, 55, 16))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(70, 330, 77, 16))
        self.password.setObjectName("password")
        self.password2 = QtWidgets.QLabel(self.centralwidget)
        self.password2.setGeometry(QtCore.QRect(70, 370, 141, 16))
        self.password2.setObjectName("password2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(arrow.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(70, 430, 400, 16))
        self.error.setStyleSheet("color:red;")
        self.error.setObjectName("error")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(180, 20, 161, 201))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("seo-and-web.png"))
        self.img.setObjectName("img")

        self.retranslateUi(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, Sign_Up):
        _translate = QtCore.QCoreApplication.translate
        Sign_Up.setWindowTitle(_translate("Sign_Up", "Form"))
        self.Sign_up.setText(_translate("Sign_Up", "Sign Up"))
        self.user.setText(_translate("Sign_Up", "User Name"))
        self.email.setText(_translate("Sign_Up", "Email"))
        self.password.setText(_translate("Sign_Up", "Password"))
        self.password2.setText(_translate("Sign_Up", "Re-enter Password"))
        self.error.setText(_translate("Sign_Up", "*"))
