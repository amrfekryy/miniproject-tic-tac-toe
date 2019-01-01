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
		# a list to refer to the buttons
		self.btn_list = []
		# create 9 buttons and add them to the list
		for row in range(3):
			for col in range(3):
				self.btn = QtWidgets.QPushButton("Button"+str(row)+str(col))
				self.btn.setMinimumSize(100, 100)
				self.btn_list.append(self.btn)
				self.Glayout.addWidget(self.btn,row,col)
		

		
		print(self.btn_list)




def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

main()