import time
import os.path
from openpyxl import Workbook
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

Ui_Form = uic.loadUiType("mf2_win.ui")[0]

class MyWindow(QtWidgets.QMainWindow, Ui_Form):

    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("공지 사항 IP 변환기")
        self.pushButton.clicked.connect(self.fileopen)


    def fileopen(self):
        global filename
        global f
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.path.expanduser("~/Downloads"))
        if filename[0]:
            f = open(filename[0], 'r')
           

            ## wb= openpyxl.Workbook()  ===>  import openpyxl
            wb = Workbook()  # from openpyxl import Workbook
            sheet = wb.active
            sheet['A1'] = 'ZONE'
            sheet['B1'] = '호스트이름'
            sheet['C1'] = 'IP'

            while True:
                line=f.readline()
                if not line: break
                a = line.split("|")
                data = "상위기관"+time.strftime('%y%m%d',time.localtime(time.time()))+"_"+a[1]
                sheet.append(['E',data,a[1]])

            wb.save(os.path.expanduser("~/Downloads/deny.xlsx"))
            f.close()
        

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) 
    myWindow = MyWindow() 
    myWindow.show()
    app.exec_()
