import cv2
import numpy as np

img1 = cv2.imread("../butterfly.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../a7v600-x02.png", cv2.IMREAD_GRAYSCALE)

# cv2.imshow("original2", img2)


# 1 - Usar funciones para realizar erosion, dilatacion, apertura y cierre en img1 e img2

# Imagen 1
kernel = np.ones((5, 5), np.uint8)
erode1 = cv2.erode(img1, kernel, iterations=1)
dilate1 = cv2.dilate(img1, kernel, iterations=1)
opening1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
cv2.imshow("original1", img1)
# El tamanio de las caracteristicas oscuras aumenta y las brillantes disminuyen
#cv2.imshow("erode img1",erode1)
# El tamanio de las caracteristicas brillantes aumenta y el de las oscuras disminuyen
# cv2.imshow("dilate img1",dilate1)
# Apertura elimina detalles luminosos chicos
#cv2.imshow("opening img1",opening1)
# Cierre elimina detalles oscuros chicos
#cv2.imshow("closing img1",closing1)
# Imagen 2
kernel2 = np.ones((7, 7), np.uint8)
erode2 = cv2.erode(img2, kernel2, iterations=1)
dilate2 = cv2.dilate(img2, kernel2, iterations=1)

#cv2.imshow("original2",img2)
#cv2.imshow("erode img2",erode2)
#cv2.imshow("dilate img2",dilate2)

# 2 - Experimente los siguientes procesos sobre la imagen, reflexionando previa-
# mente acerca de los resultados esperados

# E/D/A/C utilizando un EE disco o cuadrado de lado 10.

kernelRect = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
erodeKernelRect = cv2.erode(img1, kernel, iterations=1)
#cv2.imshow("Erode with rect kernel",erodeKernelRect)

# E/D/A/C utilizando un EE linea proponga la direccion de largo 20.

# kernelXdirection = cv2.getStructuringElement(cv2.MORPH_RECT,(1,20))
# erodex = cv2.erode(img1,kernelXdirection,iterations=1)
# cv2.imshow("erode x direction",erodex)
# dilatex = cv2.dilate(img1,kernelXdirection,iterations=1)
# cv2.imshow("dilate x direction", dilatex)
# openingx = cv2.morphologyEx(img1,cv2.MORPH_OPEN, kernelXdirection)
# cv2.imshow("opening x direction",openingx)
# closingx = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernelXdirection)
# cv2.imshow("closing x direction",closingx)

# Tanto apertura como erosion acentuan los oscuros reduciendo los claros y puede verse como distorsionan la imagen
# en direccion y, debido a que se define un kernel de 1 fila por 20 columnas. A su vez, cierre y dilatacion
# acentuan los claros reduciendo los pixeles oscuros


# kernelYdirection = cv2.getStructuringElement(cv2.MORPH_RECT,(20,1))
# erodey = cv2.erode(img1,kernelYdirection,iterations=1)
# cv2.imshow("erode y direction",erodey)
# dilatey = cv2.dilate(img1,kernelYdirection,iterations=1)
# cv2.imshow("dilate y direction", dilatey)
# openingy = cv2.morphologyEx(img1,cv2.MORPH_OPEN, kernelYdirection)
# cv2.imshow("opening y direction",openingy)
# closingy = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernelYdirection)
# cv2.imshow("closing y direction",closingy)

# Misma situacion que antes solo que ahora se ve reflejado en el eje x, debido a que se define un kernel de 20 filas
# por 1 columna


# Me falto E/D/A/C utilizando un EE disperso -proponga el conjunto de puntos- de lado 20.
# ya que no se como definir un EE disperso, o a mi gusto en python




cv2.waitKey(0)
