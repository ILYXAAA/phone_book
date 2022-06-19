import sys
from prog import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.WriteNumb)
        self.ui.pushButton_2.clicked.connect(self.Base)
        self.ui.pushButton_3.clicked.connect(self.FindWord)
        self.ui.pushButton_4.clicked.connect(self.ClearBase)

        self.ui.pushButton_3.setAutoDefault(True)
        self.ui.textEdit_3.returnPressed.connect(self.ui.pushButton_3.click)
        
        self.ui.pushButton.setAutoDefault(True)
        self.ui.textEdit_2.returnPressed.connect(self.ui.pushButton.click)

        self.ui.pushButton.setAutoDefault(True)
        self.ui.textEdit.returnPressed.connect(self.ui.pushButton.click)
        
        self.ui.pushButton_4.setAutoDefault(True)
        self.ui.ClearBaseOk.returnPressed.connect(self.ui.pushButton_4.click)

        self.ui.Base.setReadOnly(True)
        self.ui.textEdit_5.setReadOnly(True)
        self.ui.lineEdit_2.setReadOnly(True)
        self.ui.lineEdit.setReadOnly(True)
        self.ui.lineEdit_3.setReadOnly(True)  

        self.ui.textEdit.setPlaceholderText('Введите имя и фамилию')
        self.ui.textEdit_2.setPlaceholderText('Введите номер телефона')
        self.ui.textEdit_3.setPlaceholderText('Введите данные для поиска')
        self.ui.ClearBaseOk.setPlaceholderText('Для подтверждения введите "Да" и нажмите "Ок"')
        
        
        num=[]
        surn=[]
        self.ui.Base.clear()
        numbers = open('numbers.txt', 'a')
        surnames = open('surnames.txt', 'a')
        with open("numbers.txt", "r") as fin:
            numnum = fin.read()
        for string in numnum.split('\n'):
            num.append(string)
        with open("surnames.txt", "r") as kok:
            sursur = kok.read()
        for stringg in sursur.split('\n'):
            surn.append(stringg)
        if len(num)>1 and len(surn)==len(num):
            for i in range(len(num)-1):
                self.ui.Base.append(str(surn[i])+ ' - ' +str(num[i]))   
        else:
            self.ui.Base.setText('В вашей базе нет номеров.')

    def WriteNumb(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()
        text=self.ui.textEdit.text()
        text2=self.ui.textEdit_2.text()
        if len(text)<1:
            self.ui.lineEdit.setText('!!!')
        if len(text2)<1:
            self.ui.lineEdit_3.setText('!!!')
  
        if len(text)>=1 and len(text2)>=1:
            self.ui.lineEdit.clear()
            self.ui.lineEdit_3.clear()
            numbers = open('numbers.txt', 'a')
            surnames = open('surnames.txt', 'a')
            f=self.ui.textEdit.text()
            surnames.write(f)
            surnames.write('\n')
            g=self.ui.textEdit_2.text()
            numbers.write(g)
            numbers.write('\n')

            num=[]
            with open("numbers.txt", "r") as f:
                numn = f.read()
            for strin in numn.split('\n'):
                num.append(strin)
            if len(num)<2:
                self.ui.Base.clear()

            self.ui.Base.append(str(text)+ ' - ' +str(text2))
            
            self.ui.textEdit_2.clear()
            self.ui.textEdit.clear()
         
            u=(len(num))
            if u==1 or u%10==1:
                if u!=11:
                    self.ui.lineEdit_2.setText('Всего в базе '+ str(u) +' номер')
            else:
                if u==2 or u==3 or u==4 or u%10==2 or u%10==3 or u%10==4:
                    if u!=11:
                        self.ui.lineEdit_2.setText('Всего в базе '+ str(u) +' номера')
                else:
                    self.ui.lineEdit_2.setText('Всего в базе '+ str(u) +' номеров')
        

          
        
 
     
    def Base(self):
        num=[]
        surn=[]
        self.ui.Base.clear()
        with open("numbers.txt", "r") as fin:
            numnum = fin.read()
        for string in numnum.split('\n'):
            num.append(string)
        with open("surnames.txt", "r") as kok:
            sursur = kok.read()
        for stringg in sursur.split('\n'):
            surn.append(stringg)
        if len(num)>1:
            for i in range(len(num)-1):
                self.ui.Base.append(str(surn[i])+ ' - ' +str(num[i]))   
        else:
            self.ui.Base.setText('В вашей базе нет номеров')

    def FindWord(self):
        text3=self.ui.textEdit_3.text()
        self.ui.textEdit_5.clear()
        if len(text3)>=1:
            num=[]
            surn=[]
            with open("numbers.txt", "r") as fin:
                numnum = fin.read()
            for string in numnum.split('\n'):
                num.append(string)
            with open("surnames.txt", "r") as kok:
                sursur = kok.read()
            for stringg in sursur.split('\n'):
                surn.append(stringg)
            text3 = text3.lower()
            g = 0
            for i in range(len(surn)):
                if (surn[i][0:len(text3)]).lower()==text3:
                    self.ui.textEdit_5.append(str(surn[i]) + ' - ' + str(num[i]))
                    g-=1
            for j in range(len(num)):
                if (num[j][0:len(text3)]).lower()==text3:
                    self.ui.textEdit_5.append(str(surn[j]) + ' - ' + str(num[j]))
                    g-=1
            for k in range(len(surn)-1):
                for p in range(len(surn[k])-1):
                    if surn[k][p]==' ':
                        r = surn[k][(p+1):len(surn[k])]
                        for s in range(len(text3)):
                            if str(r[0:(len(text3))].lower())==text3 and surn[k] not in self.ui.textEdit_5.toPlainText():
                                self.ui.textEdit_5.append(str(surn[k]) + ' - ' + str(num[k]))
                                g=g-1
                                break
            if g==0:
                self.ui.textEdit_5.setText('Совпадений не найдено')

        
    def ClearBase(self):
        Ok=self.ui.ClearBaseOk.text()
        Ok = Ok.lower()
        if Ok == 'да':
            open('numbers.txt', 'w').close()
            open('surnames.txt', 'w').close()
            self.ui.ClearBaseOk.clear()
            self.ui.Base.setText('В вашей базе нет номеров')
            self.ui.lineEdit_2.clear()
            self.ui.textEdit_5.clear()
            self.ui.textEdit_3.clear()
            self.ui.textEdit_2.clear()
            self.ui.textEdit.clear()
        
      
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
