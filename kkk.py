import numpy as np


img_num = 20
my_result = np.zeros((img_num,3),dtype=int)
for i in range(img_num):

    my_result[i][0]= i+1

# print(my_result)
# print(my_result[0][0])

import scipy.io
data = scipy.io.loadmat('/media/wan/bei/2021-8/SG_PR-master/img_groundtruth/KITTI_Ground/kitti00GroundTruth.mat')



gnd=data['truth']




# # print(gnd[0][0])
# # gnd=gnd.sum(axis=1)
# # print(len(gnd))
# # for i in range(4000):
# #     if gnd[i]!=0:
# #         print(i)
# # smallerThan=lambda x, y: [i for i in x if i < y]
# # print(smallerThan)