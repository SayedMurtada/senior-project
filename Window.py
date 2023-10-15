
import sys
from User import User
from edit_add import Edit_Add
from DataBase import DataBase, DataBase_Manage
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        #windows
        self.edit_add = Edit_Add()
        #start window
        self.start_edit_add()

    def start_edit_add(self):
        self.edit_add.setupUi(self)
        self.setWindowTitle("Edit\Add")
        self.show()


    
# if __name__ == "__main__":
#         app = QApplication(sys.argv)
#         w = Window()
#         sys.exit(app.exec_())