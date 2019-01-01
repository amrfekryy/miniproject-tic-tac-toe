import sys
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Tic Tac Toe")

		self.initUI()

	#_______________________________________VIEWS______________________________________

	def initUI(self):
		# create a widget for the page and give it a layout
		self.page = QtWidgets.QWidget()
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignCenter)
		self.page.setLayout(self.layout)
		# give the page a lightgray background
		self.page.setStyleSheet("QWidget {background-color: pink}")
		# set it as central widget
		self.setCentralWidget(self.page)



def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()