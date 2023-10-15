import sys
from User import User
from DataBase import DataBase, DataBase_Manage
from sign_in import Sign_In
from sign_up import Sign_Up
from front import Front
from edit_add import Edit_Add
from PyQt5.QtWidgets import QAction, QMessageBox, QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from GenerateWebPage import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.user_db = DataBase_Manage()
        self.user    = User("Guest")

        self.menubar = QtWidgets.QMenuBar(self)
        MainWindow.setWindowIcon(self, QIcon("database.png"))
        self.sign_in = Sign_In()
        self.sign_up = Sign_Up()
        self.front   = Front()

        self.start_sign_in()


    def menue_bar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_Edit_DataBase = QtWidgets.QAction(self)
        self.actionAdd_Edit_DataBase.setObjectName("actionAdd_Edit_DataBase")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUser = QtWidgets.QAction(self)
        self.actionUser.setObjectName("actionUser")
        self.menuFile.addAction(self.actionUser)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionAdd_Edit_DataBase)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())   

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAdd_Edit_DataBase.setText(_translate("MainWindow", "Add\\Edit DataBase"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUser.setText(_translate("MainWindow", "User"))

    def start_sign_in(self):
        self.menubar.hide()
        self.sign_in.setupUi(self)
        self.sign_in.log_in.clicked.connect(self.sign_in_pressed)
        self.sign_in.Sign_up.clicked.connect(self.start_sign_up)
        self.sign_in.Guest.clicked.connect(self.guest_pressed)
        self.show()

    def start_sign_up(self):
        self.menubar.hide()
        self.sign_up.setupUi(self)
        self.sign_up.pushButton.clicked.connect(self.start_sign_in)
        self.sign_up.Sign_up.clicked.connect(self.sign_up_pressed)
        self.show()

    def start_front(self):
        self.menue_bar()
        self.front.setupUi(self)
        self.front.username.name = self.user.name
        self.front.retranslateUi(self)

        #update database items
        if self.user.name != "Guest":
            db = self.user_db.get_db(self.user.name)
            for item in db:
                self.user.Database.append(DataBase(item[2], item[3], item[4], item[5], item[6], item[7]))
                self.front.db_cb.addItem(item[2])

        self.front.log_out_2.clicked.connect(self.log_out_pressed)
        self.front.add.clicked.connect(self.start_edit_add)
        self.front.db_cb.currentIndexChanged.connect(self.db_change)
        self.front.Generate.clicked.connect(partial(self.generate_pressed,"uj"))
        self.show()

    
    def start_edit_add(self):
        self.app2 = QtWidgets.QMainWindow()
        self.edit_add = Edit_Add()
        self.edit_add.setupUi(self.app2)
        self.edit_add.user = self.user
        self.edit_add.db_cb_update()
        self.edit_add.add_path.add.clicked.connect(self.add_path_pressed)
        self.edit_add.add_path.pushButton.clicked.connect(self.select_dir_pressed)
        self.edit_add.add_host.add.clicked.connect(self.add_host_pressed)
        self.app2.show()


    def db_change(self):
            self.front.label.setText("* ")
            index   = self.front.db_cb.currentIndex()
            self.front.treeWidget.clear()
            self.front.treeWidget.headerItem().setText(0, "Tables of "+str(self.front.db_cb.currentText()))
            if self.user.Database[index].db_type == "SqLite" :  
                tables  = self.user.Database[index].tables_sqlite()
                columns = self.user.Database[index].columns_sqlite(tables)
                self.front.update_tree(tables,columns, self.user.Database[index].name)
            elif self.user.Database[index].db_type == "MySQl" :
                tables = MySQLTables(self.user.Database[index].name)
                columns = MySQLColumns(tables, self.user.Database[index].name)
                self.front.update_tree(tables, columns, self.user.Database[index].name)
    
    def select_dir_pressed(self):
        file = QFileDialog.getOpenFileName(self, "Open File")
        self.edit_add.add_path.url_in.setText(file[0])
        self.edit_add.window1.show()

    def log_out_pressed(self):
        self.user_db = DataBase_Manage()
        self.user.Database.clear()
        self.user    = User("Guest")
        self.user.Database =[]
        self.sign_in = Sign_In()
        self.sign_up = Sign_Up()
        self.front   = Front()
        self.front.username = User("Guest")
        self.start_sign_in()

    def guest_pressed(self):
        self.user    = User("Guest")
        self.start_front()


    def add_path_pressed(self):
        p_name = self.edit_add.add_path.name_in.text()
        p_path = self.edit_add.add_path.url_in.text()
        p_type = str(self.edit_add.type_in.currentText())
        print(p_type)
        if len(p_name) == 0:
             self.edit_add.add_path.error.setText("* Enter Name")
        elif len(p_path) == 0:
            self.edit_add.add_path.error.setText("* Enter Path")
        else:
            p_db   = DataBase(name = p_name, db_type=p_type, path= p_path)
            print(p_type)
            if self.user.name == "Guest":
                self.user.Database.append(p_db)
                self.front.db_cb_update(self.user)
                self.edit_add.window1.hide()
            else:
                check=self.user_db.add_db_path(self.user.name, p_db)
                if check:
                    self.user.Database.append(p_db)
                    self.front.db_cb_update(self.user)
                    self.edit_add.window1.hide()
                

    def add_host_pressed(self):
        h_name = self.edit_add.add_host.name_in.text()
        h_user = self.edit_add.add_host.user_in.text()
        h_pass = self.edit_add.add_host.pass_in.text()
        h_host = self.edit_add.add_host.url_in.text()
        h_type = str(self.edit_add.type_in.currentText())
        if len(h_name) == 0:
             self.edit_add.add_host.error.setText("* Enter Name")
        elif len(h_user) == 0:
            self.edit_add.add_host.error.setText("* Enter Username")
        # elif len(h_pass) == 0:
        #     self.edit_add.add_host.error.setText("* Enter Password")
        elif len(h_host) == 0:
            self.edit_add.add_host.error.setText("* Enter Host")
        else:
            h_db   = DataBase(h_name, h_type, h_host, h_user, h_pass)
            if self.user.name == "Guest":
                self.user.Database.append(h_db)
                self.front.db_cb_update(self.user)
                self.edit_add.window2.hide()
            else:
                check=self.user_db.add_db_host(self.user.name, h_db)
                if check:
                    self.user.Database.append(h_db)
                    self.front.db_cb_update(self.user)
                    self.edit_add.window2.hide()



    def generate_pressed(self, text):
        if len(str(self.front.db_cb.currentText())) !=0:
            tables, columns = self.front.find_checked()
            db_type = "sqlite"
            if self.user.Database[self.front.db_cb.currentIndex()].db_type == "SqLite":
                db_type = "sqlite"
            elif self.user.Database[self.front.db_cb.currentIndex()].db_type == "MySQl":
                db_type = "MySQL"
            print("tables:\n" ,tables)
            print("columns:\n",columns)
            if len(tables) == 0:
                self.front.label.setText("* Select tables")
            elif len(columns) == 0:
                self.front.label.setText("* Select columns")
            else:
                file = QFileDialog.getSaveFileName(self, "Select Directory")
                generate(1, tables, columns, file[0], db_type)
                self.front.label.setText("* Saved..")
        else:
            self.front.label.setText("* Select or add a database")



    
    def sign_up_pressed(self):
        username  = self.sign_up.user_inpt.text()
        email     = self.sign_up.email_input.text()
        password  = self.sign_up.pass_input.text()
        password2 = self.sign_up.pass2_input.text()
        if len(username) == 0: 
            self.sign_up.error.setText("* Enter UserNmae")
        elif len(email)==0 :
            self.sign_up.error.setText("* Enter Email")
        elif len(password)==0:
            self.sign_up.error.setText("* Enter Password")
        elif len(password2)==0 :
            self.sign_up.error.setText("* Renter Password")
        elif password != password2 :
            self.sign_up.error.setText("* Passwords don't match")
        else:
            new_user = User(username, email)
            self.user_db.add_user(new_user, password)
            self.sign_up.error.setText("* Done")
            self.start_sign_in()

    def sign_in_pressed(self):
        name     = self.sign_in.user_input.text()
        password = self.sign_in.pass_input.text()
        check = False
        if len(name)==0 | len(password) == 0 :
            print("we r in")
            self.sign_in.error.setText("* Enter user and password")
        else:
            try:
                check = self.user_db.check_user(name, password)
            except Exception:
                print('ERROR')
            if check:
                self.user.name = name 
                #print(self.user_db.get_db)
                self.start_front()
            else:
                self.sign_in.error.setText("* User or Password is Wrong")

    # def close_application(self):
    #     buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if buttonReply == QMessageBox.Yes:
    #         print('Yes clicked.')
    #     else:
    #         print('No clicked.')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
