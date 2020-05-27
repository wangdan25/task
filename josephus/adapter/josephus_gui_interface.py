import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QMessageBox
from josephus.adapter.gui_interface.mainwindow import Ui_MainWindow
from josephus.joseph import joseph as jos
from josephus.adapter.interface import Interface

class MainWindow(Interface, QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
 
        # 添加槽链接
        self.start_game.clicked.connect(self.show_people)
        self.clear.clicked.connect(self.clear_result)

    def create_reader(self):
        path = self.path_list.currentText()
        reader = self.read_data(path)
        return reader

    def set_start_step(self):
        start = int(self.start.text())
        try:
            self.check_start_value(start)
        except ValueError:
            QMessageBox.warning(self, 'warning', '起始值不能为负数！')

        step = int(self.step.text())
        try:
            self.check_step_value(step)
        except ValueError:
            QMessageBox.warning(self, 'warning', '步进大于1！')
        return (start, step)

    def show_people(self):
        reader = self.create_reader()
        for each in reader:
            self.original_people.appendPlainText(each.name+" "+str(each.age))

        start, step = self.set_start_step()
        josephus = self.create_joseph(reader, start, step)
        for each in josephus:
            self.show_result.appendPlainText(each.name+" "+str(each.age))
        
    def clear_result(self):
        self.original_people.clear()
        self.show_result.clear()


        
