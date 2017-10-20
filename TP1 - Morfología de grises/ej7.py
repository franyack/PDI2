import cv2
import numpy as np

img = cv2.imread("../school_blurry.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original",img)
kernel25x25 = np.ones((25,25), np.uint8)

dilate = cv2.dilate(img,kernel25x25,iterations=1)
erode = cv2.erode(img,kernel25x25,iterations=1)
prom = cv2.addWeighted(dilate,0.5,erode,0.5,0)
cv2.imshow("Promedio",prom)

width,height = img.shape[:2]
for i in xrange(width):
    for j in xrange(height):
        if (img[i,j] > prom[i,j]):
            img[i,j]= dilate[i,j]
        else:
            img[i, j] = erode[i, j]

cv2.imshow("Restaurado",img)

kernel5x5 = np.ones((7,7), np.uint8)
TopHat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel5x5)
cv2.imshow("Restaurado - TopHat",img - TopHat)


cv2.waitKey(0)