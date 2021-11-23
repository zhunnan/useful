import numpy as np
import cv2


def main():

    CLASSES = ('road', 'sidewalk', 'building', 'wall', 'fence', 'pole',
               'traffic light', 'traffic sign', 'vegetation', 'terrain', 'sky',
               'person', 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle',
               'bicycle')

    PALETTE = [[128, 64, 128], [244, 35, 232], [70, 70, 70], [102, 102, 156],
               [190, 153, 153], [153, 153, 153], [250, 170, 30], [220, 220, 0],
               [107, 142, 35], [152, 251, 152], [70, 130, 180], [220, 20, 60],
               [255, 0, 0], [0, 0, 142], [0, 0, 70], [0, 60, 100],
               [0, 80, 100], [0, 0, 230], [119, 11, 32]]

    PALETTE_bgr = [[128, 64, 128], [232, 35, 244], [70, 70, 70], [156, 102, 102],
                   [153, 153, 190], [153, 153, 153], [30, 170, 250], [0, 220, 220],
                   [35, 142, 107], [152, 251, 152], [180, 130, 70], [60, 20, 220],
                   [0, 0, 255], [142, 0, 0], [70, 0, 0], [100, 60, 0],
                   [100, 80, 0], [230, 0, 0], [32, 11, 119]]
    np_PALETTE = np.array(PALETTE_bgr)

    img = cv2.imread()

    for color in np_PALETTE:
        colorlist = color.tolist()
        img_2 = cv2.inRange(img,color,color)
        contours,_=cv2.findContours(img_2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        if contours:
            for cnt in contours:
                M = cv2.moments(cnt)
                if M['m00']!=0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    lebal = PALETTE_bgr.index(colorlist)



if __name__=='__main__':

    main()
