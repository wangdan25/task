import sys
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from Joseph.joseph import joseph as jos
from Joseph.file_reader import file_reader as reader

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
 
        # 添加槽链接
        self.pushButton.clicked.connect(self.show_result)
    def show_result(self):
        file_type = self.comboBox.currentText()
        if file_type == "txt":
            path = self.lineEdit.text()
            txt_reader = reader.TxtReader(path)
            result = txt_reader.read_data()
            self.plainTextEdit.appendPlainText(result)
        elif file_type == "csv":
            path = self.lineEdit.text()
            csv_reader = reader.CsvReader(path)
            result = csv_reader.read_data()
            self.plainTextEdit.appendPlainText(result.name+result.age)
        josephus = jos.JosephRing()
        josephus.start = int(self.lineEdit_2.text())
        josephus.step = int(self.lineEdit_3.text())
        length = len(josephus.query_list())
        generator_people = jos.next()
        for i in range(length):
            result = generator_people.__next__()
            self.plainTextEdit_2.appendPlainText(result.name+result.age)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

        
