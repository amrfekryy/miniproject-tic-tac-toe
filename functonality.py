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

def triplet_check(i, j, k):
	if lista[i] == lista[j] == lista[k]:
		print(str(lista[i]) + "won!")
		sys.exit()
	else: pass

def check():
	triplet_check(0, 1, 2)
	triplet_check(3, 4, 5)
	triplet_check(6, 7, 8)
	triplet_check(0, 3, 6)
	triplet_check(1, 4, 7)
	triplet_check(2, 5, 8)
	triplet_check(0, 4, 8)
	triplet_check(2, 4, 6)

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