import numpy as np
import cv2

##cap = cv2.VideoCapture(0)

##In order to save videos, we need to create a VideoWriter object
##In this we specify the output file name and the FourCC (Video Codec)
##On Windows it is cv2.VideoWriter_fourcc('D','I','V','X')
###################################################################
##while(cap.isOpened()):
##    ret, frame = cap.read()
##
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##
##    cv2.imshow('frame', gray)
##
##    if cv2.waitKey(1) & 0xFF == ord('s'):
## 
##cap.release()
##cv2.destroyAllWindows()
####################################################################
##This is the example for saving videos
##Video codec quality for Windows is DIVX
##out = cv2.VideoWriter('video.avi',fourcc, 20.0, (640,480)) parameters:
##(filename, codec quality, FPS, dimensions) Last parameter is isColor
####################################################################
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('video.mp4',fourcc, 20.0, (640,480), 1)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)

        out.write(frame)

        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
    
