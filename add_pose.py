import numpy as np
import cv2
import json
import os
import datetime
import time


def main():
    filenames = os.listdir(no_pose_path)
    filenames.sort()

    filenames2 = os.listdir(pose_path)
    filenames2.sort()
    for pose in filenames2:
        print(pose)
        # text = json.loads(open())
        with open(pose_path+pose, 'r') as load_f0:
            load_dict = json.load(load_f0)
            pose_data = load_dict['pose']

        print(no_pose_path+'0000'+pose)

        with open(no_pose_path+'0000'+pose, 'r') as load_f:
            load_dict = json.load(load_f)


            load_dict["pose"] = pose_data
            #
            # xx = json.dumps(load_dict)
            # load_f.write(xx)

        with open(result_path+pose, 'w') as load_f1:
            json_str = json.dumps(load_dict)
            load_f1.write(json_str)



if __name__=='__main__':
    no_pose_path = '/media/wan/bei/2021-7/galios/kitti08_remove_dynamic/'
    pose_path = '/media/wan/bei/2021-7/SG_PR_DATA/graphs_sk/08/'
    result_path = '/media/wan/bei/2021-7/galios/remove_dynamic/08/'
    main()
