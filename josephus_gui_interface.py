import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QMessageBox
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
 
    def josephus_init(self):
        start = int(self.start.text())
        if start < 0:
            QMessageBox.warning(self, 'warning', '起始值不能为负数！')
            raise ValueError
        step = int(self.step.text())
        if step < 1:
            QMessageBox.warning(self, 'warning', '步进要大于0！')
            raise ValueError
        return (start, step)

    def show_people(self):
        path = self.path_list.currentText()
        reader = rd.read_data(path)
        for each in reader:
            self.original_people.appendPlainText(each.name+" "+str(each.age))

        josephus = jos.JosephusRing(reader)
        josephus.start, josephus.step= self.josephus_init()
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
 

        
