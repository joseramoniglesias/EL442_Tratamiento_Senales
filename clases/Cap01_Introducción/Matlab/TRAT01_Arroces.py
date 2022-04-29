# Importar Librerías
import numpy as np
import cv2
#from cv2 import imread


# Cargamos la imagen del disco duro
imagen = cv2.imread("rices.png")

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

# Función de Segmentación por Umbral
def segmenta(X,t):
  (N,M) = X.shape
  Y = np.zeros((N,M))
  area = 0
  for i in range(N):
    for j in range(M):
      if X[i,j] > t:
        Y[i,j] = 255
        area = area + 1
  print('area = ',area)
  return Y

# Segmentación
Y = segmenta(X,170)
cv2.imshow("Prueba",Y)
cv2.waitKey(0)

# Con mayor complejidad
imagen = cv2.imread("rices.png")
X   = imagen[:,:,0]
howis(X)
cv2.imshow("Prueba",X)
cv2.waitKey(0)

Y = segmenta(X,110)
cv2.imshow("Prueba",Y)
cv2.waitKey(0)

# Obtenemos Imaágen con un fondo homogéneo
(N,M) = X.shape
Xm    = np.zeros((N,M),np.uint8)
for i in range(N):
  xmin = np.min(X[i,:])
  Xm[i,:] = X[i,:] - xmin
cv2.imshow("Prueba",Xm)
cv2.waitKey(0)

Y = segmenta(Xm,60)
cv2.imshow("Prueba",Y)
cv2.waitKey(0)

