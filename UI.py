"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
	Sean Habermiller
	Ilyes Kabouch
    
Description:

"""

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets


from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import main

progname = os.path.basename('SOAR I Ground Control System')
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
    title = ''
    xlabel = ''
    ylabel = ''
	
    def __init__(self, *args, **kwargs):
        self.title = args[1]
        self.xlabel = args[2]
        self.ylabel = args[3] 

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        
        for i in range(0,2):
            self.axes.plot(t+i, s)
            self.axes.set_title(self.title)
            self.axes.set_xlabel(self.xlabel)
            self.axes.set_ylabel(self.ylabel)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every 1/10 seconds with a new plot."""
    title = ''
    xlabel = ''
    ylabel = ''
	
    def __init__(self, *args, **kwargs):
        self.title = args[1]
        self.xlabel = args[2]
        self.ylabel = args[3] 

        args = [args[0]]
        MyMplCanvas.__init__(self, *args, **kwargs)


    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4])
        self.axes.set_title(self.title)
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
		
        self.axes.plot([0, 1, 2, 3], l)
        self.axes.set_title(self.title)
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)
        self.draw()
<<<<<<< HEAD
class MyTextBox(QtWidgets.QLabel):
    def __init__(self, parent = None):
        super(MyTextBox,self).__init__(parent)
        self.Layout()
        self.setlayout()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Layout)
        timer.start(100)
    def Layout(self):
        a = random.randint(0,10)
        b = random.randint(0,10)
        c = random.randint(0,10)
        d = random.randint(0,10)
        l1 = "Temperature: "+str(a)
        l2 = "RPM: "+str(b)
        l3 = "Longitude: "+str(c)
        l4 = "Latitude: "+str(d)
        lay = QtWidgets.QGridLayout()
        Temp = QtWidgets.QLabel()
        RPM = QtWidgets.QLabel()
        Lon = QtWidgets.QLabel()
        Lat = QtWidgets.QLabel()
        Temp.setText(l1)
        RPM.setText(l2)
        Lon.setText(l3)
        Lat.setText(l4)
        Temp.setAlignment(QtCore.Qt.AlignCenter)
        RPM.setAlignment(QtCore.Qt.AlignCenter)
        Lon.setAlignment(QtCore.Qt.AlignCenter)
        Lat.setAlignment(QtCore.Qt.AlignCenter)
        lay.addWidget(Temp,0,0)
        lay.addWidget(RPM,1,0)
        lay.addWidget(Lon,2,0)
        lay.addWidget(Lat,3,0)
        return(lay)
    def setlayout(self):
        lay = self.Layout()
        self.setLayout(lay)

=======
        
>>>>>>> origin/master
class ResizeSlider(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(ResizeSlider,self).__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        
		
        self.sl1 = QtWidgets.QSlider()
        self.sl1.setMinimum(1)
        self.sl1.setMaximum(10)
        self.sl1.setValue(7)
        self.sl1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sl1.setTickInterval(2)
        
        layout.addWidget(self.sl1)
        self.setWindowTitle("Resize Window")       
        
class ApplicationWindow(QtWidgets.QMainWindow):
    altitude = None
    acceleration = None
    gyro = None
    IMU = None
    diode = None
    
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.width = 1000
        self.height = 900
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

<<<<<<< HEAD
        l = QtWidgets.QGridLayout(self.main_widget)
        Altitude = MyDynamicMplCanvas(self.main_widget,'Altitude','Time(s)','Height(m)')
        Acceleration = MyDynamicMplCanvas(self.main_widget,'Acceleration','Time','Acceleration')
        Gyro = MyDynamicMplCanvas(self.main_widget,'Gyro','X','Y')
        IMU = MyDynamicMplCanvas(self.main_widget,'IMU','X','Y')
        Diode = MyDynamicMplCanvas(self.main_widget,'Diode','X','Y')
        l.addWidget(Altitude,0,0)
        l.addWidget(Acceleration,0,1)
        l.addWidget(Gyro,0,2)
        l.addWidget(IMU,1,0)
        l.addWidget(Diode,1,1)
        l.addWidget(MyTextBox(),1,2)
=======
        wrapper = QtWidgets.QGridLayout(self.main_widget)
        altitude = MyDynamicMplCanvas(self.main_widget,'Altitude',
                                      'Time (s)','Height (m)')
        acceleration = MyDynamicMplCanvas(self.main_widget,'Acceleration',
                                          'Time (s)','Acceleration $(m/s^2)$')
        gyro = MyDynamicMplCanvas(self.main_widget,'Gyro','Time (s)',
                                  'Acceleration $(m/s^2)$')
        IMU = MyDynamicMplCanvas(self.main_widget,'IMU','Time (s)',
                                 'Angle from True (CentiDegrees)')
        diode = MyDynamicMplCanvas(self.main_widget,'Diode','Time (s)',
                                   'Voltage (V)')
        
        wrapper.addWidget(altitude,0,0)
        wrapper.addWidget(acceleration,0,1)
        wrapper.addWidget(gyro,0,2)
        wrapper.addWidget(IMU,1,0)
        wrapper.addWidget(diode,1,1)
>>>>>>> origin/master

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 1000)
        
        loop = main.Main(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(loop.main())
        timer.start(100)

    def fileQuit(self):
        self.close()	
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
           4nathan@outlook.com""")

        
		
def __init__():
    qApp = QtWidgets.QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
    #qApp.exec_()
    return aw

if __name__=='__main__':
    __init__()