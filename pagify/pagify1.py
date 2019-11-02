import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img/test4.jpg',0)


img = cv2.imread('../img/test4.jpg', cv2.IMREAD_UNCHANGED)

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def callback(foo):
    pass

cv2.namedWindow('parameters')
cv2.createTrackbar('threshold', 'parameters', 0, 255, callback)
cv2.createTrackbar('threshold1', 'parameters', 0, 255, callback)
cv2.createTrackbar('apertureSize', 'parameters', 0,2, callback)
cv2.createTrackbar('L1/L2', 'parameters', 0, 1, callback)

while(True):
    thresh1 = cv2.getTrackbarPos('threshold', 'parameters')
    thresh2 = cv2.getTrackbarPos('threshold1', 'parameters')
    apSize = cv2.getTrackbarPos('apertureSize', 'parameters') * 2 + 3
    norm_flag = cv2.getTrackbarPos('L1/L2', 'parameters') == 1

    edges = cv2.Canny(img, thresh1, thresh2, apertureSize=apSize, L2gradient=norm_flag)

    img2 = cv2.resize(edges, (1000, 666))
    cv2.imshow('pic', img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# plt.subplot(121),plt.imshow(img)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges)
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()
