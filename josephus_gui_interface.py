import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from josephus.adapter.gui_interface.mainwindow import Ui_MainWindow
from josephus.joseph import joseph as jos
from josephus.adapter import read_data as rd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
 
        # 添加槽链接
        self.start_game.clicked.connect(self.show_people)
        self.clear.clicked.connect(self.clear_result)
        
    def show_people(self):
        path = self.path_list.currentText()
        reader = rd.read_data(path)
        for each in reader:
            self.original_people.appendPlainText(each.name+" "+str(each.age))

        josephus = jos.JosephusRing(reader)
        josephus.start = int(self.start.text())
        josephus.step = int(self.step.text())
        for each in josephus:
            self.show_result.appendPlainText(each.name+" "+str(each.age))
        
    def clear_result(self):
        self.original_people.clear()
        self.show_result.clear()

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 

        
