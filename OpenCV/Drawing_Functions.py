import numpy as np
import cv2

##Creating a black image using NumPy
##Common arguments for the drawing functions are as follows:
##img, color in the form of BGR, thickness (pass -1 for closed figures)
##lineType gives the type of line

##cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
##
##
##x1,y1 ------
##|          |
##|          |
##|          |
##--------x2,y2


img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0,0), (511,511),(255,0,0), 5)

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],False,(0,255,255))

cv2.imwrite("img.png", img)
cv2.imshow("something", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
