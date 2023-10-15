


from PyQt5 import QtCore, QtGui, QtWidgets
from add_path import Add_Path
from add_host import Add_Host
from User import User
from DataBase import DataBase, DataBase_Manage

class Edit_Add(object):
    
    def __init__(self, user=User("Guest")):
        self.user = user

        self.window1  = QtWidgets.QMainWindow()
        self.add_path = Add_Path()
        self.add_path.setupUi(self.window1)

        self.window2  = QtWidgets.QMainWindow()
        self.add_host = Add_Host()
        self.add_host.setupUi(self.window2)


    def add_starter(self):
        if str(self.type_in.currentText())=="MySQl":
            self.start_add_host()
        elif str(self.type_in.currentText())=="SqLite":
            self.start_add_path()
        elif str(self.type_in.currentText())=="PostgreSQL":
            self.start_add_host()

    def start_add_path(self):
        self.window1.show()
        self.Form.hide()

    def start_add_host(self):
        self.window2.show()
        self.Form.hide()

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(449, 439)

        self.type_in = QtWidgets.QComboBox(Form)
        self.type_in.setGeometry(QtCore.QRect(230, 330, 161, 21))
        self.type_in.setObjectName("type_in")

        self.type_in.addItem("")
        self.type_in.addItem("")
        self.type_in.addItem("")

        self.type = QtWidgets.QLabel(Form)
        self.type.setGeometry(QtCore.QRect(40, 330, 111, 20))
        self.type.setObjectName("type")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 10, 81, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Downlods/edit-tools.png"))
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 190, 151, 22))
        self.comboBox.setObjectName("comboBox")

        for item in self.user.Database :
            self.comboBox.addItem(item.name)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_starter)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.type_in.setItemText(0, _translate("Form", "MySQl"))
        self.type_in.setItemText(1, _translate("Form", "SqLite"))
        self.type_in.setItemText(2, _translate("Form", "PostgreSQL"))
        self.type.setText(_translate("Form", "DataBase Type"))
        self.label_2.setText(_translate("Form", "DataBase Name"))
        self.pushButton.setText(_translate("Form", "Edit"))
        self.pushButton_2.setText(_translate("Form", "Add"))
        self.label_3.setText(_translate("Form", "Edit existing DataBase ___________"))
        self.label_4.setText(_translate("Form", "Add new DataBase ________________"))

    def db_cb_update(self):
        self.comboBox.clear()
        for item in self.user.Database :
                self.comboBox.addItem(item.name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Edit_Add()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
