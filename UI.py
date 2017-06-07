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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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
        pass


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

    def update_figure(self, array):
        self.axes.plot(array)
        self.axes.set_title(self.title)
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)
        self.draw()

class MyTextBox(QtWidgets.QLabel):
    lay = QtWidgets.QGridLayout()
    temperature = None
    lon = None
    lat = None
    
    def __init__(self, parent = None):
        super(MyTextBox,self).__init__(parent)
        self.computeInitialLayout()
        return
        
    def computeInitialLayout(self):
        a = random.randint(0,10)
        c = random.randint(0,10)
        d = random.randint(0,10)
        
        l1 = "Temperature: "+str(a)
        l3 = "Longitude: "+str(c)
        l4 = "Latitude: "+str(d)
        
        self.temperature = QtWidgets.QLabel()
        self.lon = QtWidgets.QLabel()
        self.lat = QtWidgets.QLabel()
        
        self.temperature.setText(l1)
        self.lon.setText(l3)
        self.lat.setText(l4)
        
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.lon.setAlignment(QtCore.Qt.AlignCenter)
        self.lat.setAlignment(QtCore.Qt.AlignCenter)
        
        self.lay.addWidget(self.temperature,0,0)
        self.lay.addWidget(self.lon,1,0)
        self.lay.addWidget(self.lat,1,1)
        
        self.setLayout(self.lay)
        return 
        
    def updateText(self):
        self.temperature.setText("Temperature: "+str(random.randint(0,10)))
        self.lon.setText("Longitude: "+str(random.randint(0,10)))
        self.lat.setText("Latitude: "+str(random.randint(0,10)))
        return
        
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
    wrapper = None
    altitude = None
    acceleration = None
    gyro = None
    IMU = None
    diode = None
    text_boxes = None
    
    
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
        self.wrapper = QtWidgets.QGridLayout(self.main_widget)

        self.altitude = MyDynamicMplCanvas(self.main_widget,'Altitude','Time (s)','Height (m)')
        self.acceleration = MyDynamicMplCanvas(self.main_widget,'Acceleration','Time (s)','Acceleration $(m/s^2)$')
        self.gyro = MyDynamicMplCanvas(self.main_widget,'Gyro','Time (s)','Acceleration $(m/s^2)$')
        self.IMU = MyDynamicMplCanvas(self.main_widget,'IMU','Time (s)','Angle from True (CentiDegrees)')
        self.diode = MyDynamicMplCanvas(self.main_widget,'Diode','Time (s)','Voltage (V)')
        self.text_boxes = MyTextBox(self.main_widget) 

        self.wrapper.addWidget(self.altitude,0,0)
        self.wrapper.addWidget(self.acceleration,0,1)
        self.wrapper.addWidget(self.gyro,1,1)
        self.wrapper.addWidget(self.IMU,1,0)
        self.wrapper.addWidget(self.diode,0,2)
        self.wrapper.addWidget(self.text_boxes,1,2)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        

        return

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
    
    return aw, qApp

if __name__=='__main__':
    aw, qApp = __init__()
    sys.exit(qApp.exec_())

