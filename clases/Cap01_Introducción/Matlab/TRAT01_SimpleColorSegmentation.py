# Importar Librerías
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Función de los datos de la imágen
def howis(imagen):
  print('size = ',imagen.shape)
  print('max  = ',np.max(imagen))
  print('min  = ',np.min(imagen))
  
Icv = cv2.imread('flowers.jpg')      # lectura en formato opencv (BGR)
cv2.imshow("Prueba",Icv)
cv2.waitKey(5000)
howis(Icv)

I = Icv[:,:,[2,1,0]]             # conversion a formato estándar (RGB)
plt.imshow(I)
plt.show()

#Canales de colores
R = I[:,:,0]
cv2.imshow("Prueba",R)
cv2.waitKey(5000)
G = I[:,:,1]
cv2.imshow("Prueba",G)
cv2.waitKey(5000)
B = I[:,:,2]
cv2.imshow("Prueba",B)
cv2.waitKey(5000)
RGB = np.concatenate((R,G,B),axis=1)#
cv2.imshow("Prueba",RGB)
cv2.waitKey(5000)

#Conversion a blanco y negro (tonos de gris)
Rd = R.astype(float)
Gd = G.astype(float)
Bd = B.astype(float)
k  = (1/3,1/3,1/3)
Zd = k[0]*Rd+k[1]*Gd+k[2]*Bd
Z  = Zd.astype(int)
howis(Z)
cv2.imshow("Prueba",Z)
cv2.waitKey(5000)

#Histograma
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
  
  imhist(Z)
  
#Segmentación de la Flor Roja
Sr = R>150
#cv2.imshow("Prueba",Sr)
#cv2.waitKey(5000)
Sg = G<40
#cv2.imshow("Prueba",Sg)
#cv2.waitKey(5000)
Sb = B<40 
#cv2.imshow("Prueba",Sb)
#cv2.waitKey(5000)
Srgb = np.concatenate((Sr,Sg,Sb),axis=1)
cv2.imshow("Prueba",Srgb*255)
cv2.waitKey(5000)
cv2.waitKey(5000)

S = np.logical_and(Sr,Sg,Sb)
cv2.imshow("Prueba",S*255)
cv2.waitKey(5000)

#Eliminación de filas con pocos unos
(N,M) = S.shape
Q = S
for i in range(N):
  s = np.sum(S[i,:])
  if s<20:
    Q[i,:] = 0
cv2.imshow("Prueba",Q*255)
cv2.waitKey(5000)

#Búsqueda de (imin,jmin) y (imax,jmax) en la región segmetada
imin = 1000
imax = 0
jmin = 1000
jmax = 0
for i in range(N):
  for j in range(M):
    if Q[i,j]>0:
      if i<imin:
        imin = i
      if i>imax:
        imax = i
      if j<jmin:
        jmin = j
      if j>jmax:
        jmax = j
        
#Gráfica de Bounding Box
y = [imin,imin,imax,imax,imin]
x = [jmin,jmax,jmax,jmin,jmin]
plt.imshow(I)
plt.plot(x,y)
plt.show()

#Detección de Bordes
E = np.zeros((N,M),np.uint8)
for i in range(N):
  for j in range(1,M):
    if Q[i,j]!=Q[i,j-1]: 
      E[i,j]   = 1
      E[i,j-1] = 1
for i in range(1,N):
  for j in range(M):
    if Q[i-1,j]!=Q[i,j]: 
      E[i,j]   = 1
      E[i,j-1] = 1
cv2.imshow("Prueba",E*255)
cv2.waitKey(5000)

for i in range(N):
  for j in range(M):
    if E[i,j]==1:
      Icv[i,j,:] = [255,0,0]
cv2.imshow("Prueba",Icv)
cv2.waitKey(5000)

        