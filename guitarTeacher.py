import sys
import PyQt5
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from guiLab import *

class guitarMainWindow(QMainWindow):

	def __init__(self):
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
		self.updateTitle()

	def updateTitle(self):
		self.setWindowTitle('Guitar Tab Player')

	def _addToolBar(self):
		self.menuBar = self.menuBar()
		fileMenu = self.menuBar.addMenu("&File")
		pass
	def _addPlotter(self):
		self.graphWidget = pg.PlotWidget()
		self.mainLayout.addWidget(self.graphWidget)

		pass
def main():
	app = QApplication(sys.argv)
	# window = guitarMainWindow()
	window = classPlotter()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()