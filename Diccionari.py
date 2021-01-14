## Imports
from PyQt5 import QtCore, QtGui, QtWidgets

import sys, logging

from random import randint
###############################################################################

# Principal

class Principal(object):

    def openWindowCat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Catala()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openWindowEsp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Castellano()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()


    def openWindowEng(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = English()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openWindowSearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Buscador()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 708)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Cat = QtWidgets.QPushButton(self.centralwidget)
        self.Cat.setGeometry(QtCore.QRect(50, 130, 421, 91))
        self.Cat.setStyleSheet("font: 87 20pt \"Arial Black\"; background-color: rgb(255, 255, 127);")
        self.Cat.setObjectName("Cat")
        self.Esp = QtWidgets.QPushButton(self.centralwidget)
        self.Esp.setGeometry(QtCore.QRect(50, 240, 421, 91))
        self.Esp.setStyleSheet("background-color: rgb(255, 61, 61); font: 87 20pt \"Arial Black\";")
        self.Esp.setObjectName("Esp")
        self.Eng = QtWidgets.QPushButton(self.centralwidget)
        self.Eng.setGeometry(QtCore.QRect(50, 350, 421, 91))
        self.Eng.setStyleSheet("background-color: rgb(170, 0, 255); font: 87 20pt \"Arial Black\";")
        self.Eng.setObjectName("Eng")
        self.Buscador = QtWidgets.QPushButton(self.centralwidget)
        self.Buscador.setGeometry(QtCore.QRect(50, 460, 421, 91))
        self.Buscador.setStyleSheet("background-color: rgb(255, 170, 0); font: 87 20pt \"Arial Black\";")
        self.Buscador.setObjectName("Buscador")
        self.Titol = QtWidgets.QLabel(self.centralwidget)
        self.Titol.setGeometry(QtCore.QRect(30, 30, 461, 89))
        self.Titol.setStyleSheet("background-color: rgb(109, 109, 109); font: 87 20pt \"Arial Black\";")
        self.Titol.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol.setObjectName("Titol")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.Cat.clicked.connect(self.openWindowCat)
        self.Esp.clicked.connect(self.openWindowEsp)
        self.Eng.clicked.connect(self.openWindowEng)
        self.Buscador.clicked.connect(self.openWindowSearch)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Cat.setText(_translate("MainWindow", "Diccionari de Català"))
        self.Esp.setText(_translate("MainWindow", "Diccionario de Castellano"))
        self.Eng.setText(_translate("MainWindow", "Dictionary of English"))
        self.Buscador.setText(_translate("MainWindow", "Buscador"))
        self.Titol.setText(_translate("MainWindow", "Diccionarios"))

# Pestanya Català

class Catala(object):

    def openPrincipal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Principal()
        self.ui.setupUi(self.window)
        MainWindow.show()
        self.window.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 708)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 521, 701))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Pag1 = QtWidgets.QWidget()
        self.Pag1.setObjectName("Pag1")
        self.Btn_Z = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Z.setGeometry(QtCore.QRect(200, 370, 131, 23))
        self.Btn_Z.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Z.setObjectName("Btn_Z")
        self.Btn_Y = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Y.setGeometry(QtCore.QRect(40, 370, 131, 23))
        self.Btn_Y.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Y.setObjectName("Btn_Y")
        self.Btn_M = QtWidgets.QPushButton(self.Pag1)
        self.Btn_M.setGeometry(QtCore.QRect(40, 250, 131, 23))
        self.Btn_M.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_M.setObjectName("Btn_M")
        self.Btn_G = QtWidgets.QPushButton(self.Pag1)
        self.Btn_G.setGeometry(QtCore.QRect(40, 190, 131, 23))
        self.Btn_G.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_G.setObjectName("Btn_G")
        self.Titol = QtWidgets.QLabel(self.Pag1)
        self.Titol.setGeometry(QtCore.QRect(30, 30, 469, 89))
        self.Titol.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol.setObjectName("Titol")
        self.Btn_K = QtWidgets.QPushButton(self.Pag1)
        self.Btn_K.setGeometry(QtCore.QRect(200, 220, 131, 23))
        self.Btn_K.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_K.setObjectName("Btn_K")
        self.Btn_V = QtWidgets.QPushButton(self.Pag1)
        self.Btn_V.setGeometry(QtCore.QRect(40, 340, 131, 23))
        self.Btn_V.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_V.setObjectName("Btn_V")
        self.Btn_H = QtWidgets.QPushButton(self.Pag1)
        self.Btn_H.setGeometry(QtCore.QRect(200, 190, 131, 23))
        self.Btn_H.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_H.setObjectName("Btn_H")
        self.Btn_J = QtWidgets.QPushButton(self.Pag1)
        self.Btn_J.setGeometry(QtCore.QRect(40, 220, 131, 23))
        self.Btn_J.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_J.setObjectName("Btn_J")
        self.Btn_D = QtWidgets.QPushButton(self.Pag1)
        self.Btn_D.setGeometry(QtCore.QRect(40, 160, 131, 23))
        self.Btn_D.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_D.setObjectName("Btn_D")
        self.Btn_W = QtWidgets.QPushButton(self.Pag1)
        self.Btn_W.setGeometry(QtCore.QRect(200, 340, 131, 21))
        self.Btn_W.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_W.setObjectName("Btn_W")
        self.Btn_B = QtWidgets.QPushButton(self.Pag1)
        self.Btn_B.setGeometry(QtCore.QRect(200, 130, 131, 23))
        self.Btn_B.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_B.setObjectName("Btn_B")
        self.Btn_O = QtWidgets.QPushButton(self.Pag1)
        self.Btn_O.setGeometry(QtCore.QRect(360, 250, 131, 23))
        self.Btn_O.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_O.setObjectName("Btn_O")
        self.Btn_N = QtWidgets.QPushButton(self.Pag1)
        self.Btn_N.setGeometry(QtCore.QRect(200, 250, 131, 21))
        self.Btn_N.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_N.setObjectName("Btn_N")
        self.Btn_E = QtWidgets.QPushButton(self.Pag1)
        self.Btn_E.setGeometry(QtCore.QRect(200, 160, 131, 21))
        self.Btn_E.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_E.setObjectName("Btn_E")
        self.Btn_C = QtWidgets.QPushButton(self.Pag1)
        self.Btn_C.setGeometry(QtCore.QRect(360, 130, 131, 23))
        self.Btn_C.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_C.setObjectName("Btn_C")
        self.Btn_Q = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Q.setGeometry(QtCore.QRect(200, 280, 131, 23))
        self.Btn_Q.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Q.setObjectName("Btn_Q")
        self.Btn_T = QtWidgets.QPushButton(self.Pag1)
        self.Btn_T.setGeometry(QtCore.QRect(200, 310, 131, 23))
        self.Btn_T.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_T.setObjectName("Btn_T")
        self.Btn_P = QtWidgets.QPushButton(self.Pag1)
        self.Btn_P.setGeometry(QtCore.QRect(40, 280, 131, 23))
        self.Btn_P.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_P.setObjectName("Btn_P")
        self.Btn_I = QtWidgets.QPushButton(self.Pag1)
        self.Btn_I.setGeometry(QtCore.QRect(360, 190, 131, 23))
        self.Btn_I.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_I.setObjectName("Btn_I")
        self.Btn_S = QtWidgets.QPushButton(self.Pag1)
        self.Btn_S.setGeometry(QtCore.QRect(40, 310, 131, 23))
        self.Btn_S.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_S.setObjectName("Btn_S")
        self.Btn_F = QtWidgets.QPushButton(self.Pag1)
        self.Btn_F.setGeometry(QtCore.QRect(360, 160, 131, 23))
        self.Btn_F.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_F.setObjectName("Btn_F")
        self.Btn_L = QtWidgets.QPushButton(self.Pag1)
        self.Btn_L.setGeometry(QtCore.QRect(360, 220, 131, 23))
        self.Btn_L.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_L.setObjectName("Btn_L")
        self.Btn_X = QtWidgets.QPushButton(self.Pag1)
        self.Btn_X.setGeometry(QtCore.QRect(360, 340, 131, 23))
        self.Btn_X.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_X.setObjectName("Btn_X")
        self.Btn_U = QtWidgets.QPushButton(self.Pag1)
        self.Btn_U.setGeometry(QtCore.QRect(360, 310, 131, 23))
        self.Btn_U.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_U.setObjectName("Btn_U")
        self.Btn_R = QtWidgets.QPushButton(self.Pag1)
        self.Btn_R.setGeometry(QtCore.QRect(360, 280, 131, 23))
        self.Btn_R.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_R.setObjectName("Btn_R")
        self.Enrere = QtWidgets.QPushButton(self.Pag1)
        self.Enrere.setGeometry(QtCore.QRect(140, 650, 251, 41))
        self.Enrere.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 20pt \"Arial Black\";")
        self.Enrere.setObjectName("Enrere")
        self.Btn_A = QtWidgets.QPushButton(self.Pag1)
        self.Btn_A.setGeometry(QtCore.QRect(40, 130, 131, 23))
        self.Btn_A.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_A.setObjectName("Btn_A")
        self.stackedWidget.addWidget(self.Pag1)
        self.Pag2 = QtWidgets.QWidget()
        self.Pag2.setObjectName("Pag2")
        self.Titol_2 = QtWidgets.QLabel(self.Pag2)
        self.Titol_2.setGeometry(QtCore.QRect(30, 30, 469, 89))
        self.Titol_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol_2.setObjectName("Titol_2")
        self.Enrere_2 = QtWidgets.QPushButton(self.Pag2)
        self.Enrere_2.setGeometry(QtCore.QRect(180, 670, 151, 21))
        self.Enrere_2.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 10pt \"Arial Black\";")
        self.Enrere_2.setObjectName("Enrere_2")
        self.label = QtWidgets.QLabel(self.Pag2)
        self.label.setGeometry(QtCore.QRect(40, 130, 451, 541))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.Titol_2.raise_()
        self.label.raise_()
        self.Enrere_2.raise_()
        self.stackedWidget.addWidget(self.Pag2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Enrere.clicked.connect(self.openPrincipal)
        self.Btn_A.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.Pag2))
        self.Enrere_2.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.Pag1))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Z.setText(_translate("MainWindow", "Z"))
        self.Btn_Y.setText(_translate("MainWindow", "Y"))
        self.Btn_M.setText(_translate("MainWindow", "M"))
        self.Btn_G.setText(_translate("MainWindow", "G"))
        self.Titol.setText(_translate("MainWindow", "Diccionari de Català"))
        self.Btn_K.setText(_translate("MainWindow", "K"))
        self.Btn_V.setText(_translate("MainWindow", "V"))
        self.Btn_H.setText(_translate("MainWindow", "H"))
        self.Btn_J.setText(_translate("MainWindow", "J"))
        self.Btn_D.setText(_translate("MainWindow", "D"))
        self.Btn_W.setText(_translate("MainWindow", "W"))
        self.Btn_B.setText(_translate("MainWindow", "B"))
        self.Btn_O.setText(_translate("MainWindow", "O"))
        self.Btn_N.setText(_translate("MainWindow", "N"))
        self.Btn_E.setText(_translate("MainWindow", "E"))
        self.Btn_C.setText(_translate("MainWindow", "C"))
        self.Btn_Q.setText(_translate("MainWindow", "Q"))
        self.Btn_T.setText(_translate("MainWindow", "T"))
        self.Btn_P.setText(_translate("MainWindow", "P"))
        self.Btn_I.setText(_translate("MainWindow", "I"))
        self.Btn_S.setText(_translate("MainWindow", "S"))
        self.Btn_F.setText(_translate("MainWindow", "F"))
        self.Btn_L.setText(_translate("MainWindow", "L"))
        self.Btn_X.setText(_translate("MainWindow", "X"))
        self.Btn_U.setText(_translate("MainWindow", "U"))
        self.Btn_R.setText(_translate("MainWindow", "R"))
        self.Enrere.setText(_translate("MainWindow", "Enrere"))
        self.Btn_A.setText(_translate("MainWindow", "A"))
        self.Titol_2.setText(_translate("MainWindow", "Diccionari de Català \n"
"-- Lletra A"))
        self.Enrere_2.setText(_translate("MainWindow", "Enrere"))
        self.label.setText(_translate("MainWindow", "Abalançar\n"
"verb predominal\n"
"\n"
"1. Tirar-se endavant recolzant sobre un \n"
"objecte de manera que el cos faci balança, \n"
"estigui a punt de fer la balançada; \n"
"abocar-se excessivament\n"
"\n"
"2. Fer l’acció de llançar-se contra algú.\n"
"\n"
"Abaltiment\n"
"masculí\n"
"\n"
"1. Estat del qui està abaltit.\n"
"\n"
"Abancalar\n"
"verb transitiu \n"
"\n"
"1. Preparar un terreny erm per conrear-lo\n"
"tot subdividint-lo en bancals.\n"
"\n"
"Abans\n"
"adverbi \n"
"\n"
"1. Denota prioritat en el temps, anterioritat."))

# Pestanya Castellano

class Castellano(object):

    def openPrincipal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Principal()
        self.ui.setupUi(self.window)
        MainWindow.show()
        self.window.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 708)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 521, 691))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Pag1 = QtWidgets.QWidget()
        self.Pag1.setObjectName("Pag1")
        self.Btn_O = QtWidgets.QPushButton(self.Pag1)
        self.Btn_O.setGeometry(QtCore.QRect(40, 270, 131, 23))
        self.Btn_O.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_O.setObjectName("Btn_O")
        self.Btn_F = QtWidgets.QPushButton(self.Pag1)
        self.Btn_F.setGeometry(QtCore.QRect(360, 150, 131, 23))
        self.Btn_F.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_F.setObjectName("Btn_F")
        self.Btn_A = QtWidgets.QPushButton(self.Pag1)
        self.Btn_A.setGeometry(QtCore.QRect(40, 120, 131, 23))
        self.Btn_A.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_A.setObjectName("Btn_A")
        self.Btn_V = QtWidgets.QPushButton(self.Pag1)
        self.Btn_V.setGeometry(QtCore.QRect(200, 330, 131, 21))
        self.Btn_V.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_V.setObjectName("Btn_V")
        self.Btn_C = QtWidgets.QPushButton(self.Pag1)
        self.Btn_C.setGeometry(QtCore.QRect(360, 120, 131, 23))
        self.Btn_C.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_C.setObjectName("Btn_C")
        self.Btn_K = QtWidgets.QPushButton(self.Pag1)
        self.Btn_K.setGeometry(QtCore.QRect(200, 210, 131, 23))
        self.Btn_K.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_K.setObjectName("Btn_K")
        self.Btn_X = QtWidgets.QPushButton(self.Pag1)
        self.Btn_X.setGeometry(QtCore.QRect(40, 360, 131, 23))
        self.Btn_X.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_X.setObjectName("Btn_X")
        self.Btn_E = QtWidgets.QPushButton(self.Pag1)
        self.Btn_E.setGeometry(QtCore.QRect(200, 150, 131, 21))
        self.Btn_E.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_E.setObjectName("Btn_E")
        self.Btn_R = QtWidgets.QPushButton(self.Pag1)
        self.Btn_R.setGeometry(QtCore.QRect(40, 300, 131, 23))
        self.Btn_R.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_R.setObjectName("Btn_R")
        self.Btn_M = QtWidgets.QPushButton(self.Pag1)
        self.Btn_M.setGeometry(QtCore.QRect(40, 240, 131, 23))
        self.Btn_M.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_M.setObjectName("Btn_M")
        self.Btn_I = QtWidgets.QPushButton(self.Pag1)
        self.Btn_I.setGeometry(QtCore.QRect(360, 180, 131, 23))
        self.Btn_I.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_I.setObjectName("Btn_I")
        self.Btn_N = QtWidgets.QPushButton(self.Pag1)
        self.Btn_N.setGeometry(QtCore.QRect(200, 240, 131, 21))
        self.Btn_N.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_N.setObjectName("Btn_N")
        self.Btn_S = QtWidgets.QPushButton(self.Pag1)
        self.Btn_S.setGeometry(QtCore.QRect(200, 300, 131, 23))
        self.Btn_S.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_S.setObjectName("Btn_S")
        self.Btn_U = QtWidgets.QPushButton(self.Pag1)
        self.Btn_U.setGeometry(QtCore.QRect(40, 330, 131, 23))
        self.Btn_U.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_U.setObjectName("Btn_U")
        self.Btn_Y = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Y.setGeometry(QtCore.QRect(200, 360, 131, 23))
        self.Btn_Y.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Y.setObjectName("Btn_Y")
        self.Atras = QtWidgets.QPushButton(self.Pag1)
        self.Atras.setGeometry(QtCore.QRect(140, 640, 251, 41))
        self.Atras.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 20pt \"Arial Black\";")
        self.Atras.setObjectName("Atras")
        self.Btn_J = QtWidgets.QPushButton(self.Pag1)
        self.Btn_J.setGeometry(QtCore.QRect(40, 210, 131, 23))
        self.Btn_J.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_J.setObjectName("Btn_J")
        self.Btn_P = QtWidgets.QPushButton(self.Pag1)
        self.Btn_P.setGeometry(QtCore.QRect(200, 270, 131, 23))
        self.Btn_P.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_P.setObjectName("Btn_P")
        self.Btn_ENYE = QtWidgets.QPushButton(self.Pag1)
        self.Btn_ENYE.setGeometry(QtCore.QRect(360, 240, 131, 23))
        self.Btn_ENYE.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_ENYE.setObjectName("Btn_ENYE")
        self.Btn_T = QtWidgets.QPushButton(self.Pag1)
        self.Btn_T.setGeometry(QtCore.QRect(360, 300, 131, 23))
        self.Btn_T.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_T.setObjectName("Btn_T")
        self.Btn_G = QtWidgets.QPushButton(self.Pag1)
        self.Btn_G.setGeometry(QtCore.QRect(40, 180, 131, 23))
        self.Btn_G.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_G.setObjectName("Btn_G")
        self.Btn_L = QtWidgets.QPushButton(self.Pag1)
        self.Btn_L.setGeometry(QtCore.QRect(360, 210, 131, 23))
        self.Btn_L.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_L.setObjectName("Btn_L")
        self.Btn_Z = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Z.setGeometry(QtCore.QRect(360, 360, 131, 23))
        self.Btn_Z.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Z.setObjectName("Btn_Z")
        self.Btn_B = QtWidgets.QPushButton(self.Pag1)
        self.Btn_B.setGeometry(QtCore.QRect(200, 120, 131, 23))
        self.Btn_B.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_B.setObjectName("Btn_B")
        self.Btn_W = QtWidgets.QPushButton(self.Pag1)
        self.Btn_W.setGeometry(QtCore.QRect(360, 330, 131, 23))
        self.Btn_W.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_W.setObjectName("Btn_W")
        self.Btn_D = QtWidgets.QPushButton(self.Pag1)
        self.Btn_D.setGeometry(QtCore.QRect(40, 150, 131, 23))
        self.Btn_D.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_D.setObjectName("Btn_D")
        self.Btn_H = QtWidgets.QPushButton(self.Pag1)
        self.Btn_H.setGeometry(QtCore.QRect(200, 180, 131, 23))
        self.Btn_H.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_H.setObjectName("Btn_H")
        self.Titol = QtWidgets.QLabel(self.Pag1)
        self.Titol.setGeometry(QtCore.QRect(30, 20, 469, 89))
        self.Titol.setStyleSheet("background-color: rgb(255, 61, 61);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol.setObjectName("Titol")
        self.Btn_Q = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Q.setGeometry(QtCore.QRect(360, 270, 131, 23))
        self.Btn_Q.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Q.setObjectName("Btn_Q")
        self.stackedWidget.addWidget(self.Pag1)
        self.Pag2 = QtWidgets.QWidget()
        self.Pag2.setObjectName("Pag2")
        self.label = QtWidgets.QLabel(self.Pag2)
        self.label.setGeometry(QtCore.QRect(40, 130, 451, 531))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.Titol_2 = QtWidgets.QLabel(self.Pag2)
        self.Titol_2.setGeometry(QtCore.QRect(30, 30, 469, 89))
        self.Titol_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol_2.setObjectName("Titol_2")
        self.Atras_2 = QtWidgets.QPushButton(self.Pag2)
        self.Atras_2.setGeometry(QtCore.QRect(190, 650, 151, 21))
        self.Atras_2.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 10pt \"Arial Black\";")
        self.Atras_2.setObjectName("Atras_2")
        self.stackedWidget.addWidget(self.Pag2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Atras.clicked.connect(self.openPrincipal)
        self.Btn_A.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.Pag2))
        self.Atras_2.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.Pag1))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_O.setText(_translate("MainWindow", "O"))
        self.Btn_F.setText(_translate("MainWindow", "F"))
        self.Btn_A.setText(_translate("MainWindow", "A"))
        self.Btn_V.setText(_translate("MainWindow", "V"))
        self.Btn_C.setText(_translate("MainWindow", "C"))
        self.Btn_K.setText(_translate("MainWindow", "K"))
        self.Btn_X.setText(_translate("MainWindow", "X"))
        self.Btn_E.setText(_translate("MainWindow", "E"))
        self.Btn_R.setText(_translate("MainWindow", "R"))
        self.Btn_M.setText(_translate("MainWindow", "M"))
        self.Btn_I.setText(_translate("MainWindow", "I"))
        self.Btn_N.setText(_translate("MainWindow", "N"))
        self.Btn_S.setText(_translate("MainWindow", "S"))
        self.Btn_U.setText(_translate("MainWindow", "U"))
        self.Btn_Y.setText(_translate("MainWindow", "Y"))
        self.Atras.setText(_translate("MainWindow", "Atrás"))
        self.Btn_J.setText(_translate("MainWindow", "J"))
        self.Btn_P.setText(_translate("MainWindow", "P"))
        self.Btn_ENYE.setText(_translate("MainWindow", "Ñ"))
        self.Btn_T.setText(_translate("MainWindow", "T"))
        self.Btn_G.setText(_translate("MainWindow", "G"))
        self.Btn_L.setText(_translate("MainWindow", "L"))
        self.Btn_Z.setText(_translate("MainWindow", "Z"))
        self.Btn_B.setText(_translate("MainWindow", "B"))
        self.Btn_W.setText(_translate("MainWindow", "W"))
        self.Btn_D.setText(_translate("MainWindow", "D"))
        self.Btn_H.setText(_translate("MainWindow", "H"))
        self.Titol.setText(_translate("MainWindow", "Diccionario de Castellano"))
        self.Btn_Q.setText(_translate("MainWindow", "Q"))
        self.label.setText(_translate("MainWindow", "Abalanzar\n"
"verbo predominal\n"
"\n"
"1. Tirarse adelante apoyando  sobre un \n"
"objeto de manera que el cuerpo haga palança, \n"
"esté a punto de hacer el balanceado.; \n"
"abocar-se excessivament\n"
"\n"
"2. Acción de lanzarse contra alguien.\n"
"\n"
"Adormecimiento\n"
"nombre masculino\n"
"\n"
"1.Estado del que está adormecido.\n"
"\n"
"sin.  amodorramiento"))
        self.Titol_2.setText(_translate("MainWindow", "Diccionario de Castellano \n"
"-- Letra A"))
        self.Atras_2.setText(_translate("MainWindow", "Atrás"))

# Pestanya English

class English(object):

    def openPrincipal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Principal()
        self.ui.setupUi(self.window)
        MainWindow.show()
        self.window.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 708)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 10, 501, 691))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Pag1 = QtWidgets.QWidget()
        self.Pag1.setObjectName("Pag1")
        self.Btn_Q = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Q.setGeometry(QtCore.QRect(180, 270, 131, 23))
        self.Btn_Q.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Q.setObjectName("Btn_Q")
        self.Back = QtWidgets.QPushButton(self.Pag1)
        self.Back.setGeometry(QtCore.QRect(120, 640, 251, 41))
        self.Back.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 20pt \"Arial Black\";")
        self.Back.setObjectName("Back")
        self.Btn_O = QtWidgets.QPushButton(self.Pag1)
        self.Btn_O.setGeometry(QtCore.QRect(340, 240, 131, 23))
        self.Btn_O.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_O.setObjectName("Btn_O")
        self.Btn_T = QtWidgets.QPushButton(self.Pag1)
        self.Btn_T.setGeometry(QtCore.QRect(180, 300, 131, 23))
        self.Btn_T.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_T.setObjectName("Btn_T")
        self.Btn_I = QtWidgets.QPushButton(self.Pag1)
        self.Btn_I.setGeometry(QtCore.QRect(340, 180, 131, 23))
        self.Btn_I.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_I.setObjectName("Btn_I")
        self.Btn_H = QtWidgets.QPushButton(self.Pag1)
        self.Btn_H.setGeometry(QtCore.QRect(180, 180, 131, 23))
        self.Btn_H.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_H.setObjectName("Btn_H")
        self.Btn_P = QtWidgets.QPushButton(self.Pag1)
        self.Btn_P.setGeometry(QtCore.QRect(20, 270, 131, 23))
        self.Btn_P.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_P.setObjectName("Btn_P")
        self.Btn_U = QtWidgets.QPushButton(self.Pag1)
        self.Btn_U.setGeometry(QtCore.QRect(340, 300, 131, 23))
        self.Btn_U.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_U.setObjectName("Btn_U")
        self.Btn_Y = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Y.setGeometry(QtCore.QRect(20, 360, 131, 23))
        self.Btn_Y.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Y.setObjectName("Btn_Y")
        self.Btn_B = QtWidgets.QPushButton(self.Pag1)
        self.Btn_B.setGeometry(QtCore.QRect(180, 120, 131, 23))
        self.Btn_B.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_B.setObjectName("Btn_B")
        self.Btn_L = QtWidgets.QPushButton(self.Pag1)
        self.Btn_L.setGeometry(QtCore.QRect(340, 210, 131, 23))
        self.Btn_L.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_L.setObjectName("Btn_L")
        self.Btn_J = QtWidgets.QPushButton(self.Pag1)
        self.Btn_J.setGeometry(QtCore.QRect(20, 210, 131, 23))
        self.Btn_J.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_J.setObjectName("Btn_J")
        self.Btn_Z = QtWidgets.QPushButton(self.Pag1)
        self.Btn_Z.setGeometry(QtCore.QRect(180, 360, 131, 23))
        self.Btn_Z.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_Z.setObjectName("Btn_Z")
        self.Btn_S = QtWidgets.QPushButton(self.Pag1)
        self.Btn_S.setGeometry(QtCore.QRect(20, 300, 131, 23))
        self.Btn_S.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_S.setObjectName("Btn_S")
        self.Btn_D = QtWidgets.QPushButton(self.Pag1)
        self.Btn_D.setGeometry(QtCore.QRect(20, 150, 131, 23))
        self.Btn_D.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_D.setObjectName("Btn_D")
        self.Btn_F = QtWidgets.QPushButton(self.Pag1)
        self.Btn_F.setGeometry(QtCore.QRect(340, 150, 131, 23))
        self.Btn_F.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_F.setObjectName("Btn_F")
        self.Btn_E = QtWidgets.QPushButton(self.Pag1)
        self.Btn_E.setGeometry(QtCore.QRect(180, 150, 131, 21))
        self.Btn_E.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_E.setObjectName("Btn_E")
        self.Btn_G = QtWidgets.QPushButton(self.Pag1)
        self.Btn_G.setGeometry(QtCore.QRect(20, 180, 131, 23))
        self.Btn_G.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_G.setObjectName("Btn_G")
        self.Btn_W = QtWidgets.QPushButton(self.Pag1)
        self.Btn_W.setGeometry(QtCore.QRect(180, 330, 131, 21))
        self.Btn_W.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_W.setObjectName("Btn_W")
        self.Btn_V = QtWidgets.QPushButton(self.Pag1)
        self.Btn_V.setGeometry(QtCore.QRect(20, 330, 131, 23))
        self.Btn_V.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_V.setObjectName("Btn_V")
        self.Btn_A = QtWidgets.QPushButton(self.Pag1)
        self.Btn_A.setGeometry(QtCore.QRect(20, 120, 131, 23))
        self.Btn_A.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_A.setObjectName("Btn_A")
        self.Btn_R = QtWidgets.QPushButton(self.Pag1)
        self.Btn_R.setGeometry(QtCore.QRect(340, 270, 131, 23))
        self.Btn_R.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_R.setObjectName("Btn_R")
        self.Titol = QtWidgets.QLabel(self.Pag1)
        self.Titol.setGeometry(QtCore.QRect(10, 20, 469, 89))
        self.Titol.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol.setObjectName("Titol")
        self.Btn_C = QtWidgets.QPushButton(self.Pag1)
        self.Btn_C.setGeometry(QtCore.QRect(340, 120, 131, 23))
        self.Btn_C.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_C.setObjectName("Btn_C")
        self.Btn_X = QtWidgets.QPushButton(self.Pag1)
        self.Btn_X.setGeometry(QtCore.QRect(340, 330, 131, 23))
        self.Btn_X.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_X.setObjectName("Btn_X")
        self.Btn_N = QtWidgets.QPushButton(self.Pag1)
        self.Btn_N.setGeometry(QtCore.QRect(180, 240, 131, 21))
        self.Btn_N.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_N.setObjectName("Btn_N")
        self.Btn_K = QtWidgets.QPushButton(self.Pag1)
        self.Btn_K.setGeometry(QtCore.QRect(180, 210, 131, 23))
        self.Btn_K.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_K.setObjectName("Btn_K")
        self.Btn_M = QtWidgets.QPushButton(self.Pag1)
        self.Btn_M.setGeometry(QtCore.QRect(20, 240, 131, 23))
        self.Btn_M.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 87 9pt \"Arial Black\";")
        self.Btn_M.setObjectName("Btn_M")
        self.stackedWidget.addWidget(self.Pag1)
        self.Pag2 = QtWidgets.QWidget()
        self.Pag2.setObjectName("Pag2")
        self.Titol_2 = QtWidgets.QLabel(self.Pag2)
        self.Titol_2.setGeometry(QtCore.QRect(10, 30, 469, 89))
        self.Titol_2.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol_2.setObjectName("Titol_2")
        self.label = QtWidgets.QLabel(self.Pag2)
        self.label.setGeometry(QtCore.QRect(20, 130, 451, 531))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.Back_2 = QtWidgets.QPushButton(self.Pag2)
        self.Back_2.setGeometry(QtCore.QRect(170, 650, 151, 21))
        self.Back_2.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 10pt \"Arial Black\";")
        self.Back_2.setObjectName("Back_2")
        self.stackedWidget.addWidget(self.Pag2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Back.clicked.connect(self.openPrincipal)
        self.Btn_A.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.Pag2))
        self.Back_2.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.Pag1))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Q.setText(_translate("MainWindow", "Q"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.Btn_O.setText(_translate("MainWindow", "O"))
        self.Btn_T.setText(_translate("MainWindow", "T"))
        self.Btn_I.setText(_translate("MainWindow", "I"))
        self.Btn_H.setText(_translate("MainWindow", "H"))
        self.Btn_P.setText(_translate("MainWindow", "P"))
        self.Btn_U.setText(_translate("MainWindow", "U"))
        self.Btn_Y.setText(_translate("MainWindow", "Y"))
        self.Btn_B.setText(_translate("MainWindow", "B"))
        self.Btn_L.setText(_translate("MainWindow", "L"))
        self.Btn_J.setText(_translate("MainWindow", "J"))
        self.Btn_Z.setText(_translate("MainWindow", "Z"))
        self.Btn_S.setText(_translate("MainWindow", "S"))
        self.Btn_D.setText(_translate("MainWindow", "D"))
        self.Btn_F.setText(_translate("MainWindow", "F"))
        self.Btn_E.setText(_translate("MainWindow", "E"))
        self.Btn_G.setText(_translate("MainWindow", "G"))
        self.Btn_W.setText(_translate("MainWindow", "W"))
        self.Btn_V.setText(_translate("MainWindow", "V"))
        self.Btn_A.setText(_translate("MainWindow", "A"))
        self.Btn_R.setText(_translate("MainWindow", "R"))
        self.Titol.setText(_translate("MainWindow", "Dictionary of English"))
        self.Btn_C.setText(_translate("MainWindow", "C"))
        self.Btn_X.setText(_translate("MainWindow", "X"))
        self.Btn_N.setText(_translate("MainWindow", "N"))
        self.Btn_K.setText(_translate("MainWindow", "K"))
        self.Btn_M.setText(_translate("MainWindow", "M"))
        self.Titol_2.setText(_translate("MainWindow", "Dictionary of English \n"
"-- Letter A"))
        self.label.setText(_translate("MainWindow", "Act\n"
"Traducido al castellano como Actuar.\n"
"Verbo intransitivo\n"
"\n"
"1.  Ejercer funciones propias de un oficio o un cargo.\n"
"\n"
"2. Comportarse o proceder de una manera \n"
"determinada. \n"
"\n"
"Account\n"
"Traducido al castellano como Cuenta.\n"
"\n"
"1.  Elemento básico en la contabilidad i servicios\n"
"de pago. \n"
"\n"
"Actor\n"
"Traducido al castellano como Actor\n"
"\n"
"1. Persona dedicada al oficio del espectáculo."))
        self.Back_2.setText(_translate("MainWindow", "Back"))

# Buscador

class Buscador(object):

    def openPrincipal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Principal()
        self.ui.setupUi(self.window)
        MainWindow.show()
        self.window.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 708)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titol_2 = QtWidgets.QLabel(self.centralwidget)
        self.Titol_2.setGeometry(QtCore.QRect(30, 20, 469, 89))
        self.Titol_2.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"background-color: rgb(255, 170, 0);")
        self.Titol_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol_2.setObjectName("Titol_2")
        self.Txt_Buscar = QtWidgets.QTextEdit(self.centralwidget)
        self.Txt_Buscar.setGeometry(QtCore.QRect(30, 120, 391, 21))
        self.Txt_Buscar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Txt_Buscar.setObjectName("Txt_Buscar")
        self.Btn_Buscar = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Buscar.setGeometry(QtCore.QRect(420, 120, 75, 23))
        self.Btn_Buscar.setStyleSheet("background-color: rgb(170, 170, 166);\n"
"font: 87 10pt \"Arial Black\";")
        self.Btn_Buscar.setObjectName("Btn_Buscar")
        self.Txt_Buscado = QtWidgets.QLabel(self.centralwidget)
        self.Txt_Buscado.setGeometry(QtCore.QRect(30, 150, 461, 521))
        self.Txt_Buscado.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.Txt_Buscado.setText("")
        self.Txt_Buscado.setObjectName("Txt_Buscado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Enrere = QtWidgets.QPushButton(self.centralwidget)
        self.Enrere.setGeometry(QtCore.QRect(130, 660, 261, 31))
        self.Enrere.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 14pt \"Arial Black\";")
        self.Enrere.setText("Enrere")
        self.Enrere.setObjectName("Enrere")

        self.Enrere.clicked.connect(self.openPrincipal)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titol_2.setText(_translate("MainWindow", "Buscador"))
        self.Txt_Buscar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Btn_Buscar.setText(_translate("MainWindow", "Buscar"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Principal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


## https://www.learnpyqt.com/tutorials/creating-multiple-windows/
