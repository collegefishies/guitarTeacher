import sys
from guiLab import *
import PyQt5
from PyQt5.QtWidgets import *
import sounddevice as sd
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from functools import partial #controller library

class guitarModel():
	device = None

	def saveDevice(self, dev):
		self.device = dev
		print(dev)

class guitarMainWindow(QMainWindow):
	def __init__(self, model):
		self.model = model
		super(guitarMainWindow,self).__init__()
		#define primitive widgets
		self.setGeometry(100,100,400,300)
		self.mainPage = QWidget()
		self.mainLayout = QVBoxLayout()
		self.mainPage.setLayout(self.mainLayout)
		self.setCentralWidget(self.mainPage)
		#make gui elements
		self._addToolBar()
		self._addPlotter()
		#start up code
		self._updateTitle()

	def _updateTitle(self):
		self.setWindowTitle('Guitar Tab Player')

	def _addToolBar(self):
		self.menuBar = self.menuBar()
		#file menu
		fileMenu = self.menuBar.addMenu("&Open Tab")
		action = QAction("Import MusicXML...", self)
		fileMenu.addAction(action)
		action.triggered.connect(partial(self.openFile, 'Import MusicXML...', 'MusicXML (*.xml *.musicxml *.mxl);; All Files (*.*)'))
		#devicesmenu
		deviceMenu = self.menuBar.addMenu("&Audio Input")
		self.devices = sd.query_devices()
		for device in self.devices:
			action = QAction(device['name'], self) 
			deviceMenu.addAction(action)
			action.triggered.connect(partial(self.model.saveDevice, device))

	def _addPlotter(self):
		self.graphWidget = pg.PlotWidget()
		self.mainLayout.addWidget(self.graphWidget)
	def openFile(self, title, file_ext):
		filename, _ = QFileDialog.getOpenFileName(self,title,'',file_ext)
		self.filename = filename

def main():
	app = QApplication(sys.argv)
	model = guitarModel()
	window = guitarMainWindow(model)
	# window = classPlotter()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()