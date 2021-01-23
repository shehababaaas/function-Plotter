# Shehab Eldin Tarek Master Micro
# First we will import all libraries we will need
import sys
from typing import Text
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import QLine
from PySide2.QtGui import QWindow, QWindowStateChangeEvent
import matplotlib
from matplotlib import figure
matplotlib.use('Qt5Agg')
import re 
import numpy as np 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import time
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit
from PySide2.QtCore import QFile, QObject
# we will define classes for plotting
class MplCanvas(FigureCanvasQTAgg):
    # we will insert suitable figure
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
class Form(QObject):
    
    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile('C:\\Users\OWNER\Downloads\submit udacity\Design.ui')
        ui_file.open(QFile.ReadOnly)
        
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        btn = self.window.findChild(QPushButton, 'pushButton')
        btn_1 = self.window.findChild(QPushButton, 'pushButton_2')
        btn.clicked.connect(self.clickme)
        btn_1.clicked.connect(self.clickme_2)
        
        
        self.window.show()
    def mysecond(self,e,s):
        # here is the second window which the plotting will present itself.
        mydialog=QDialog()
        mydialog.setModal(True)
        sc = MplCanvas(self, width=5, height=3, dpi=100)
        sc.axes.plot(s, e)
        self.setCentralWidget(sc)
        self.show()
        mydialog.exec()
        time.sleep(1.5)
        self.__init__()
    def initUI(self,j):
        # it's function to provide a waring to any predictable errors.
        self.title = 'Error Message'
        self.left = 10
        self.top = -10
        self.width = 320
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, 'Error message', "{} continue?".format(j), QMessageBox.Ok)
        self.show()
        if buttonReply == QMessageBox.Ok:
            self.__init__()
            app.quit()
    def clickme_2(self):
        # It's the cancel button
        app.quit()         
    def clickme(self):
        # Here is our main code.
        # we will take input from the user. and the maximum and the minimum numbers.
        val = self.lineEdit.text()
        try:
            max_ = float(self.lineEdit_2.text())
            min_= float(self.lineEdit_3.text())
        except ValueError:
            self.initUI('Use proper values for max and min ')
        the_allowed_words={'sin','cos','exp','sqrt','^','x'}
    # we will try to find string x 
        for x in re.findall('[a-zA-Z_]+', val):
            if x not in the_allowed_words:
                self.initUI('you can\'t use this {} Try another one'.format(x))
                pass
        # we will see if the maximum and the minmum values are intact.    
        if min_ >= max_ or max_ <min_ :
            self.initUI('Use proper max and min values')
            pass
            # we will make a function range.
        func_range = np.linspace(min_,max_,101)
        s=list(func_range)
        replacements= {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}
# we will replace the forms from user to actual code in order to use 
        for old, new in replacements.items():
            val = val.replace(old, new)
        val1=val
        y=[]
        # We try to have y values from the input function. 
        for i in range(len(s)):
            if 'exp' in val1:
                for i1 in re.findall('exp+', val1):
                    val1 = val1.replace(i1, "_")
                    for x in re.findall('[x]+', val1):
                        val1 = val1.replace(x, str(s[i]))
                    val1 = val1.replace("_", "exp")
            else:     
                for x in re.findall('[x]+', val):
                    val1 = val.replace(x, str(s[i]))   
            try:
                y.append(eval(val1))
            except ZeroDivisionError :
                y.append(np.nan)
            val1=val 
         # the plot will show in other window.   
        self.mysecond(y,s)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('mainwindow.ui')
    sys.exit(app.exec_())
