import cv2
import numpy as np

img = cv2.imread("../hoja.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("original",img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel2)
opening = cv2.morphologyEx(gradient,cv2.MORPH_OPEN,kernel)
eroding = cv2.erode(gradient,kernel,iterations=1)

width,height = img.shape[:2]


cv2.imshow("gradient",gradient)
cv2.imshow("gradient + opening",opening)
cv2.imshow("gradient + eroding",eroding)

dilating = cv2.dilate(img,kernel,iterations=2)
gradient2 = cv2.morphologyEx(dilating,cv2.MORPH_GRADIENT,kernel)

mask = gradient2.copy()

for i in xrange(width):
    for j in xrange(height):
        if (gradient2[i,j] > 50):
            mask[i, j] = 255
        else:
            mask[i, j] = 0


cv2.imshow("dilating + gradient", gradient2)
cv2.imshow("mask",mask)

cv2.waitKey(0)

