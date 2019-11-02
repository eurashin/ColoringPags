import cv2
import numpy as np
from matplotlib import pyplot as plt


def callback(foo):
    pass


def pagify(url = '../img/test4.jpg'):
    img = cv2.imread(url, cv2.IMREAD_UNCHANGED)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    cv2.namedWindow('parameters')
    cv2.createTrackbar('threshold', 'parameters', 0, 255, callback)

    while(True):
        thresh = cv2.getTrackbarPos('threshold', 'parameters')

        ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

        contours, heirarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img_contours = np.zeros(img.shape)
        img_contours.fill(255)

        cv2.drawContours(img_contours, contours, -1, (0,0,0), 3)

        # img2 = cv2.resize(img_contours, (1000, 666))
        # img3 = cv2.bitwise_not(img2)
        cv2.imshow('pic', img_contours)

        if cv2.waitKey(1)&0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

pagify()