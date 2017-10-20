import cv2
import numpy as np

img = cv2.imread("../coins.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original",img)
kernel9x9 = np.ones((9,9),np.uint8)
dilate = cv2.dilate(img,kernel9x9,iterations=7)
cv2.imshow("dilate",dilate)
opening = cv2.morphologyEx(dilate,cv2.MORPH_OPEN,kernel9x9)
cv2.imshow("opening",opening)
width,height = img.shape[:2]
mask = opening.copy()
for i in xrange(width):
    for j in xrange(height):
        if (opening[i,j] > 240):
            mask[i,j]= 0
        else:
            mask[i, j] = 255
cv2.imshow("mask",mask)
# ret,thresh = cv2.threshold(img,0,100,0)
#
# img2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#
# cv2.imshow("img2",thresh)


cv2.waitKey(0)