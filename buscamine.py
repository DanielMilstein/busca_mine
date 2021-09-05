from numpy import random

def tablero(n, k):
	tab = []
	for i in range(n):
		fila = []
		for j in range(n):
			fila.append('0')
		tab.append(fila)

	return tab

def gen_minas(tabl, k):
	minas = []
	n = len(tabl[0])

	while len(minas) != k:
		x = random.randint(0,n)
		y = random.randint(0,n)

		if (x,y) not in minas:
			minas.append((x,y))
			tabl[y][x] = 'M'
	return minas

def verif(e):
	if e == 'M':
		return e
	else:
		e = str(int(e)+1)
		return e


def algoritmo_minas(tab, minas):
	n = len(tab[0])
	for (x, y) in minas:
		#Casos limite, ie: bordes y esquinas
		#Esquinas (Primero para no repetir condiciones)
		if x == 0 and y == 0:	
			tab[y+1][x+1] = verif(tab[y+1][x+1])
			tab[y][x+1] = verif(tab[y][x+1])
			tab[y+1][x] = verif(tab[y+1][x])
		elif x == n-1 and y == n-1:
			tab[y-1][x-1] = verif(tab[y-1][x-1])
			tab[y][x-1] = verif(tab[y][x-1])
			tab[y-1][x] = verif(tab[y-1][x])
		elif x == 0 and y == n-1:
			tab[y-1][x] = verif(tab[y-1][x])
			tab[y-1][x+1] = verif(tab[y-1][x+1])
			tab[y][x+1] = verif(tab[y][x+1])
		elif x == n-1 and y == 0:
			tab[y][x-1] = verif(tab[y][x-1])
			tab[y+1][x-1] = verif(tab[y+1][x-1])
			tab[y+1][x] = verif(tab[y+1][x])
		#Bordes
		elif x == 0:
			tab[y-1][x] = verif(tab[y-1][x])
			tab[y][x+1] = verif(tab[y][x+1])
			tab[y+1][x] = verif(tab[y+1][x])
			tab[y-1][x+1] = verif(tab[y-1][x+1])
			tab[y+1][x+1] = verif(tab[y+1][x+1])
		elif y == 0:
			tab[y][x-1] =verif(tab[y][x-1])
			tab[y+1][x] = verif(tab[y+1][x])
			tab[y][x+1] = verif(tab[y][x+1])
			tab[y+1][x-1] = verif(tab[y+1][x-1])
			tab[y+1][x+1] = verif(tab[y+1][x+1])
		elif x == n-1:
			tab[y-1][x] = verif(tab[y-1][x])
			tab[y][x-1] = verif(tab[y][x-1])
			tab[y+1][x] = verif(tab[y+1][x])
			tab[y-1][x-1] = verif(tab[y-1][x-1])
			tab[y+1][x-1] = verif(tab[y+1][x-1])
		elif y == n-1:
			tab[y][x-1] = verif(tab[y][x-1])
			tab[y-1][x] = verif(tab[y-1][x])
			tab[y][x+1] = verif(tab[y][x+1])
			tab[y-1][x-1] = verif(tab[y-1][x-1])
			tab[y-1][x+1] = verif(tab[y-1][x+1])
		#Else...
		else:
			tab[y-1][x-1] = verif(tab[y-1][x-1])
			tab[y-1][x] = verif(tab[y-1][x])
			tab[y-1][x+1] = verif(tab[y-1][x+1])
			tab[y][x-1] = verif(tab[y][x-1])
			tab[y][x+1] = verif(tab[y][x+1])
			tab[y+1][x-1] = verif(tab[y+1][x-1])
			tab[y+1][x] = verif(tab[y+1][x])
			tab[y+1][x+1] = verif(tab[y+1][x+1])






def main():
	n = 15
	k = 15
	t = tablero(n, k)
	mines = gen_minas(t, k)
	algoritmo_minas(t, mines)
	for x in t:
		print(x)


#Main
if __name__ == "__main__":
	main()