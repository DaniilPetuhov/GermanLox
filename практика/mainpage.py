# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glav.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainpage(object):
    def setupUi(self, mainpage):
        mainpage.setObjectName("mainpage")
        mainpage.resize(1058, 712)
        mainpage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        mainpage.setStyleSheet("\n"
"\n"
"*\n"
"{\n"
"font-family: century gothic;\n"
"font-size:14px;\n"
"color:white;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"background: url(:/картинки/картинки/univ.jpg);\n"
"background-size: cover;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background: transparent;\n"
"border: none;\n"
"color: #717072;\n"
"border-bottom: 1px solid #717072;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background: steelblue;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background: teal;\n"
"border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mainpage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 1101, 61))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size:24px\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 120, 461, 511))
        self.listWidget.setStyleSheet("QFrame\n"
"{\n"
"background: white;\n"
"border-radius:15px;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 640, 149, 38))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size:24px;\n"
"color:white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 231, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size:24px\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(530, 120, 261, 271))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background:#333;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background: red;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background: darkred;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 241, 20))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 241, 20))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton \n"
"{\n"
"border-radius: 10px;\n"
"}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 220, 121, 27))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size:24px\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 636, 91, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton \n"
"{\n"
"border-radius: 10px;\n"
"background-color: red;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background: darkred;\n"
"border-radius:15px;\n"
"}")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        mainpage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainpage)
        self.statusbar.setObjectName("statusbar")
        mainpage.setStatusBar(self.statusbar)

        self.retranslateUi(mainpage)
        QtCore.QMetaObject.connectSlotsByName(mainpage)

    def retranslateUi(self, mainpage):
        _translate = QtCore.QCoreApplication.translate
        mainpage.setWindowTitle(_translate("mainpage", "MainWindow"))
        self.label_3.setText(_translate("mainpage", "Орловский государственный университет имени И.С. Тургенева"))
        self.pushButton_3.setText(_translate("mainpage", "Подробнее"))
        self.label_4.setText(_translate("mainpage", "Конференции"))
        self.lineEdit.setText(_translate("mainpage", "Логин"))
        self.lineEdit_2.setText(_translate("mainpage", "Пароль"))
        self.pushButton.setText(_translate("mainpage", "Войти"))
        self.pushButton_2.setText(_translate("mainpage", "Регистрация"))
        self.label_5.setText(_translate("mainpage", "Авторизация"))
        self.pushButton_4.setText(_translate("mainpage", "Выйти"))
import resource_rc
