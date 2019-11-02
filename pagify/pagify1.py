import numpy as np
import cv2
from matplotlib import pyplot as plt

def callback(foo):
    pass

def pagify(paths):
    counter = 0
    img_paths = []
    for url in paths:
        img = cv2.imread(url, cv2.IMREAD_UNCHANGED)
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        high_thresh, thresh_im = cv2.threshold(img_grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        lowThresh = 0.8 * high_thresh
        edges = cv2.Canny(img_grey, lowThresh, high_thresh, apertureSize=3)

        scale_percent = 60  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        img3 = cv2.bitwise_not(resized)
        fname = 'colorme' + str(counter) + '.pdf'
        cv2.imwrite('static/' + fname ,img3)
        counter += 1

        img_paths.append(fname)
    return(img_paths)

    # cv2.namedWindow('parameters')
    # cv2.createTrackbar('threshold', 'parameters', 0, 255, callback)
    # cv2.createTrackbar('threshold1', 'parameters', 0, 255, callback)
    # cv2.createTrackbar('apertureSize', 'parameters', 0,2, callback)
    # cv2.createTrackbar('L1/L2', 'parameters', 0, 1, callback)
    #
    # while(True):
    #     thresh1 = cv2.getTrackbarPos('threshold', 'parameters')
    #     thresh2 = cv2.getTrackbarPos('threshold1', 'parameters')
    #     apSize = cv2.getTrackbarPos('apertureSize', 'parameters') * 2 + 3
    #     norm_flag = cv2.getTrackbarPos('L1/L2', 'parameters') == 1
    #
    #     edges = cv2.Canny(img_grey, thresh1, thresh2, apertureSize=apSize, L2gradient=norm_flag)
    #
    #     img2 = cv2.resize(edges, (1000, 666))
    #     img3 = cv2.bitwise_not(img2)
    #     cv2.imshow('pic', img3)
    #
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # cv2.destroyAllWindows()


# plt.subplot(121),plt.imshow(img)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges)
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()
