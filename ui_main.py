# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folder = QtWidgets.QPushButton(self.centralwidget)
        self.folder.setGeometry(QtCore.QRect(0, 0, 111, 23))
        self.folder.setObjectName("folder")
        self.replay = QtWidgets.QPushButton(self.centralwidget)
        self.replay.setGeometry(QtCore.QRect(50, 500, 101, 41))
        self.replay.setObjectName("replay")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(270, 500, 101, 41))
        self.next.setObjectName("next")
        self.folderpath = QtWidgets.QLabel(self.centralwidget)
        self.folderpath.setGeometry(QtCore.QRect(140, 0, 581, 16))
        self.folderpath.setObjectName("folderpath")
        self.Videoname = QtWidgets.QLabel(self.centralwidget)
        self.Videoname.setGeometry(QtCore.QRect(140, 30, 321, 21))
        self.Videoname.setObjectName("Videoname")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(680, 500, 141, 41))
        self.save.setObjectName("save")
        self.emotion = QtWidgets.QLabel(self.centralwidget)
        self.emotion.setGeometry(QtCore.QRect(640, 430, 141, 41))
        self.emotion.setObjectName("emotion")
        self.videoplayer = QtWidgets.QLabel(self.centralwidget)
        self.videoplayer.setGeometry(QtCore.QRect(37, 67, 571, 381))
        self.videoplayer.setObjectName("videoplayer")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(670, 0, 160, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.happy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.happy.setObjectName("happy")
        self.verticalLayout.addWidget(self.happy)
        self.sad = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sad.setObjectName("sad")
        self.verticalLayout.addWidget(self.sad)
        self.surprise = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.surprise.setObjectName("surprise")
        self.verticalLayout.addWidget(self.surprise)
        self.disgust = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.disgust.setObjectName("disgust")
        self.verticalLayout.addWidget(self.disgust)
        self.angry = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.angry.setObjectName("angry")
        self.verticalLayout.addWidget(self.angry)
        self.fear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.fear.setObjectName("fear")
        self.verticalLayout.addWidget(self.fear)
        self.uncertain = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.uncertain.setObjectName("uncertain")
        self.verticalLayout.addWidget(self.uncertain)
        self.noemotion = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.noemotion.setObjectName("noemotion")
        self.verticalLayout.addWidget(self.noemotion)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.folder.setText(_translate("MainWindow", "Choose Folder"))
        self.replay.setText(_translate("MainWindow", "Play / Replay"))
        self.next.setText(_translate("MainWindow", "Next >>"))
        self.folderpath.setText(_translate("MainWindow", "folderpath"))
        self.Videoname.setText(_translate("MainWindow", "videoname"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.emotion.setText(_translate("MainWindow", "emotion"))
        self.videoplayer.setText(_translate("MainWindow", "TextLabel"))
        self.happy.setText(_translate("MainWindow", "Happy"))
        self.sad.setText(_translate("MainWindow", "Sad"))
        self.surprise.setText(_translate("MainWindow", "Surprise"))
        self.disgust.setText(_translate("MainWindow", "Disgust"))
        self.angry.setText(_translate("MainWindow", "Angry"))
        self.fear.setText(_translate("MainWindow", "Fear"))
        self.uncertain.setText(_translate("MainWindow", "Uncertain"))
        self.noemotion.setText(_translate("MainWindow", "NoEmotion"))
