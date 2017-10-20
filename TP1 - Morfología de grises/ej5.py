import cv2
import numpy as np
img = cv2.imread("../Fig9-44c.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("original",img)
kernel1x20 = np.ones((1,20), np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel1x20)
cv2.imshow("Opening",opening)

kernel5x5 = np.ones((5,5), np.uint8)
TopHat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel5x5)
cv2.imshow("TopHat",TopHat)

# TopHat = img - opening
# cv2.imshow("TopHat",TopHat)


cv2.waitKey(0)