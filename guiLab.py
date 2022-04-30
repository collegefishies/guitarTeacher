from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
from random import randint

class classPlotter(QMainWindow):
	def __init__(self):
		super(classPlotter,self).__init__()

		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)

		self.x = list(range(100))
		self.y = [randint(0,100) for _ in range(100)]

		pen = pg.mkPen(color=(255,0,0))
		self.data_line = self.graphWidget.plot(self.x,self.y, pen=pen)