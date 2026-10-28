import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("Castelo.jpg").convert("RGB")

def converter_cinza(matriz):
    m, n= matriz.shape[0], matriz.shape[1]
    matriz_cinza = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            R = matriz[i, j, 0]
            G = matriz[i, j, 1]
            B = matriz[i, j, 2]
            matriz_cinza[i, j] = (0.299 * R + 0.587 * G + 0.114 * B)
    return matriz_cinza

matriz = np.array(img)
m = matriz.shape[0]
n = matriz.shape[1]

matriz_cinza = converter_cinza(matriz)

def padding(matriz_cinza):
    m, n = matriz_cinza.shape
    mtz_padding = np.zeros((m + 2, n + 2))
    m, n = mtz_padding.shape
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                mtz_padding[i, j] = 0
            else:
                mtz_padding[i, j] = matriz_cinza[i - 1, j - 1]
    return mtz_padding

matriz_padding = padding(matriz_cinza)

kernel_x = np.array([[-1, 0, 1], 
                     [-1, 0, 1], 
                     [-1, 0, 1]])

kernel_y = np.array([[-1, -1, -1],
                     [ 0,  0,  0],
                     [ 1,  1,  1]])

def aplicar_filtro(matriz_padding, kernel_x, kernel_y):
    m, n = matriz_padding.shape
    matriz_filtrada_x = np.zeros((m, n))
    matriz_filtrada_y = np.zeros((m, n))
    for i in range(m):
        for j in range(n):   
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                pass
            else:    
                matriz_filtrada_x[i, j] = np.sum(matriz_padding[i - 1:i + 2, j - 1:j + 2] * kernel_x)
                matriz_filtrada_y[i, j] = np.sum(matriz_padding[i - 1:i + 2, j - 1:j + 2] * kernel_y)

    return matriz_filtrada_x, matriz_filtrada_y

matriz_bordas_x, matriz_bordas_y = aplicar_filtro(matriz_padding, kernel_x, kernel_y)

matriz_bordas_combinadas = np.sqrt(matriz_bordas_x**2 + matriz_bordas_y**2)

print(matriz.shape)
print(matriz_cinza.shape)
print(matriz_bordas_x.shape)
print(matriz_bordas_y.shape)

#img colorida
plt.imshow(matriz)
plt.show()

#img cinza
plt.imshow(matriz_cinza, cmap='gray')
plt.show()

#img bordas
plt.imshow(np.abs(matriz_bordas_x), cmap='gray', vmin=0, vmax=765)
plt.colorbar()
plt.show()

#img bordas
plt.imshow(np.abs(matriz_bordas_y), cmap='gray', vmin=0, vmax=765)
plt.colorbar()
plt.show()

#img bordas combinadas 
plt.imshow(matriz_bordas_combinadas, cmap='gray', vmin=0, vmax=765)
plt.colorbar()
plt.show()