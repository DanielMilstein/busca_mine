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
	minas = [(1,1)]
	n = len(tabl[0])

	while len(minas) != k:
		x = random.randint(0,n)
		y = random.randint(0,n)

		if (x,y) not in minas:
			minas.append((x,y))
			tabl[y][x] = 'M'
	return minas


def algoritmo_minas(tab, minas):
	n = len(tab[0])
	for (x, y) in minas:
		#Casos limite, ie: bordes y esquinas
		#Esquinas (Primero para no repetir condiciones)
		if x == 0 and y == 0:
			try:
				tab[y+1][x+1] = str(int(tab[y+1][x+1])+1)
				tab[y][x+1] = str(int(tab[y][x+1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
			except:
				continue
	
		elif x == n-1 and y == n-1:
			try:
				tab[y-1][x-1] = str(int(tab[y-1][x-1])+1)
				tab[y][x-1] = str(int(tab[y][x-1])+1)
				tab[y-1][x] = str(int(tab[y-1][x])+1)
			except:
				continue

		elif x == 0 and y == n-1:
			try:
				tab[y-1][x] = str(int(tab[y-1][x])+1)
				tab[y-1][x+1] = str(int(tab[y-1][x+1])+1)
				tab[y][x+1] = str(int(tab[y][x+1])+1)
			except:
				continue
		elif x == n-1 and y == 0:
			try:
				tab[y][x-1] = str(int(tab[y][x-1])+1)
				tab[y+1][x-1] = str(int(tab[y+1][x-1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
			except:
				continue
		#Bordes
		elif x == 0:
			try:
				tab[y-1][x] = str(int(tab[y-1][x])+1)
				tab[y][x+1] = str(int(tab[y][x+1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
				tab[y-1][x+1] = str(int(tab[y-1][x+1])+1)
				tab[y+1][x+1] = str(int(tab[y+1][x+1])+1)
			except:
				continue
		elif y == 0:
			try:
				tab[y][x-1] = str(int(tab[y][x-1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
				tab[y][x+1] = str(int(tab[y][x+1])+1)
				tab[y+1][x-1] = str(int(tab[y+1][x-1])+1)
				tab[y+1][x+1] = str(int(tab[y+1][x+1])+1)			
			except:
				continue
		elif x == n-1:
			try:
				tab[y-1][x] = str(int(tab[y-1][x])+1)
				tab[y][x-1] = str(int(tab[y][x-1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
				tab[y-1][x-1] = str(int(tab[y-1][x-1])+1)
				tab[y+1][x-1] = str(int(tab[y+1][x-1])+1)
			except:
				continue
		elif y == n-1:
			try:
				tab[y][x-1] = str(int(tab[y][x-1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
				tab[y][x+1] = str(int(tab[y][x+1])+1)
				tab[y-1][x-1] = str(int(tab[y-1][x-1])+1)
				tab[y-1][x+1] = str(int(tab[y-1][x+1])+1)
			except:
				continue
		#Else...
		else:
			try:
				tab[y-1][x-1] = str(int(tab[y-1][x-1])+1)
				tab[y-1][x] = str(int(tab[y-1][x])+1)
				tab[y-1][x+1] = str(int(tab[y-1][x+1])+1)
				tab[y][x-1] = str(int(tab[y][x-1])+1)
				tab[y][x+1] = str(int(tab[y][x+1])+1)
				tab[y+1][x-1] = str(int(tab[y+1][x-1])+1)
				tab[y+1][x] = str(int(tab[y+1][x])+1)
				tab[y+1][x+1] = str(int(tab[y+1][x+1])+1)
			except:
				continue



def mini_alg(tab, x, y): # Intentar excluir terminos mas que agregar
	if x != 0:
		tab[y-1][x-1] = str(int(tab[y-1][x-1])+1)
	tab[y-1][x] = str(int(tab[y-1][x])+1)
	tab[y-1][x+1] = str(int(tab[y-1][x+1])+1)
	tab[y][x-1] = str(int(tab[y][x-1])+1)
	tab[y][x+1] = str(int(tab[y][x+1])+1)
	tab[y+1][x-1] = str(int(tab[y+1][x-1])+1)
	tab[y+1][x] = str(int(tab[y+1][x])+1)
	tab[y+1][x+1] = str(int(tab[y+1][x+1])+1)





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