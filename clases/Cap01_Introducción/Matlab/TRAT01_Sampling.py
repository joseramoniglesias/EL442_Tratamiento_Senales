# Importar Librerías
import numpy as np
import cv2
#from cv2 import imread


# Cargamos la imagen del disco duro
imagen = cv2.imread('mandril.png')

cv2.imshow("prueba", imagen)
cv2.waitKey(0)

# Función de los datos de la imágen
def howis(imagen):
  print('size = ',imagen.shape)
  print('max  = ',np.max(imagen))
  print('min  = ',np.min(imagen))

howis(imagen)

# Seleciona el canal de la imágen
X = imagen[:,:,0]
howis(X)
cv2.imshow("Prueba",X)
cv2.waitKey(0)


# Muestreo Espacial
d = 4   # se muestrea cada d pixeles
(Nx,Mx) = X.shape
ix = range(0,Nx,d)
jx = range(0,Mx,d)
Ny = len(ix)
My = len(jx)
Y = np.zeros((Ny,My),np.uint8)
for i in range(Ny):
  for j in range(My):
    Y[i,j] = X[ix[i],jx[j]]
cv2.imshow("Prueba",Y)
cv2.waitKey(0)
howis(Y)

d = 8  # se muestrea cada d pixeles
(Nx,Mx) = X.shape
Ny = Nx
My = Mx
Y = np.zeros((Ny,My),np.uint8)
for i in range(Ny):
  for j in range(My):
    ix = int(np.fix(i/d)*d)
    jx = int(np.fix(j/d)*d)
    Y[i,j] = X[ix,jx]
cv2.imshow("Prueba",Y)
cv2.waitKey(0)
howis(Y)
print('desplegado como = ',int(Nx/d),'x',int(Nx/d))

# Muestreo en tonos de gris (Cuantización)
p = 4  # se muestrea el tono de gris cada p valores de gris
(Nx,Mx) = X.shape
Ny = Nx
My = Mx
Y = np.zeros((Ny,My),np.uint8)
for i in range(Ny):
  for j in range(My):
    x = int(np.fix(X[i,j]/p)*p)
    Y[i,j] = x
cv2.imshow("Prueba",Y)
cv2.waitKey(0)
howis(Y)
print('esta imagen tiene = ',int(256/p),' tonos de gris')

import matplotlib.pyplot as plt
def imhist(X):
  (N,M) = X.shape
  n = 256
  h = np.zeros((256,))
  for i in range(N):
    for j in range(M):
      x = X[i,j]
      h[x] = h[x]+1
  plt.plot(range(n),h[0:n])
  plt.show()

imhist(Y)

#print(h[0:256])






