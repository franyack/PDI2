import cv2
import numpy as np

img = cv2.imread("../Pattern.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("original",img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(30,30))
kernel2 = cv2.getStructuringElement(cv2.MORPH_OPEN,(150,150))
kernel3 = cv2.getStructuringElement(cv2.MORPH_OPEN,(5,5))



#erode = cv2.dilate(img,kernel,iterations=4)

close = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow("Closing",close)

opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel2)

cv2.imshow("Opening",opening)

cv2.imshow("Opening + Closing",opening+close)

gradientOpening = cv2.morphologyEx(opening,cv2.MORPH_GRADIENT,kernel3)

cv2.imshow("GradientOpening",gradientOpening)

erode2 = cv2.erode(gradientOpening,kernel3,iterations=1)

cv2.imshow("Erode of GradientOpening",erode2)

kernel4 = cv2.getStructuringElement(cv2.MORPH_OPEN,(35,35))
closing2 = cv2.morphologyEx(erode2,cv2.MORPH_CLOSE,kernel4)

cv2.imshow("Closing of Erode",closing2)
#
# dilate2 = cv2.dilate(gradientOpening,kernel3,iterations=1)

#
# cv2.imshow("Dilate of Erode",dilate2)
#
# mask = erode2.copy()

width,height = img.shape[:2]

for i in xrange(width):
    for j in xrange(height):
        if closing2[i,j] > 25:
            img[i,j]=0
            img[i+1,j+1]=0
            img[i-1, j-1] = 0

cv2.imshow("Segmented original",img)


cv2.waitKey(0)

