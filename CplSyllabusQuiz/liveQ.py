
import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *




class Ui_live(object):
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
    ui = Ui_live()
    ui.setupUi(MainWindow)
    MainWindow.load(QtCore.QUrl('https://docs.google.com/forms/d/e/1FAIpQLSdXfH8yhBzGCTM5b3vp4BF8Kw1ztVwvkVCfKXzPNXfKzwYvTg/viewform?usp=sf_link'))
    MainWindow.show()
    sys.exit(app.exec_())
