import json
import os
import datetime
from numpy.core.arrayprint import printoptions
from utils import tab_printer
from sg_net import SGTrainer
from parser_sg import sgpr_args
import numpy as np
from tqdm import tqdm
import os
import sys
from matplotlib import pyplot as plt
from sklearn import metrics
from utils import *
from utils import tab_printer
from sg_net import SGTrainer
from parser_sg import sgpr_args
import linecache
import datetime

def main():

    key_frame =[]
    json_dir = ''        #dir path
    filenames = os.listdir(json_dir)
    filenames.sort()
    frame_num = len(filenames)
    key_frame_threshold  = 0.8
    start = 200
    follow = 201


    time1 = str(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))

    while follow < frame_num:
        x = sim(start, follow)
        with open(time1 + '_gene_key_frame.txt', 'a') as f:
            f.write(str(start) + ' ' + str(follow) + ' ' + str(x) + '\n' + str(key_frame[-1]) + '\n')

        if x > key_frame_threshold:
            follow += 1
        else:
            key_frame.append(follow)  # key_frame.append(follow + 1) generate key frames
            start = follow
            follow = start + 1

    time2 = str(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
    with open( time2+ '_key_frame.txt','a') as f:
        for key_fra in key_frame:
            f.write(str(key_fra) + '\n')
    time2_1 = str(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
    with open(time2_1 + '_key_frame_list.txt','a') as f:
        for key_fra in key_frame:
            f.write(str(key_fra) + ',')


def sim(frame_a, frame_b):
    file_a = file_path + linecache.getline('./jsonlist.txt', frame_a + 1).strip() + '.json'
    file_b = file_path + linecache.getline('./jsonlist.txt', frame_b + 1).strip() + '.json'
    # return graph_sim(file_a,file_b)
    print(file_a, file_b)
    pair_file = [file_a, file_b]
    args = sgpr_args()
    args.load('./config/config.yml')
    tab_printer(args)
    trainer = SGTrainer(args, False)
    trainer.model.eval()
    pred, gt = trainer.eval_batch_pair([pair_file, ])
    print("Score:", pred[0])
    return pred[0]




if __name__=='__main__':

    main()
    #.sort()

