import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *




class Ui_rank(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Live Quiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QWebEngineView()
    ui = Ui_rank()
    ui.setupUi(MainWindow)
    MainWindow.load(QtCore.QUrl('https://docs.google.com/spreadsheets/d/1_KzVdYGxY3uJL_TyXT5gPPMU4AMmdRjKD7BdMT2NWkA/edit?usp=sharing'))
    MainWindow.show()
    sys.exit(app.exec_())