import cv2
import numpy as np
img = cv2.imread("../PostSpinalRodsAP.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("original",img)
kernel = np.ones((10,10), np.uint8)

#####################PARTE 1 - TORNILLOS#####################################
#Al hacer una apertura remuevo las diferencias externas normalizando el exterior haciendo todos sus puntos parecidos,
#Luego, me quedo unicamente con aquellos puntos que superan un valor muy alto casi al blanco total.
#Por ultimo, erosiono para que los tornillos no queden tan anchos (podria no ser necesario)
opening1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("apertura",opening1)
width,height = img.shape[:2]
mask = opening1.copy()
for i in xrange(width):
    for j in xrange(height):
        if (opening1[i,j] > 230):
            mask[i, j] = 255
        else:
            mask[i, j] = 0
# cv2.imshow("Mascara",mask)
kernel2 = np.ones((3,3), np.uint8)
erodeMask = cv2.erode(mask,kernel2,iterations=1)
# cv2.imshow("Mascara Erosionada",erodeMask)
##############################################################################

##########################PARTE 2 - REJILLA###################################
TopHat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
# cv2.imshow("Top-Hat",TopHat)
# BottomHat = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) - img
# cv2.imshow("Bottom-Hat",BottomHat)

# width,height = img.shape[:2]
# mask = TopHat.copy()
#
# for i in xrange(width):
#     for j in xrange(height):
#         if (TopHat[i,j] > 25):
#             mask[i, j] = 255
#         else:
#             mask[i, j] = 0
#
cv2.imshow("Top-Hat",TopHat)
# cv2.imshow("Mascara",mask)
#########################################################################
cv2.waitKey(0)