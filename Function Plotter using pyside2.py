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
        self.axes.set_ylabel('Y')
        self.axes.set_xlabel('X')
        self.axes.set_title('Function Plot')
        super(MplCanvas, self).__init__(fig)
def mysecond(e,s):
        # here is the second window which the plotting will present itself.
        mydialog=QDialog()
        mydialog.setModal(True)
        sc = MplCanvas(w, width=5, height=3, dpi=100)
        sc.axes.plot(s, e)
        w.setCentralWidget(sc)
        mydialog.exec_()
        
def initUI(j):
        # it's function to provide a waring to any predictable errors.
        w.title = 'Error Message'
        w.left = 10
        w.top = -10
        w.width = 320
        w.height = 200
        w.setWindowTitle(w.title)
        w.setGeometry(w.left, w.top, w.width, w.height)

        buttonReply = QMessageBox.question(w, 'Error message', "{} continue?".format(j), QMessageBox.Ok)
        w.show() 
        app.quit         
def plot():
    val= w.lineEdit.text()
    try:
        max_ = float(w.lineEdit_2.text())
        min_= float(w.lineEdit_3.text())
    except ValueError:
        initUI('Use proper values for max and min ')
    the_allowed_words={'sin','cos','exp','sqrt','^','x'}
    # we will try to find string x 
    for x in re.findall('[a-zA-Z_]+', val):
        if x not in the_allowed_words:
            initUI('you can\'t use this {} Try another one'.format(x))
            pass
        # we will see if the maximum and the minmum values are intact.    
    if min_ >= max_ or max_ <min_ :
        initUI('Use proper max and min values')
        pass
            # we will make a function range.
    func_range = np.linspace(min_,max_,101)
    s=list(func_range)
    replacements= {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',}
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
                    val1 = val1.replace(x, '({})'.format(str(s[i])))
                val1 = val1.replace("_", "exp")
        else:     
            for x in re.findall('[x]+', val):
                val1 = val.replace(x,'({})'.format(str(s[i])))   
        try:
            y.append(eval(val1))
        except ZeroDivisionError :
            y.append(np.nan)
    val1=val 
         # the plot will show in other window.   
    mysecond(y,s)
def clickme_2():
        # It's the cancel button
        app.quit()        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QUiLoader().load("C:\\Users\OWNER\Downloads\submit udacity\Design.ui")
    w.pushButton.clicked.connect(plot)
    w.pushButton_2.clicked.connect(clickme_2)
    w.show()
    sys.exit(app.exec_())
