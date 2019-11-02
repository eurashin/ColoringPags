import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('../img/test4.jpg', cv2.IMREAD_UNCHANGED)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def callback(foo):
    pass

cv2.namedWindow('parameters')
cv2.createTrackbar('threshold', 'parameters', 0, 255, callback)

while(True):
    thresh = cv2.getTrackbarPos('threshold', 'parameters')
        
    ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

    contours, heirarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_contours = np.zeros(img.shape)

    cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)

#cv2.imwrite('../img/pic4.jpg', img_contours)
    img2 = cv2.resize(img_contours, (1000, 666))
    cv2.imshow('pic', img2)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cv2.destroyAllWindows()
