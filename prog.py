# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 600, 281, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Base = QtWidgets.QTextEdit(self.centralwidget)
        self.Base.setGeometry(QtCore.QRect(10, 10, 281, 581))
        self.Base.setObjectName("Base")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(300, 10, 681, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 80, 231, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 160, 231, 161))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 125, 621, 31))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 631, 71))
        self.label_3.setScaledContents(False)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 80, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 631, 51))
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 170, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 130, 371, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 191, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QLineEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 371, 31))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(380, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ClearBaseOk = QtWidgets.QLineEdit(self.tab_3)
        self.ClearBaseOk.setGeometry(QtCore.QRect(10, 90, 451, 31))
        self.ClearBaseOk.setObjectName("ClearBaseOk")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 641, 51))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 90, 51, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhoneBook"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить базу контактов"))
        self.label_5.setText(_translate("MainWindow", "Номера по вашему запросу:"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Поиск по имени или номеру</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Поиск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Поиск"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Запись в телефонную книгу</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Записать в базу"))
        self.lineEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Запись "))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Очистить базу контактов<br/></span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Ок"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Очистка"))
