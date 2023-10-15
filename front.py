
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
from User import User
from DataBase import DataBase
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Front(object):

    def __init__(self, user=User("Guest")):
        self.username = user

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(565, 710)
        MainWindow.setWindowTitle("DataBase Editor")
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)

        self.centralwidget = QWidget(MainWindow)

        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(370, 590, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Generate.setFont(font)
        self.Generate.setObjectName("Generate")
        self.table = QtWidgets.QLabel(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 120, 55, 16))
        self.table.setObjectName("table")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 140, 441, 431))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.treeWidget.setFont(font)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "None")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 620, 400, 30))
        self.label.setStyleSheet("color:red;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.db_cb = QtWidgets.QComboBox(self.centralwidget)
        self.db_cb.setGeometry(QtCore.QRect(190, 70, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_cb.setFont(font)
        self.db_cb.setObjectName("db_cb")

        for item in self.username.Database :
                self.db_cb.addItem(item.name)

        self.db = QtWidgets.QLabel(self.centralwidget)
        self.db.setGeometry(QtCore.QRect(20, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db.setFont(font)
        self.db.setObjectName("db")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(20, 10, 41, 31))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("man-avatar.png"))
        self.img.setObjectName("img")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(60, 20, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.user.setFont(font)
        self.user.setStyleSheet("color:rgb(85, 170, 255);")
        self.user.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user.setScaledContents(False)
        self.user.setWordWrap(False)
        self.user.setObjectName("user")
        self.log_out_2 = QtWidgets.QPushButton(self.centralwidget)
        self.log_out_2.setGeometry(QtCore.QRect(530, 20, 21, 21))
        self.log_out_2.setStyleSheet("background-color: transparent;\n"
"border-image: url(multimedia-option.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"\n"
"")
        self.log_out_2.setText("")
        self.log_out_2.setObjectName("log_out_2")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(430, 70, 21, 21))
        self.add.setStyleSheet("background-color: transparent;\n"
"border-image:url(interface(1).png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"\n"
"")
        self.add.setText("")
        self.add.setObjectName("add")

        self.retranslateUi(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def db_cb_update(self, usr):
        self.username = usr
        self.db_cb.clear()
        for item in self.username.Database :
                self.db_cb.addItem(item.name)

    def update_tree(self, Tables=None, Columns=None, DB="DB"):
        for i in range(len(Tables)):
                parent = QTreeWidgetItem(self.treeWidget)
                parent.setText(0, Tables[i])
                parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                for x in range(len(Columns)):
                        if i==Columns[x][0]:
                                child = QTreeWidgetItem(parent)
                                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                        if Columns[x][2]==1:
                                child.setText(0, Columns[x][1]+" [PK]")
                        else:
                                child.setText(0, Columns[x][1])
                        child.setCheckState(0, Qt.Unchecked)
                                
        self.treeWidget.show() 


                
    def find_checked(self):
        tables  = []
        columns = []
        root = self.treeWidget.invisibleRootItem()
        signal_count = root.childCount()

        count = 0
        for i in range(signal_count):
            p = False
            signal = root.child(i)
            num_children = signal.childCount()
            for n in range(num_children):
                child = signal.child(n)
                if child.checkState(0) == QtCore.Qt.Checked:
                    p = True
                    checked_sweeps = []
                    checked_sweeps.append(count)
                    if child.text(0).endswith("[PK]"):
                        checked_sweeps.append(child.text(0)[:len(child.text(0))-5])
                        checked_sweeps.append('1')
                    else:
                        checked_sweeps.append(child.text(0))
                        checked_sweeps.append('0')
                        
                    columns.append(checked_sweeps)  
                    
            if p:
                count += 1
                tables.append(signal.text(0))

        return tables, columns
    
    def retranslateUi(self, Front):
        _translate = QtCore.QCoreApplication.translate
        Front.setWindowTitle(_translate("Front", "Front"))
        self.Generate.setText(_translate("Front", "Generate"))
        self.table.setText(_translate("Front", "Tables"))
        self.label.setText(_translate("Front", "*"))
        self.db.setText(_translate("Front", "Selected DataBase"))
        self.user.setText(_translate("Front", self.username.name))
