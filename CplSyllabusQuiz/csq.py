from email.errors import StartBoundaryNotFoundDefect
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from genericpath import exists
from telnetlib import theNULL
from turtle import back
from PyQt5 import QtCore, QtGui, QtWidgets
from engine import CsqEngine
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from study import Ui_Study
from liveQ import Ui_live
from rankQ import Ui_rank
from PyQt5.QtWebEngineWidgets import *
from os.path import exists
import sys
import os


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        global index
        index=-1
        self.answerChosen=False
        self.started=0
        self.nexxt=1
        self.bacck=self.nexxt-1
        self.cDetail=CsqEngine()
        self.scenario=CsqEngine()
        self.mainQuestion=CsqEngine()
        self.answerA=CsqEngine()
        self.answerB=CsqEngine()
        self.answerC=CsqEngine()
        self.answerD=CsqEngine()
        self.correct=CsqEngine()
        self.saveAnswer=CsqEngine()
        self.startText=CsqEngine()
        
        
       
        self.begin=False
        self.submit=False
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.courseListLabel = QtWidgets.QLabel(self.centralwidget)
        self.courseListLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.courseListLabel.setObjectName("courseListLabel")
        self.courseListLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.courseListLabel.setFont(QFont('Arial', 11))
        self.courseListLabel.setWordWrap(True)

        self.gridLayout.addWidget(self.courseListLabel, 0, 0, 1, 1)
        self.questionDetail = QtWidgets.QLabel(self.centralwidget)
        self.questionDetail.setFrameShape(QtWidgets.QFrame.Box)
        self.questionDetail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.questionDetail.setStyleSheet("background-color: rgba(249, 251, 251, 251)")
        
        
        self.questionDetail.setObjectName("questionDetail")
        self.questionDetail.setWordWrap(True)
        
        self.gridLayout.addWidget(self.questionDetail, 6, 1, 1, 3)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("background-color: rgba(249, 251, 251, 251)")
        self.modeBox = QtWidgets.QCheckBox(self.groupBox)
        self.modeBox.setGeometry(QtCore.QRect(6, 30, 200, 26))
        self.modeBox.setObjectName("modeBox")
        self.modeBox.setToolTip('When Helper Mode is checked, the anaswer buttons will chage to \"Green\" if the selected answer is correct and \"Red\" if not.')

        self.shadow1 = QGraphicsDropShadowEffect()
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow3 = QGraphicsDropShadowEffect()
        self.shadow1.setBlurRadius(5)
        self.shadow1.setOffset(0)
        self.shadow1.setColor(QColor("skyblue"))
        
        self.shadow2.setBlurRadius(5)
        self.shadow2.setOffset(0)
        self.shadow2.setColor(QColor("skyblue"))
        
        self.shadow3.setBlurRadius(5)
        self.shadow3.setOffset(0)
        self.shadow3.setColor(QColor("skyblue"))
        
        self.studyButton=QtWidgets.QPushButton(self.groupBox)
        self.liveButton=QtWidgets.QPushButton(self.groupBox)
        self.rankButton=QtWidgets.QPushButton(self.groupBox)
        self.studyButton.setFont(QFont('Arial', 9))
        self.studyButton.setText("Study")
        self.studyButton.setGraphicsEffect(self.shadow1)
        self.studyButton.setGeometry(QtCore.QRect(8, 60, 200, 26))
        self.liveButton.setText("Live Quiz")
        self.liveButton.setGraphicsEffect(self.shadow2)
        self.liveButton.setGeometry(QtCore.QRect(8, 90, 200, 26))
        self.rankButton.setText("Live Rankings")
        self.rankButton.setGraphicsEffect(self.shadow3)
        self.rankButton.setGeometry(QtCore.QRect(8, 120, 200, 26))

        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setFont(QFont('Arial', 9))
        self.gridLayout.addWidget(self.resetButton, 5, 0, 1, 1)

        #self.gridLayout.addWidget(self.questionDetail, 6, 0, 1, 4)
        self.questionBox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.questionBox.setFont(font)

        self.questionBox.setFont(QFont('Arial', 12))
        self.questionBox.setFrameShape(QtWidgets.QFrame.Box)
        self.questionBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.questionBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.questionBox.setWordWrap(True)
        self.questionBox.setObjectName("questionBox")
        self.gridLayout.addWidget(self.questionBox, 0, 1, 4, 3)
        self.submittButton = QtWidgets.QPushButton(self.centralwidget)
        self.submittButton.setObjectName("submittButton")
        self.submittButton.setFont(QFont('Arial', 9))
        self.questionBox.setStyleSheet("background-color: rgba(249, 251, 251, 251)")

        self.gridLayout.addWidget(self.submittButton, 4, 0, 1, 1)
        self.bButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.bButton.setFont(font)
        self.bButton.setObjectName("bButton")
        self.bButton.setFont(QFont('Arial', 9))
        self.gridLayout.addWidget(self.bButton, 4, 2, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setFont(QFont('Arial', 9))

        self.gridLayout.addWidget(self.nextButton, 4, 3, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.backButton.setFont(QFont('Arial', 9))
        self.gridLayout.addWidget(self.backButton, 5, 3, 1, 1)
        self.choiceLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.choiceLabel2.setFrameShape(QtWidgets.QFrame.Box)
        
        self.choiceLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.choiceLabel2.setText("")
        self.choiceLabel2.setWordWrap(True)
        self.choiceLabel2.setObjectName("choiceLabel2")
        #self.choiceLabel2.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.gridLayout.addWidget(self.choiceLabel2, 3, 0, 1, 1)
        self.choiceLabel = QtWidgets.QLabel(self.centralwidget)
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.choiceLabel.setFont(font)
        self.choiceLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.choiceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.choiceLabel.setObjectName("choiceLabel")
        self.choiceLabel.setStyleSheet("background-image : url(img/icon.png)")
        self.choiceLabel.setScaledContents(True)
        self.gridLayout.addWidget(self.choiceLabel, 2, 0, 1, 1)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(5)
        self.shadow.setOffset(0)
        self.shadow.setColor(QColor("skyblue"))
        
        self.courseList = QtWidgets.QComboBox(self.centralwidget)
        self.courseList.setObjectName("courseList")
        self.courseList.setGraphicsEffect(self.shadow)
        self.courseList.setFont(QFont('Arial', 9))

        
        
        self.items=CsqEngine()
        for clist in self.items.getCourse():
            self.courseList.addItem(clist)
        

        self.gridLayout.addWidget(self.courseList, 1, 0, 1, 1)
        self.aButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.aButton.setFont(font)
        self.aButton.setObjectName("aButton")
        self.aButton.setFont(QFont('Arial', 9))
        self.gridLayout.addWidget(self.aButton, 4, 1, 1, 1)
        self.cButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.cButton.setFont(QFont('Arial', 9))
        self.gridLayout.addWidget(self.cButton, 5, 1, 1, 1)
        self.dButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.dButton.setFont(font)
        self.dButton.setObjectName("dButton")
        self.dButton.setFont(QFont('Arial', 9))
        self.gridLayout.addWidget(self.dButton, 5, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.submittButton.clicked.connect(lambda: self.submitt())
        self.aButton.clicked.connect(lambda: self.getCorrectA(0))
        self.bButton.clicked.connect(lambda: self.getCorrectA(1))
        self.cButton.clicked.connect(lambda: self.getCorrectA(2))
        self.dButton.clicked.connect(lambda: self.getCorrectA(3))
        self.nextButton.clicked.connect(lambda: self.navigate(1))
        self.backButton.clicked.connect(lambda: self.navigate(-1))
        self.resetButton.clicked.connect(lambda: self.reset())
        self.studyButton.clicked.connect(lambda: self.openStudy())
        self.liveButton.clicked.connect(lambda: self.openlive())
        self.rankButton.clicked.connect(lambda: self.openRank())



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Corporal Syllabus Quiz 2022-19877 Cons. O. McKenzie"))
        self.courseListLabel.setText(_translate("MainWindow", "Select Course"))
        self.questionDetail.setText(_translate("MainWindow", "Question details"))
        self.questionBox.setText(_translate("MainWindow", self.startText.getRandomQuote()))
        self.submittButton.setText(_translate("MainWindow", "Submit"))
        self.bButton.setText(_translate("MainWindow", "B"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.choiceLabel.setText(_translate("MainWindow", ""))
        self.aButton.setText(_translate("MainWindow", "A"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.dButton.setText(_translate("MainWindow", "D"))

        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.modeBox.setText(_translate("MainWindow", "Helper Mode"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        
    def openStudy(self):
        self.studyWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Study()
        self.ui.setupUi(self.studyWindow)
        self.studyWindow.show()
    def openlive(self):
        self.liveWindow = QWebEngineView()
        self.ui = Ui_live()
        self.ui.setupUi(self.liveWindow)
        self.liveWindow.load(QtCore.QUrl('https://docs.google.com/forms/d/e/1FAIpQLSdXfH8yhBzGCTM5b3vp4BF8Kw1ztVwvkVCfKXzPNXfKzwYvTg/viewform?usp=sf_link'))
        self.liveWindow.show()
    def openRank(self):
        self.rankWindow = QWebEngineView()
        self.ui = Ui_rank()
        self.ui.setupUi(self.rankWindow)
        self.rankWindow.load(QtCore.QUrl('https://docs.google.com/spreadsheets/d/1_KzVdYGxY3uJL_TyXT5gPPMU4AMmdRjKD7BdMT2NWkA/edit?usp=sharing'))
        self.rankWindow.show()
   

    def submitt(self):
        global listText
        global getIndex
        global index

        if self.begin == False and self.submit == False:
            self.submit=True
            listText=self.courseList.currentText()
            getIndex=self.courseList.findText(listText, QtCore.Qt.MatchFixedString)
            index=getIndex
        self.choiceLabel2.setText(self.cDetail.getCourseDetail(index))
        self.choiceLabel2.setFont(QFont('Arial', 9))
   
        if index > 0:
            self.courseListLabel.setText(listText)
            if self.scenario.getQuestionBank("data",listText+".xlsx",self.nexxt,-2)==-1:
                self.questionDetail.setFont(QFont('Arial', 18))
                self.questionDetail.setText("🎊🎊 You completed all questions in the "+listText+" quiz. See Results above 🎊🎊")
                self.submit=False
                self.begin=False
                self.started=0
                self.nexxt=1
                index=-5
                self.questionBox.setText("\tYour Answer\t\tCorrect Answer\n")
                c=1
                for rTable in self.saveAnswer.getAnswers(-1,-1,1,-1):
                    if not rTable:
                        continue
                    else:
                        self.questionBox.setText(self.questionBox.text()+"\n"+str(c)+".\t"+str(rTable))
                        c=c+1
                mark=self.saveAnswer.getGrade(c-1)
                self.questionBox.setText(self.questionBox.text()+"\n\n"+"\tYour score is "+str(mark)+"%")
                self.cDetail.reset()
                self.scenario.reset()
                self.mainQuestion.reset()
                self.answerA.reset()
                self.answerB.reset()
                self.answerC.reset()
                self.answerD.reset()
                self.correct.reset()
                self.saveAnswer.reset()
                

            else:
                if self.modeBox.isChecked() == True:
                    self.aButton.setStyleSheet('background-color : white')
                    self.bButton.setStyleSheet('background-color : white')
                    self.cButton.setStyleSheet('background-color : white')
                    self.dButton.setStyleSheet('background-color : white')
                else:
                    self.aButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
                    self.bButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
                    self.cButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
                    self.dButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
                
                self.questionDetail.setFont(QFont('Arial', 12))
                self.questionDetail.setText("⚠️ "+self.scenario.getQuestionBank("data",listText+".xlsx",self.nexxt,-2))
                self.questionBox.setFont(QFont('Arial', 16))
                self.questionBox.setText(self.mainQuestion.getQuestionBank("data",listText+".xlsx",self.nexxt,-1)+"\n\n"
                +self.answerA.getQuestionBank("data",listText+".xlsx",self.nexxt,0)+"\n\n"+self.answerB.getQuestionBank("data",listText+".xlsx",self.nexxt,1)+"\n\n"
                +self.answerC.getQuestionBank("data",listText+".xlsx",self.nexxt,2)+"\n\n"+self.answerD.getQuestionBank("data",listText+".xlsx",self.nexxt,3))
        else:
            self.submit=False
            self.begin=False
            self.courseListLabel.setText("Please submit course option.")
    
    def reset(self):
        global index
        self.submit=False
        self.begin=False
        self.started=0
        self.nexxt=1
        index=-1
        self.courseList.setCurrentText("-------Select--------")
        self.cDetail.reset()
        self.scenario.reset()
        self.mainQuestion.reset()
        self.answerA.reset()
        self.answerB.reset()
        self.answerC.reset()
        self.answerD.reset()
        self.correct.reset()
        self.saveAnswer.reset()
        self.aButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
        self.bButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
        self.cButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
        self.dButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.829545, y1:0.295455, x2:0.364, y2:0.488636, stop:0 rgba(21, 165, 255, 211), stop:1 rgba(255, 255, 255, 255));")
        self.choiceLabel2.setText("")
        self.courseListLabel.setText("Select Course")
        self.questionDetail.setText("Question details")
        
        self.questionBox.setText(self.startText.getRandomQuote())
        
        

    def getCorrectA(self,chosen):
        global listText
        global getIndex
        global index
        
        if chosen == 0:
            displayChoice="A"
        if chosen == 1:
            displayChoice="B"
        if chosen == 2:
            displayChoice="C"
        if chosen == 3:
            displayChoice="D"
        if self.submit == True:
            if index > 0:

                
                if self.modeBox.isChecked() == True:
                    self.aButton.setStyleSheet('background-color : white')
                    self.bButton.setStyleSheet('background-color : white')
                    self.cButton.setStyleSheet('background-color : white')
                    self.dButton.setStyleSheet('background-color : white')
                    if chosen!=self.correct.getQuestionBank("data",listText+".xlsx",self.nexxt,4):
                        match chosen:
                            case 0:
                                self.aButton.setStyleSheet('background-color : red')
                            case 1:
                                self.bButton.setStyleSheet('background-color : red')
                            case 2:
                                self.cButton.setStyleSheet('background-color : red')
                            case 3:
                                self.dButton.setStyleSheet('background-color : red')
                            case _:
                                print(chosen)
                    else:
                        match chosen:
                            case 0:
                                self.aButton.setStyleSheet('background-color : green')
                            case 1:
                                self.bButton.setStyleSheet('background-color : green')
                            case 2:
                                self.cButton.setStyleSheet('background-color : green')
                            case 3:
                                self.dButton.setStyleSheet('background-color : green')
                            case _:
                                print(chosen)

                self.saveAnswer.getAnswers(chosen,self.correct.getQuestionBank("data",listText+".xlsx",self.nexxt,4),0,self.started)
                
                self.begin=True
                self.answerChosen=True
                self.courseListLabel.setText(listText+"\n"+"Selected answer is: "+displayChoice)
        
    def navigate(self,forward):
        global index
        if index > 0 and self.begin==True:
            if self.answerChosen == True and forward==1:
                self.nexxt=self.nexxt+1
                self.answerChosen=False
                self.submitt()
                self.started=self.started+1
            elif forward==-1 and self.nexxt > 1:
                self.started=self.started-1
                self.nexxt=self.nexxt-1
                self.answerChosen=False
                self.submitt()
            else:
                self.courseListLabel.setText(listText+"\n"+"Please choose an answer 👉")
        elif index == -1:
            self.courseListLabel.setText("Select Course"+"\n"+"Please Select a Course from the drop-down list \nBELOW👇 THEN press submit!")
        elif index == 1 and self.begin==False:
            self.courseListLabel.setText(listText+"\n"+"Please choose an answer 👉")
        elif index == 0 and self.begin==False:
            self.courseListLabel.setText("Select Course"+"\n"+"Please Select a Course from the drop-down list \nBELOW👇 THEN press submit!")
        elif index == -5:
            self.courseListLabel.setText("Please press the reset button or Select Course"+"\n"+"Please Select a Course from the drop-down list \nBELOW👇 THEN press submit!")
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    app.setStyleSheet("QCheckBox{font-size: 9pt}")
    MainWindow.show()
    
    sys.exit(app.exec_())
