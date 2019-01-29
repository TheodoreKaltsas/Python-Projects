import numpy as np
import cv2
from matplotlib import pyplot as plt

##img = cv2.imread('Forest.jpg', 0)
##
####Show the image amd create a break for the program
####cv2.WINDOW_NORMAL creates a resizable window 
##cv2.namedWindow('Forest Image', cv2.WINDOW_NORMAL)
##cv2.imshow('Forest Image',img)
##k = cv2.waitKey(0) & 0xFF
##
##if k == 27:
##    cv2.destroyAllWindows()

##Can also display image with keypoints

img = cv2.imread('Forest.jpg', 0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
