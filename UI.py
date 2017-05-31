"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    Sean Habermiller
Description:

"""

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets, QtGui


from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)
        

        self.compute_initial_figure()
       
        #
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        for i in range(0,2):
            self.axes.plot(t+i, s)
            self.axes.set_title('FittingTitle')
            self.axes.set_xlabel('XLabel')
            self.axes.set_ylabel('YLabel')


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every 1/10 seconds with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
        self.axes.set_title('FittingTitle')
        self.axes.set_xlabel('XLabel')
        self.axes.set_ylabel('YLabel')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        w = [random.randint(0, 10) for i in range(4)]
		
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.set_title('FittingTitle')
        self.axes.set_xlabel('XLabel')
        self.axes.set_ylabel('YLabel')
        self.draw()
class ResizeSlider(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(ResizeSlider, self).__init__(parent)
		
        layout = QtWidgets.QVBoxLayout()
		
        self.sl1 = QtWidgets.QSlider(0x1)
        self.sl1.setMinimum(1)
        self.sl1.setMaximum(10)
        self.sl1.setValue(7)
        self.sl1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sl1.setTickInterval(2)
        
        layout.addWidget(self.sl1)
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.width = 400
        self.height = 650
        self.resize(self.width,self.height)
        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.options_menu = QtWidgets.QMenu('&Options', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.options_menu)
		
        self.options_menu.addAction('&Resize', ResizeSlider)
		
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=7, height=6, dpi=80)
        sc1 = MyStaticMplCanvas(self.main_widget, width=7, height=6, dpi=80)
        dc = MyDynamicMplCanvas(self.main_widget, width=7, height=6, dpi=80)
        l.addWidget(sc)
        l.addWidget(sc1)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()
    def size(self):
        QtWidgets.QSlider.size(Qt.Horizontal)	
    def closeEvent(self, ce):
        self.fileQuit()
    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """# Ground Control Software
								

This software is intended to remotely communicate with and control the 
avionics on the Atlantis-I rocket, developped in 2016/2017 by the Student
Organisation for Aerospace Research (SOAR). The software listens for data from
a downlink from the rocket, saving all data locally to corresponding files as
a backup from the rocket. Additionally, data from the rocket is plotted and 
analysed in real time as data is received.

# License

This software is provided without a warrantee of any kind. For permission
to use this software outside of the club, please contact SOAR at the University
of Calgary through one of the following methods:

SOAR:
    Email: soar@ucalgary.ca
    
Developer:
    Email: nathan.meulenbroek@ucalgary.ca
           4nathan@outlook.com"""
                                )

def __init__():
    qApp = QtWidgets.QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
    #qApp.exec_()
    return

if __name__=='__main__':
    __init__()