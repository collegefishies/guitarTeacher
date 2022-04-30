import sys
import PyQt5
from PyQt5.QtWidgets import *

class guitarMainWindow(QWidget):
	pass

def main():
	app = QApplication(sys.argv)
	window = guitarMainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()