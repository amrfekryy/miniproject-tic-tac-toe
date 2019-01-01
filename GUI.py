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
		self.Vlayout = QtWidgets.QVBoxLayout()
		self.Vlayout.setAlignment(QtCore.Qt.AlignCenter)
		self.page.setLayout(self.Vlayout)
		# set bg color to pink
		self.page.setStyleSheet("QWidget {background-color: pink}")
		# set page as central widget
		self.setCentralWidget(self.page)
		# add a grid layout for the buttons
		self.Glayout = QtWidgets.QGridLayout()
		self.Vlayout.addLayout(self.Glayout)
		# create 9 buttons and add them to the list
		for row in range(3):
			for col in range(3):
				self.btn = QtWidgets.QPushButton("Button"+str(row)+str(col))
				# connect each button while looping to the function passing the button as argument
				self.btn.clicked.connect(partial(self.btn_clicked, self.btn))
				self.btn.setMinimumSize(100, 100)
				self.Glayout.addWidget(self.btn,row,col)
		
		for i in range(9):
			print(self.Glayout.itemAt(i).widget())

	#_______________________________________METHODS______________________________________

	def btn_clicked(self, btn):
		print(btn)




def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()