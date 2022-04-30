from PyQt5 import QtCore
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

		self.timer = QtCore.QTimer()
		self.timer.setInterval(16)
		self.timer.timeout.connect(self.update_plot_data)
		self.timer.start()

	def update_plot_data(self):
		self.x = self.x[1:]
		self.x.append(self.x[-1] + 1)

		self.y = self.y[1:]
		self.y.append(randint(0,100))

		self.data_line.setData(self.x,self.y)