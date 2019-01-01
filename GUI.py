import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Tic Tac Toe")



def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()