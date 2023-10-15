

from PyQt5 import QtCore, QtGui, QtWidgets
from DataBase import DataBase, DataBase_Manage
from User import User

class Add_Path(object):

    def __init__(self, user=User("Guest")):
        self.user = user

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 405)
        self.url = QtWidgets.QLabel(Form)
        self.url.setGeometry(QtCore.QRect(50, 240, 121, 16))
        self.url.setObjectName("url")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(50, 40, 361, 21))
        self.title.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.title.setObjectName("title")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(50, 340, 400, 16))
        self.error.setStyleSheet("color:red;")
        self.error.setObjectName("error")
        self.Name = QtWidgets.QLabel(Form)
        self.Name.setGeometry(QtCore.QRect(50, 140, 111, 20))
        self.Name.setObjectName("Name")
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(360, 330, 93, 28))
        self.add.setObjectName("add")
        self.url_in = QtWidgets.QLineEdit(Form)
        self.url_in.setGeometry(QtCore.QRect(240, 240, 161, 22))
        self.url_in.setObjectName("url_in")
        self.name_in = QtWidgets.QLineEdit(Form)
        self.name_in.setGeometry(QtCore.QRect(240, 140, 161, 22))
        self.name_in.setObjectName("name_in")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(410, 240, 31, 21))
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(archive.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.url.setText(_translate("Form", "DataBase Path"))
        self.title.setText(_translate("Form", "Add New DataBase (SQLite)"))
        self.error.setText(_translate("Form", "*"))
        self.Name.setText(_translate("Form", "DataBase Name"))
        self.add.setText(_translate("Form", "ADD"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Add_Path()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
