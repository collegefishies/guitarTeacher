import sys
import PyQt5
from PyQt5.QtWidgets import *

class guitarMainWindow(QMainWindow):

	def __init__(self):
		super(guitarMainWindow,self).__init__()
		#define primitive widgets
		self.setGeometry(100,100,400,300)
		self.mainPage = QWidget()
		self.mainLayout = QVBoxLayout()
		self.mainPage.setLayout(self.mainLayout)
		self.setCentralWidget(self.mainPage)

		#start up code
		self.updateTitle()
		
	def updateTitle(self):
		self.setWindowTitle('Guitar Tab Player')

	def _addToolBar(self):
		pass

def main():
	app = QApplication(sys.argv)
	window = guitarMainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()