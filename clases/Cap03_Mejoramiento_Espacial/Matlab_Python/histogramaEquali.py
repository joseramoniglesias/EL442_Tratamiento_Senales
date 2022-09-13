#/////////////////////////////////////
#//Equalizacion del histograma
#//Autor: José Ramón Iglesias
#/////////////////////////////////////

import cv2
import numpy as np
import matplotlib.pyplot as plt

f = cv2.imread('zorro.jpg', 0)

#calculo del histograma de la imagen de entrada f
histF = cv2.calcHist([f], [0], None, [256], [0, 256])
x = np.array(range(256))

#numero de elementos de la imagen, para normalizar
numel = f.size

#histograma normalizado (0 - 1) (divido entre todos los elementos)
histNorm = histF/numel

#suma acumulada del histograma normalizado
# cdf = np.sum(histNorm)
cdf = histNorm.cumsum()
cdf = cdf * 255


width, height = f.shape
g = np.zeros((width, height), np.uint8)

for i in range(width):
    for j in range(height):

        g[i, j] = cdf[f[i, j]]

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(f, cmap = 'gray')
plt.title('imagen de entrada')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(g, cmap = 'gray')
plt.axis('off')
plt.title('ecualización de histograma')
plt.show()


histG = cv2.calcHist([g], [0], None, [256], [0, 256])

# no se graficar chido
plt.figure()
plt.subplot(1, 3, 1)
plt.title('histgrama de f')
plt.plot(x, histF)

plt.subplot(1, 3, 2)
plt.title('funcion de densidad acumulada')
plt.plot(x, cdf)

plt.subplot(1, 3, 3)
plt.title('histograma de g')
plt.stem(x, histG)
plt.show()

#%%
