

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 60, 261, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 41))
        self.label.setObjectName("label")
        self.path_list = QtWidgets.QComboBox(self.frame)
        self.path_list.setGeometry(QtCore.QRect(100, 10, 131, 41))
        self.path_list.setObjectName("path_list")
        self.path_list.addItem("")
        self.path_list.addItem("")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 71, 51))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 71, 41))
        self.label_5.setObjectName("label_5")
        self.start = QtWidgets.QLineEdit(self.frame)
        self.start.setGeometry(QtCore.QRect(100, 80, 131, 41))
        self.start.setObjectName("start")
        self.step = QtWidgets.QLineEdit(self.frame)
        self.step.setGeometry(QtCore.QRect(100, 170, 131, 41))
        self.step.setObjectName("step")
        self.start_game = QtWidgets.QPushButton(self.frame)
        self.start_game.setGeometry(QtCore.QRect(20, 260, 211, 41))
        self.start_game.setObjectName("start_game")
        self.clear = QtWidgets.QPushButton(self.frame)
        self.clear.setGeometry(QtCore.QRect(20, 320, 211, 41))
        self.clear.setObjectName("clear")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 10, 201, 41))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 20, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(780, 10, 181, 41))
        self.label_7.setObjectName("label_7")
        self.original_people = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.original_people.setGeometry(QtCore.QRect(350, 60, 251, 351))
        self.original_people.setPlainText("")
        self.original_people.setObjectName("original_people")
        self.show_result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.show_result.setGeometry(QtCore.QRect(680, 60, 241, 351))
        self.show_result.setPlainText("")
        self.show_result.setObjectName("show_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "path_list", None, -1))
        self.path_list.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "person.txt", None, -1))
        self.path_list.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "person.csv", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "start", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "step", None, -1))
        self.start.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.step.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.start_game.setText(QtWidgets.QApplication.translate("MainWindow", "start_game", None, -1))
        self.clear.setText(QtWidgets.QApplication.translate("MainWindow", "clear", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "original_people", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "init", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "show_result", None, -1))

