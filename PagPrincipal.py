# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PagPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 708)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Cat = QtWidgets.QPushButton(self.centralwidget)
        self.Cat.setGeometry(QtCore.QRect(50, 130, 421, 91))
        self.Cat.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 127);")
        self.Cat.setObjectName("Cat")
        self.Esp = QtWidgets.QPushButton(self.centralwidget)
        self.Esp.setGeometry(QtCore.QRect(50, 240, 421, 91))
        self.Esp.setStyleSheet("background-color: rgb(255, 61, 61);\n"
"font: 87 20pt \"Arial Black\";")
        self.Esp.setObjectName("Esp")
        self.Eng = QtWidgets.QPushButton(self.centralwidget)
        self.Eng.setGeometry(QtCore.QRect(50, 350, 421, 91))
        self.Eng.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.Eng.setObjectName("Eng")
        self.Buscador = QtWidgets.QPushButton(self.centralwidget)
        self.Buscador.setGeometry(QtCore.QRect(50, 460, 421, 91))
        self.Buscador.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 87 20pt \"Arial Black\";")
        self.Buscador.setObjectName("Buscador")
        self.Titol = QtWidgets.QLabel(self.centralwidget)
        self.Titol.setGeometry(QtCore.QRect(30, 30, 461, 89))
        self.Titol.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"font: 87 20pt \"Arial Black\";")
        self.Titol.setAlignment(QtCore.Qt.AlignCenter)
        self.Titol.setObjectName("Titol")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
