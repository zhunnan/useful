import numpy as np
import cv2
import json
import os
import datetime
import time
import matplotlib.pyplot as plt


def main():
    CLASSES = ('road', 'sidewalk', 'building', 'wall',
               'fence', 'pole', 'traffic light', 'traffic sign',
               'vegetation', 'terrain', 'sky', 'person',
               'rider', 'car', 'truck', 'bus',
               'train', 'motorcycle', 'bicycle')

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
    # dict data

    img_path = 'F:\\Download\\data_semantics\\training\\10\\'
    save_path = 'F:\\Download\\data_semantics\\training\\10\\'
    save2_path = 'F:\\Download\\data_semantics\\training\\100\\'
    filenames = os.listdir(save_path)
    # filenames.sort()

    for img_0 in filenames:
        print(img_0)
        img = cv2.imread(img_path + img_0)
        # print(img_path+img_0)
        sakura = {'centers': [], 'nodes': [], 'label': [], 'square': []}
        # height, width, channel = img.shape
        for color in np_PALETTE:
            colorlist = color.tolist()
            img_2 = cv2.inRange(img, color, color)
            contours, _ = cv2.findContours(img_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            if contours:
                for cnt in contours:
                    M = cv2.moments(cnt)
                    if M['m00'] != 0:
                        cx = int(M['m10'] / M['m00'])
                        cy = int(M['m01'] / M['m00'])
                        square = cv2.contourArea(cnt)
                        if square>400:
                            sakura['centers'].append([cx, cy, 0])
                            lebal = PALETTE_bgr.index(colorlist)
                            sakura['label'].append(CLASSES[lebal])
                            sakura['square'].append(square)
                            sakura['nodes'].append(color)
        cen = sakura['centers']
        cen = np.array(cen)
        x = cen[:, 0]
        y = cen[:, 1]
        color = sakura['nodes']
        # print(len(cen))
        # plt.plot(x,y,color='gray', zorder=-1)
        # plt.scatter(x, y,s=2)
        # print(x[0])
        # print(color)
        for i in range(len(cen)):
            plt.scatter(x[i], y[i], s=50, color=RGB_to_Hex(color[i]))
            # print(RGB_to_Hex(color[i]))
        # plt.axis('off')
        # plt.xticks([])
        # plt.yticks([])
        plt.savefig(fname=save2_path + img_0,dpi = 600)
        plt.clf()


def dic2node(sakura,img_0):
    # print(sakura['centers'])`
    save_path = 'F:\\Download\\data_semantics\\training\\save\\'
    cen = sakura['centers']
    cen = np.array(cen)
    x = cen[:, 0]
    y = cen[:, 1]
    color = sakura['nodes']
    # print(len(cen))
    # plt.plot(x,y,color='gray', zorder=-1)
    # plt.scatter(x, y,s=2)
    # print(x[0])
    # print(color)
    for i in range(len(cen)):
        plt.scatter(x[i], y[i],s=8,color=RGB_to_Hex(color[i]))
        # print(RGB_to_Hex(color[i]))

    plt.savefig(fname=save_path+img_0, figsize=[10, 10])





def RGB_to_Hex(bgr):

    color = '#'

    color += str(hex(bgr[2]))[-2:].replace('x', '0').upper()
    color += str(hex(bgr[1]))[-2:].replace('x', '0').upper()
    color += str(hex(bgr[0]))[-2:].replace('x', '0').upper()
    # print(hex(bgr[2]))
    # print(color)
    return color

if __name__ == '__main__':
    # c =[[499, 305, 0], [999, 353, 0], [947, 241, 0], [958, 237, 0], [970, 230, 0], [925, 233, 0], [399, 212, 0], [443, 203, 0], [383, 207, 0], [777, 200, 0], [813, 206, 0], [840, 227, 0], [753, 199, 0], [820, 263, 0], [543, 180, 0], [635, 180, 0], [504, 174, 0], [526, 178, 0], [554, 169, 0], [568, 168, 0], [538, 174, 0], [516, 166, 0], [638, 162, 0], [664, 157, 0], [837, 149, 0], [711, 149, 0], [791, 140, 0], [754, 143, 0], [763, 104, 0], [765, 94, 0], [756, 75, 0], [4, 99, 0], [772, 61, 0], [792, 52, 0], [784, 48, 0], [775, 33, 0], [1088, 81, 0], [344, 85, 0], [991, 201, 0], [842, 196, 0], [667, 171, 0], [712, 169, 0], [754, 179, 0], [830, 174, 0], [792, 177, 0], [848, 168, 0], [1086, 170, 0], [781, 222, 0], [799, 222, 0], [493, 169, 0], [822, 190, 0], [765, 163, 0], [951, 208, 0], [494, 154, 0], [80, 259, 0], [832, 232, 0], [810, 226, 0], [786, 220, 0], [379, 172, 0], [526, 147, 0], [782, 91, 0], [104, 102, 0], [535, 54, 0], [223, 185, 0], [697, 175, 0], [1096, 285, 0], [229, 234, 0], [686, 187, 0], [714, 193, 0], [657, 184, 0], [621, 178, 0], [568, 175, 0], [449, 191, 0], [588, 169, 0], [622, 168, 0]]
    main()
    # c=np.array([232, 35, 244])
    # print(c)
    # t=RGB_to_Hex(c)



