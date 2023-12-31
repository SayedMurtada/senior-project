


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 460)
        self.name_in = QtWidgets.QLineEdit(Form)
        self.name_in.setGeometry(QtCore.QRect(270, 120, 161, 22))
        self.name_in.setObjectName("name_in")
        self.Name = QtWidgets.QLabel(Form)
        self.Name.setGeometry(QtCore.QRect(80, 120, 111, 20))
        self.Name.setObjectName("Name")
        self.type_in = QtWidgets.QComboBox(Form)
        self.type_in.setGeometry(QtCore.QRect(270, 170, 161, 21))
        self.type_in.setObjectName("type_in")
        self.type_in.addItem("")
        self.type = QtWidgets.QLabel(Form)
        self.type.setGeometry(QtCore.QRect(80, 170, 111, 20))
        self.type.setObjectName("type")
        self.user = QtWidgets.QLabel(Form)
        self.user.setGeometry(QtCore.QRect(80, 270, 111, 20))
        self.user.setObjectName("user")
        self.pass = QtWidgets.QLabel(Form)
        self.pass.setGeometry(QtCore.QRect(80, 320, 121, 16))
        self.pass.setObjectName("pass")
        self.url = QtWidgets.QLabel(Form)
        self.url.setGeometry(QtCore.QRect(80, 220, 121, 16))
        self.url.setObjectName("url")
        self.url_in = QtWidgets.QLineEdit(Form)
        self.url_in.setGeometry(QtCore.QRect(270, 220, 161, 22))
        self.url_in.setObjectName("url_in")
        self.user_in = QtWidgets.QLineEdit(Form)
        self.user_in.setGeometry(QtCore.QRect(270, 270, 161, 22))
        self.user_in.setObjectName("user_in")
        self.pass_in = QtWidgets.QLineEdit(Form)
        self.pass_in.setGeometry(QtCore.QRect(270, 320, 161, 22))
        self.pass_in.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_in.setObjectName("pass_in")
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(390, 380, 93, 28))
        self.add.setObjectName("add")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(80, 390, 55, 16))
        self.error.setObjectName("error")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 60, 201, 21))
        self.label.setStyleSheet("font: 75 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Name.setText(_translate("Form", "DataBase Name"))
        self.type_in.setItemText(0, _translate("Form", "SQl"))
        self.type.setText(_translate("Form", "DataBase Type"))
        self.user.setText(_translate("Form", "User Name"))
        self.pass.setText(_translate("Form", "Password"))
        self.url.setText(_translate("Form", "DataBase URL"))
        self.add.setText(_translate("Form", "ADD"))
        self.error.setText(_translate("Form", "*"))
        self.label.setText(_translate("Form", "Add New DataBase"))
