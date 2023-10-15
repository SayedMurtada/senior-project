
from PyQt5 import QtCore, QtGui, QtWidgets
from DataBase import DataBase
from User import User

class Add_Host(object):
    def setupUi(self, error_2):
        error_2.setObjectName("error_2")
        error_2.resize(509, 409)
        self.name_in = QtWidgets.QLineEdit(error_2)
        self.name_in.setGeometry(QtCore.QRect(270, 120, 161, 22))
        self.name_in.setObjectName("name_in")
        self.Name = QtWidgets.QLabel(error_2)
        self.Name.setGeometry(QtCore.QRect(80, 120, 111, 20))
        self.Name.setObjectName("Name")
        self.user = QtWidgets.QLabel(error_2)
        self.user.setGeometry(QtCore.QRect(80, 220, 111, 20))
        self.user.setObjectName("user")

        self.password = QtWidgets.QLabel(error_2)
        self.password.setGeometry(QtCore.QRect(80, 270, 121, 16))
        self.password.setObjectName("pass")

        self.url = QtWidgets.QLabel(error_2)
        self.url.setGeometry(QtCore.QRect(80, 170, 121, 16))
        self.url.setObjectName("url")
        self.url_in = QtWidgets.QLineEdit(error_2)
        self.url_in.setGeometry(QtCore.QRect(270, 170, 161, 22))
        self.url_in.setDragEnabled(False)
        #self.url_in.setReadOnly(True)
        self.url_in.setObjectName("url_in")
        self.user_in = QtWidgets.QLineEdit(error_2)
        self.user_in.setGeometry(QtCore.QRect(270, 220, 161, 22))
        self.user_in.setObjectName("user_in")
        self.pass_in = QtWidgets.QLineEdit(error_2)
        self.pass_in.setGeometry(QtCore.QRect(270, 270, 161, 22))
        self.pass_in.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_in.setObjectName("pass_in")
        self.add = QtWidgets.QPushButton(error_2)
        self.add.setGeometry(QtCore.QRect(390, 350, 93, 28))
        self.add.setObjectName("add")
        self.error = QtWidgets.QLabel(error_2)
        self.error.setGeometry(QtCore.QRect(80, 360, 400, 16))
        self.error.setStyleSheet("color:red;")
        self.error.setObjectName("error")
        self.title = QtWidgets.QLabel(error_2)
        self.title.setGeometry(QtCore.QRect(80, 60, 201, 21))
        self.title.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.title.setObjectName("title")

        self.retranslateUi(error_2)
        QtCore.QMetaObject.connectSlotsByName(error_2)

    def retranslateUi(self, error_2):
        _translate = QtCore.QCoreApplication.translate
        error_2.setWindowTitle(_translate("error_2", "Form"))
        self.Name.setText(_translate("error_2", "DataBase Name"))
        self.user.setText(_translate("error_2", "User Name"))
        self.password.setText(_translate("error_2", "Password"))
        self.url.setText(_translate("error_2", "DataBase Host"))
        self.add.setText(_translate("error_2", "ADD"))
        self.error.setText(_translate("error_2", "*"))
        self.title.setText(_translate("error_2", "Add New DataBase"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_2 = QtWidgets.QWidget()
    ui = Add_Host()
    ui.setupUi(error_2)
    error_2.show()
    sys.exit(app.exec_())
