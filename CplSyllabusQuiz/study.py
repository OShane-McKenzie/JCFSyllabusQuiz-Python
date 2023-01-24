#from msilib.schema import ComboBox
from PyQt5.QtWidgets import QComboBox
from engine import CsqEngine
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import os, sys,subprocess
from sys import platform
from os.path import exists


class Ui_Study(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 417)
        MainWindow.setFixedSize(605, 417)
        MainWindow.setStyleSheet("background-color: rgba(249, 251, 251, 251)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(70, 10, 431, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox, clicked= lambda: self.readMaterial())
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 261, 61))
        self.pushButton.setObjectName("pushButton")
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(5)
        self.shadow.setOffset(0)
        self.shadow.setColor(QColor("skyblue"))
        self.pushButton.setGraphicsEffect(self.shadow)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.sitems=CsqEngine()
        for slist in self.sitems.getStudyList():
            if not slist or slist =="":
                continue
            else:
                self.comboBox.addItem(slist)

    def readMaterial(self):
        self.materialName="./study/"+self.comboBox.currentText()+".pdf"
        isFileFound=os.path.exists(self.materialName)
        if isFileFound==True:
            if platform == "linux" or platform == "linux2":
                 subprocess.call(["xdg-open", self.materialName])
            elif platform == "darwin":
                subprocess.call(["open", self.materialName])
            elif platform == "win32":
                os.startfile(self.materialName)
        else:
            print("File not found")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Study"))
        self.pushButton.setText(_translate("MainWindow", "READ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Study()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    

