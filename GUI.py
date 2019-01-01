import sys
from PyQt5 import QtWidgets, QtCore
from functools import partial


class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Tic Tac Toe")

		self.initUI()

	#_______________________________________VIEWS______________________________________

	def initUI(self):
		# create a widget for the page with a vertical layout
		self.page = QtWidgets.QWidget()
		self.page.setStyleSheet("QWidget {background-color: pink}")
		self.Vlayout = QtWidgets.QVBoxLayout()
		self.Vlayout.setAlignment(QtCore.Qt.AlignCenter)
		self.page.setLayout(self.Vlayout)
		# set page as central widget
		self.setCentralWidget(self.page)
		# add a grid layout for the buttons
		self.Glayout = QtWidgets.QGridLayout()
		self.Vlayout.addLayout(self.Glayout)
		
		# create 9 buttons and add them to the grid layout
		self.btn_indx = 0 # counter for buttons indeces
		for row in range(3):
			for col in range(3):
				self.btn = QtWidgets.QPushButton()
				self.btn.setMinimumSize(100, 100)
				self.Glayout.addWidget(self.btn,row,col)
				
				# connect each button while looping to the function passing the button as argument
				self.btn.clicked.connect(partial(self.btn_clicked, self.btn, self.btn_indx)) # currying, or partial application
				self.btn_indx += 1
		
		# initialize a list to store Xs and Os
		self.init_list()

	#_______________________________________METHODS______________________________________

	def init_list(self):
		self.click_list = [0, 1, 2,
						   3, 4, 5,
		                   6, 7, 8]
		self.click_counter = 0

	def btn_clicked(self, btn, indx):
		print(btn)
		print(indx)
		if self.click_counter % 2 == 0:
			self.click_list[indx] = "X"
			print(self.click_list)
			btn.setText("X")
			self.click_counter += 1
		else:
			self.click_list[indx] = "O"
			print(self.click_list)
			btn.setText("O")
			self.click_counter += 1


def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()