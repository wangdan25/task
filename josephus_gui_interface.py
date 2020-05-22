import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from josephus.adapter.gui_interface.mainwindow import Ui_MainWindow
from josephus.joseph import joseph as jos
from josephus.adapter import create_ui_reader as rd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
 
        # 添加槽链接
        self.pushButton_start_game.clicked.connect(self.show_result)
        self.pushButton_clear.clicked.connect(self.clear_result)
        
    def show_result(self):
        file_type = self.comboBox_path_list.currentText()
        path = self.lineEdit_path.text()
        file_reader = rd.CreateUiReader(path)
        result = file_reader.create_ui_reader()
        for i in range(len(result)):
            self.plainTextEdit_original_people.appendPlainText(result[i].name+" "+str(result[i].age))

        josephus = jos.JosephusRing(result)
        josephus.start = int(self.lineEdit_start.text())
        josephus.step = int(self.lineEdit_step.text())
        length = len(josephus.query_list())
        generator_people = josephus.next()
        for i in range(length):
            out_people = generator_people.__next__()
            self.plainTextEdit_out_people.appendPlainText(out_people.name+" "+str(out_people.age))
        
    def clear_result(self):
        self.plainTextEdit_original_people.clear()
        self.plainTextEdit_out_people.clear()

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 

        
