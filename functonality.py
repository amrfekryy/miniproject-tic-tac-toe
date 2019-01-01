import sys

lista = [" 1 ", " 2 ", " 3 ", 
         " 4 ", " 5 ", " 6 ", 
         " 7 ", " 8 ", " 9 "]

def print_lista():
	print(lista[:3])
	print()
	print(lista[3:6])
	print()
	print(lista[6:])
	print()

def playerX():
	index = int(input("Player X: choose a position? "))
	print()
	lista[index-1] = " X "

def playerO():
	index = int(input("Player O: choose a position? "))
	print()
	lista[index-1] = " O "

def check():
	if lista[0] == lista[1] == lista[2]:
		print(str(lista[0]) + "won!")
		sys.exit()
	if lista[3] == lista[4] == lista[5]:
		print(str(lista[3]) + "won!")
		sys.exit()
	if lista[6] == lista[7] == lista[8]:
		print(str(lista[6]) + "won!")
		sys.exit()
	if lista[0] == lista[3] == lista[6]:
		print(str(lista[0]) + "won!")
		sys.exit()
	if lista[1] == lista[4] == lista[7]:
		print(str(lista[1]) + "won!")
		sys.exit()
	if lista[2] == lista[5] == lista[8]:
		print(str(lista[2]) + "won!")
		sys.exit()
	if lista[0] == lista[4] == lista[8]:
		print(str(lista[0]) + "won!")
		sys.exit()
	if lista[2] == lista[4] == lista[6]:
		print(str(lista[2]) + "won!")
		sys.exit()

print_lista()
playerX()
print_lista()
playerO()
print_lista()
playerX()
print_lista()
playerO()
print_lista()
playerX()
check()
print_lista()
playerO()
check()
print_lista()
playerX()
check()
print_lista()
playerO()
check()
print_lista()
playerX()
check()
print("Draw!")