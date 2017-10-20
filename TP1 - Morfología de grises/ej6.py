import cv2
import numpy as np

img = cv2.imread("../bike.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original",img)
kernel5x5 = np.ones((5,5), np.uint8)
kernel2x2 = np.ones((2,2), np.uint8)
dilate = cv2.dilate(img,kernel5x5,iterations=1)
diff = dilate - img
cv2.imshow("diff",diff)
erode = cv2.erode(diff,kernel2x2,iterations=1)
cv2.imshow("Erode2x2",erode)



cv2.waitKey(0)