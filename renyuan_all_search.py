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
import scipy.io

def main():
    key_frame = [1]
    i = 2
    # build key frames
    while i < img_num:
        if sim(i,key_frame[-1]) < threshold_alpha:
            key_frame.append(i)
        else:
            pass
        i+=1

    # start search
    # make result table
    my_result = np.zeros((img_num,3),dtype=int)
    for i in range(img_num):
        my_result[i][0] = i + 1


    flow = start_frame
    while flow < img_num:
        smallerThan = lambda x, y: [i for i in x if i < y]
        before_flow = smallerThan(key_frame, flow)
        first_batch = gene_batch(flow, before_flow)

        first_sim = trainer.eval_batch_pair(first_batch)
        if first_sim.max() > threshold_beta:
            second_batch, start = second_gene(flow, key_frame, first_sim)
            if second_batch != None:
                second_sim = trainer.eval_batch_pair(second_batch)
                if first_sim.max() > threshold_theta:
                    idx = np.argmax(second_sim)
                    if check_time(flow, idx):
                        my_result[flow-1][1]=idx
                        my_result[flow-1][2]=1

                else:
                    pass

            else:
                pass
        else:
            pass
        flow += 1

    pr,recall = pr_racall(my_result, gnd)



def pr_racall(my_result,gnd):

    data = scipy.io.loadmat(gnd)  # 读取mat文件
    gnds = data['truth']
    gnd_add= gnds.sum(axis=1)
    i=0
    tp,fp,fn,tn,er=0
    while i <= len(gnd_add) :
        if my_result[i][2]==1 and gnds[my_result[i][0],my_result[i][1]]==1:
            tp+=1
        elif my_result[i][2]==1 and gnds[my_result[i][0],my_result[i][1]]==0:
            fp+=1
        elif my_result[i][2]==0 and gnd_add[i]==1:
            fn+=1
        elif my_result[i][2]==0 and gnd_add[i]==0:
            tn+=1
        else
            er+=1

    if tp+fp+fn+tn == img_num and er !=0:
        pr = tp/(tp+fp)
        recall=tp/(tp+fn)
    else:
        pr, recall=0
    return pr,recall



def check_time(now_frame, return_frame):
    # 连续三帧检查
    if sim(now_frame+1,return_frame+1) > threshold_theta and sim(now_frame+2,return_frame+2)> threshold_theta:
        state = True
    else:
        state = False

    return state


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


def gene_batch(ref,list):
    list2 = []
    # file_path = '../SG_PR_DATA/graphs_rn/05/'
    list = list[0:-10]
    for i in range(len(list)):
        file_a = file_path + linecache.getline('./jsonlist.txt', ref + 1).strip() + '.json'
        file_b = file_path + linecache.getline('./jsonlist.txt', list[i] + 1).strip() + '.json'
        list2.append([file_a,file_b])
    return list2


def second_gene(flow,key_frame,first_sim):
    idx = np.argmax(first_sim)
    if idx >0 and idx <len(first_sim)-1:
        start = key_frame[idx-1]
        end = key_frame[idx+1]
        list = range(start,end)
        snd = gene_batch(flow,list)
    elif idx ==0:
        start =  key_frame[0]
        end =  key_frame[1]
        list = range(start, end)
        snd = gene_batch(flow, list)
    elif idx ==len(first_sim):
        start =  key_frame[idx-1]
        end =  key_frame[idx]
        list = range(start, end)
        snd = gene_batch(flow, list)
    else :
        start = None
        snd = None
    return snd,start



if __name__ == '__main__':
    path = ''
    img_num = len(path)
    # parameters
    threshold_alpha = 0.75   # guanjianzhen
    threshold_beta = 0.80    # 与关键帧列表的相似度阈值
    threshold_theta = 0.85    # 与关键帧列表间的相似度阈值

    start_frame = 200
    gnd= '/media/wan/bei/2021-8/SG_PR-master/img_groundtruth/KITTI_Ground/kitti00GroundTruth.mat'
    main()



