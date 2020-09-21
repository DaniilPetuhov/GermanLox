import sys
import codecs
import easygui
import tkinter
import tkinter.messagebox
import re
import random
import docx
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from mainpage import Ui_mainpage
from howreg import Ui_howreg
from exitaccept import Ui_exitaccept
from registration import Ui_Form
from regi import Ui_Form1

app = QtWidgets.QApplication(sys.argv)

mainpage = QtWidgets.QMainWindow()
ui = Ui_mainpage()
ui.setupUi(mainpage)
mainpage.showFullScreen()

def exit():
    global exitaccept
    exitaccept = QtWidgets.QDialog()
    ui = Ui_exitaccept()
    ui.setupUi(exitaccept)
    exitaccept.show()

    def exitapp():
        sys.exit(app.exec_())
    ui.pushButton_4.clicked.connect(exitapp)
    def dontexitapp():
        exitaccept.close()
    ui.pushButton_5.clicked.connect(dontexitapp)

def openHowReg():
    global howreg
    howreg = QtWidgets.QDialog()
    ui = Ui_howreg()
    ui.setupUi(howreg)
    #mainpage.close() если надо закрыть mainpage
    howreg.show()




    def closehowreg():
        howreg.close()
    ui.pushButton_2.clicked.connect(closehowreg)

    def openuchastnik():
        global Form1
        Form1 = QtWidgets.QWidget()
        ui = Ui_Form1()
        ui.setupUi(Form1)
        Form1.show()
        howreg.close()

        def savedannie(self):
            os.chdir(r"C:/Users/petuh/Desktop/Программа/Участники")
            os.mkdir(str(self.lineEdit_4.text())+' '+str(self.lineEdit_5.text())+' '+str(self.lineEdit_6.text()))
            os.chdir(r"C:/Users/petuh/Desktop/Программа/Участники"+"/{}".format(str(self.lineEdit_4.text())+' '+str(self.lineEdit_5.text())+' '+str(self.lineEdit_6.text())))

            createfile=open('Данные.txt','a+')
            createfile.write(self.lineEdit_21.text()+'\n'+self.lineEdit_20.text()+'\n')
            createfile.close()
            createfile=open('Данные.txt','a+')
            createfile.write(self.lineEdit_4.text()+'\n'+self.lineEdit_5.text()+'\n'+self.lineEdit_6.text()+'\n'+self.lineEdit_3.text()+'\n'+self.lineEdit.text()+'\n'+self.lineEdit_2.text()+'\n')
            createfile.close()

            os.chdir(r"C:/Users/petuh/Desktop/Программа/Пароли")
            file=open('Данные.txt','a+')
            file.write(self.lineEdit_21.text()+'\n')
            file.close()
            file=open('Данные.txt','a+')
            file.write(self.lineEdit_20.text()+'\n')
            file.close()
            window = Tk()
            window.withdraw()
            tkinter.messagebox.showinfo('Оповещение','Информация сохранена')


        def savedannie1(self):
            os.chdir(r"C:/Users/petuh/Desktop/Программа/Участники"+"/{}".format(str(self.lineEdit_4.text())+' '+str(self.lineEdit_5.text())+' '+str(self.lineEdit_6.text())))

            createfile=open('Данные.txt','a+')
            createfile.write(self.comboBox_6.currentText()+'\n'+self.comboBox_3.currentText()+'\n'+self.lineEdit_14.text()+'\n'+self.comboBox_2.currentText()+'\n'+self.comboBox_4.currentText()+'\n')
            createfile.close()
            window = Tk()
            window.withdraw()
            tkinter.messagebox.showinfo('Оповещение','Информация сохранена')

        def savekod(self):
            os.chdir(r"C:/Users/petuh/Desktop/Программа/Участники"+"/{}".format(str(self.lineEdit_4.text())+' '+str(self.lineEdit_5.text())+' '+str(self.lineEdit_6.text())))

            createfile=open('Данные.txt','a+')
            createfile.write(self.comboBox_5.currentText()+'\n')
            createfile.close()
            window = Tk()
            window.withdraw()
            tkinter.messagebox.showinfo('Оповещение','Дополнительный код классификатора сохранен')


        def savedannie2(self):
            os.chdir(r"C:/Users/petuh/Desktop/Программа/Участники"+"/{}".format(str(self.lineEdit_4.text())+' '+str(self.lineEdit_5.text())+' '+str(self.lineEdit_6.text())))

            createfile=open('Данные.txt','a+')
            createfile.write(self.comboBox.currentText()+'\n'+self.lineEdit_18.text()+'\n'+self.lineEdit_19.text()+'\n')
            createfile.close()
            window = Tk()
            window.withdraw()
            tkinter.messagebox.showinfo('Оповещение','Информация сохранена')

        
    ui.pushButton_4.clicked.connect(openuchastnik)

    def openexpert():
        global Form
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        howreg.close()

        def knopka(self):
            # os.chdir(r"D:\Рабочий стол\КУРСОВАЯ БЕТА\КУРСАЧПРОГ\файлы с данными\Эксперты"+"\{}".format(str(self.lineEdit_5.text())+' '+str(self.lineEdit_4.text())))
            # createfile = open('RABOTA.txt','w')
            # createfile.write(self.lineEdit_8.text()+'\n'+self.lineEdit_7.text()+'\n'+self.lineEdit.text()+'\n'+self.textEdit_2.toPlainText()+'\n'+self.textEdit_3.toPlainText()+'\n'+self.textEdit_4.toPlainText()+'\n'+self.lineEdit_16.text()+'\n'+self.lineEdit_17.text()+'\n'+self.lineEdit_18.text()+'\n'+self.lineEdit_19.text()+'\n'+self.lineEdit_9.text()+'\n'+self.lineEdit_10.text()+'\n'+self.lineEdit_11.text()+'\n'+self.lineEdit_12.text()+'\n'+self.lineEdit_13.text()+'\n'+self.lineEdit_14.text()+'\n'+self.lineEdit_15.text()+'\n')
            # createfile.close()

            doc= docx.Document(easygui.fileopenbox(filetypes=["*.docx"]))
            text = []
            for paragraph in doc.paragraphs:
                text.append(paragraph.text)
                poisk=' '.join(text)
                textkluchsplit = poisk.split()
                punctuation=re.sub(r'[^A-Za-z0-9а-яА-Я]+',' ',str(textkluchsplit))
                punctuation2=re.sub(r'\b\w{1,3}\b', ' ', punctuation)
                FINALTEKST = punctuation2.lower()
            print(FINALTEKST)

            os.chdir(r'D:\Рабочий стол\КУРСОВАЯ БЕТА\КУРСАЧПРОГ\файлы с данными\Эксперты'+"\{}".format(str(self.lineEdit_5.text())+' '+str(self.lineEdit_4.text())))
            createfile=open('СТАТЬЯ.txt','a+')
            createfile.write(str(FINALTEKST))
            createfile.close()

        def savedannie(self):
            os.chdir(r"D:\Рабочий стол\КУРСОВАЯ БЕТА\КУРСАЧПРОГ\файлы с данными\Эксперты")
            os.mkdir(str(self.lineEdit_5.text())+' '+str(self.lineEdit_4.text()))
            os.chdir(r"D:\Рабочий стол\КУРСОВАЯ БЕТА\КУРСАЧПРОГ\файлы с данными\Эксперты"+"\{}".format(str(self.lineEdit_5.text())+' '+str(self.lineEdit_4.text())))
            os.mkdir("СТАТЬИ")

            createfile=open('LOGIN.txt','w')
            createfile.write(self.lineEdit_21.text()+'\n'+self.lineEdit_20.text()+'\n')
            createfile.close()
            createfile=open('FIO.txt','w')
            createfile.write(self.lineEdit_4.text()+'\n'+self.lineEdit_5.text()+'\n'+self.lineEdit_6.text()+'\n'+self.lineEdit.text()+'\n'+self.lineEdit_2.text()+'\n'+self.lineEdit_3.text())
            createfile.close()

            os.chdir(r"D:\Рабочий стол\КУРСОВАЯ БЕТА\КУРСАЧПРОГ\файлы с данными\Пароли")
            file=open('LOGIN.txt','a+')
            file.write(self.lineEdit_21.text()+'\n')
            file.close()
            file=open('PAROL.txt','a+')
            file.write(self.lineEdit_20.text()+'\n')
            file.close()

    ui.pushButton_5.clicked.connect(openexpert)

def login():
    pass

def moreinfo():
    pass


ui.pushButton_2.clicked.connect(openHowReg)

ui.pushButton.clicked.connect(login)

ui.pushButton_3.clicked.connect(moreinfo)

ui.pushButton_4.clicked.connect(exit)

sys.exit(app.exec_())
