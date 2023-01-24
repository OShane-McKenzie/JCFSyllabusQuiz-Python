import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWebEngineWidgets import *
app=QtWidgets.QApplication(sys.argv)
w=QWebEngineView()
w.setWindowTitle("Rankings")
w.load(QtCore.QUrl('https://docs.google.com/spreadsheets/d/1_KzVdYGxY3uJL_TyXT5gPPMU4AMmdRjKD7BdMT2NWkA/edit?usp=sharing'))
w.showMaximized()
app.exec_()

