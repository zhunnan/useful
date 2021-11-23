import os
import numpy as np
from sklearn import metrics

def main():
    pc_scores = '/media/wan/bei/2021-9/SG_PR-master/eva/'
    img_scores = '/media/wan/bei/2021-8/SG_PR-master/eva/eva1009/'

    p00 = np.load(pc_scores+'00_DL_db.npy')
    i00 = np.load(img_scores+'00_DL_db.npy')
    gt = np.load(pc_scores+'00_gt_db.npy')
    # igt = np.load(img_scores+'00_gt_db.npy')
    # print(pgt==igt)
    # print(p00.shape)
    # print(i00.shape)
    alphas = np.linspace(0,1,num=21)
    for alpha in alphas:
        beta = 1- alpha
        weigt_score = alpha*p00+beta*i00
        print(alpha,beta)
        precision, recall, pr_thresholds = metrics.precision_recall_curve(gt,weigt_score)
        F1_score = 2 * precision * recall / (precision + recall)
        F1_score = np.nan_to_num(F1_score)
        F1_max_score = np.max(F1_score)
        print(F1_max_score)

if __name__=='__main__':

    main()