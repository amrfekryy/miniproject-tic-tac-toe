import sys, time
from PyQt5 import QtWidgets, QtCore
from functools import partial


class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		
		self.setGeometry(450, 200, 600, 400)
		self.setWindowTitle("Tic Tac Toe")
		self.show()
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
		# add a play again button
		self.playagain_btn = QtWidgets.QPushButton("Play Again")
		self.playagain_btn.setFixedSize(100, 30)
		self.playagain_btn.clicked.connect(self.new_game)
		self.Vlayout.addWidget(self.playagain_btn, 0, QtCore.Qt.AlignCenter)

		# create 9 buttons and add them to the grid layout
		self.add_btns()
		# initialize a list to store Xs and Os
		self.init_list()

	def add_btns(self):
		self.btn_indx = 0 # counter for buttons indeces
		for row in range(3):
			for col in range(3):
				self.btn = QtWidgets.QPushButton()
				self.btn.setMinimumSize(100, 100)
				self.Glayout.addWidget(self.btn,row,col)
				
				# connect each button while looping to the function passing the button as argument
				self.btn.clicked.connect(partial(self.btn_clicked, self.btn, self.btn_indx)) # currying, or partial application
				self.btn_indx += 1

	#_______________________________________METHODS______________________________________

	def init_list(self):
		self.click_list = [0, 1, 2,
						   3, 4, 5,
		                   6, 7, 8]
		self.click_counter = 0

	def btn_clicked(self, btn, indx):
		# X turn is even
		if self.click_counter % 2 == 0:
			self.click_list[indx] = "X"
			btn.setText("X")
			print(self.click_list)
		# O turn is odd
		else:
			self.click_list[indx] = "O"
			btn.setText("O")
			print(self.click_list)
		self.click_counter += 1
		# start checking after the third X (turn 5)
		if self.click_counter > 4:
			self.check()
		if self.click_counter == 9:
			QtWidgets.QMessageBox.warning(self, "winner!", "It is a draw")
			self.disable_btns()

	def check(self):
		self.triplet_check(0, 1, 2)
		self.triplet_check(3, 4, 5)
		self.triplet_check(6, 7, 8)
		self.triplet_check(0, 3, 6)
		self.triplet_check(1, 4, 7)
		self.triplet_check(2, 5, 8)
		self.triplet_check(0, 4, 8)
		self.triplet_check(2, 4, 6)

	def triplet_check(self, i, j, k):
		if self.click_list[i] == self.click_list[j] == self.click_list[k]:
			print(self.click_list[i] + " Won!!")
			QtWidgets.QMessageBox.warning(self, "winner!", "Player " + self.click_list[i] + " Won!!")
			self.disable_btns()
		else: pass

	def disable_btns(self):
		for i in range(self.Glayout.count()):
			self.Glayout.itemAt(i).widget().setEnabled(False)

	def new_game(self):
		self.init_list()
		self.clear_btns()
		self.enable_btns()

	def clear_btns(self):
		for i in range(self.Glayout.count()):
			self.Glayout.itemAt(i).widget().setText("")

	def enable_btns(self):
		for i in range(self.Glayout.count()):
			self.Glayout.itemAt(i).widget().setEnabled(True)



def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()