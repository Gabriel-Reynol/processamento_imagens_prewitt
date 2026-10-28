import numpy as np

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

def converter_cinza(matriz):
    matriz_cinza = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            R = matriz[i, j, 0]
            G = matriz[i, j, 1]
            B = matriz[i, j, 2]
            matriz_cinza[i, j] = (0.299 * R + 0.587 * G + 0.114 * B)
    return matriz_cinza

matriz = np.zeros((m, n, 3))
matriz_cinza = np.zeros((m, n))
RGB = {'R': 0, 'G': 0, 'B': 0}

for i in range(m):
    for j in range(n):
        x = int(input(f"Enter R element at position ({i}, {j}): R{RGB['R']} "))
        y = int(input(f"Enter G element at position ({i}, {j}): G{RGB['G']}"))
        z = int(input(f"Enter B element at position ({i}, {j}): B{RGB['B']} "))

        matriz[i, j, 0] = x
        matriz[i, j, 1] = y
        matriz[i, j, 2] = z

matriz_cinza = converter_cinza(matriz)


