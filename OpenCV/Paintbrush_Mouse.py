import cv2
import numpy as np

##This is the most basic version of a mouse call back which waits for
##The user to double click before drawing a circle
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

drawing = False
mode = True
ix,iy = -1,-1

##This is the more advanced version of drawing the rectange
##it is based on mouse clicks rather than double clickss
def draw_circle_adv(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y 

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
##            else:
##                cv2.circle(img,(x,y),5,(0,0,255),-1)
                
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y), (0,255,0),-1)
##        else:
##            cv2.circle(img,(x,y),5,(0,0,255),-1)

##Initialize a basic black screen and window
##Link the mouse draw function to the window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle_adv)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

##Save drawn image and destroy the windows
cv2.imwrite('drawing.png',img)
cv2.destroyAllWindows()
