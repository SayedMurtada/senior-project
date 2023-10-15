# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, Tables=None, Columns=None, DB_name=""):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(350, 480, 111, 41))
        self.Generate.setObjectName("Generate")
        self.Generate.clicked.connect(self.Generate_clicked)

        self.name_space = QtWidgets.QLineEdit(self.centralwidget)
        self.name_space.setGeometry(QtCore.QRect(20, 490, 291, 22))
        self.name_space.setObjectName("name_space")

        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 470, 71, 16))
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 55, 16))
        self.label_2.setObjectName("label_2")

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 30, 441, 431))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, DB_name)

        j = Tables[0]
        print(type(j))
        j = Tables[0].tostring()
        j = np.fromstring(j, dtype=int)
        print(type(j))

        for i in range(Tables.size):
            parent = QTreeWidgetItem(self.treeWidget)
            parent.setText(0, Tables[i])
            parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            for x in range(Columns.shape[1]):
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, Columns[i][x])
                child.setCheckState(0, Qt.Unchecked)
        self.treeWidget.show()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Generator"))
        self.Generate.setText(_translate("MainWindow", "Generate"))
        self.name.setText(_translate("MainWindow", "Page Name"))
        self.label_2.setText(_translate("MainWindow", "Tables"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))

    def find_checked(self):
        checked = dict()
        root = self.treeWidget.invisibleRootItem()
        signal_count = root.childCount()

        for i in range(signal_count):
            signal = root.child(i)
            checked_sweeps = list()
            num_children = signal.childCount()

            for n in range(num_children):
                child = signal.child(n)
                if child.checkState(0) == QtCore.Qt.Checked:
                    checked_sweeps.append(child.text(0))

            checked[signal.text(0)] = checked_sweeps

        return checked

    def Generate_clicked(self, MainWindow):
        if self.name_space.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Enter File Name')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Success")
            msg.setInformativeText(str(self.find_checked()))
            msg.setWindowTitle("Success")
            msg.exec_()


def columns(tables):
    if(sqlite3.connect("project.db")):
        result = []
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        # cur.execute("PRAGMA table_info('" + tables[0] + "');")
        # schema = cur.fetchall()
        # print(*schema, sep="\n")
        l = len(tables)
        for m in range(l):
            cur.execute("PRAGMA table_info('"+tables[m]+"');")
            schema = cur.fetchall()
            # for i in schema:
            #     result.append(schema[i][0])
            # print(tables[m])
            x = len(schema)
            sum = []
            for i in range(x):
                # sum.append(m)
                sum.append(schema[i][1])

                # sum.append(schema[i][5])
                # print(*sum, sep=",")
            # print(type(result))
            result.append(sum)
            # print(*sum)

        conn.close()
        print(result)
        return result
    else:
        print("Failed")


def tables():
    if (sqlite3.connect("project.db")):
        result = []
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        cur.execute('''SELECT name, sql FROM sqlite_master
                        WHERE type='table'
                        ORDER BY name;''')
        schema = cur.fetchall()

        x = len(schema)
        for i in range(x):
            result.append(schema[i][0])
        # print(schema[0][0])
        conn.close()
        # print(*result, sep="\n")
        return result
    else:
        print("Failed")



if __name__ == "__main__":
    ta= tables()
    cols = columns(ta)
    # print(type(cols))
    Tables = np.array(ta)
    Columns = np.array(cols)
    # print(Columns)
    # print(type(Columns))
    # c= [["1", "2", "3"], ["4", '5', "6"], ["3", "9", "6"], ["11", "22", "34"]]
    # print(c)
    # print(type("1"))
    # Tables = np.array(["22", "33", "44", "55"])
    # Columns = np.array([["1", "2", "3"], ["4", '5', "6"], ["3", "9", "6"], ["11", "22", "34"]])
    # print(Columns)
    # print(type(Columns))
    # DB_name = "KFUPM"
    #
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow, Tables, Columns, DB_name)
    # MainWindow.show()
    # sys.exit(app.exec_())
