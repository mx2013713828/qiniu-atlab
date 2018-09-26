# coding:utf-8
#myf-tools
#compute pr and ap

import matplotlib.pyplot as plt
%matplotlib inline
import itertools
import numpy as np


#画pr图计算ap
def plot_pr_ap(pred,gt):
    x = []
    y = []
    for thr in np.arange(0.01,1.0,0.01):
        recall,precision = compute_pr(pred=pred,gt=gt,throuh=thr)
    #     print recall,precision
        y.append(precision)
        x.append(recall)

    #计算ap
    ap = 0
    for i in range(len(x)-1):
        ap = ap+(x[i]-x[i+1])*y[i]
    print ap


    plt.figure(1) # 创建图表1
    plt.title('Precision/Recall Curve')# give plot a title
    plt.xlabel('Recall')# make axis labels
    plt.ylabel('Precision')

    #x、y都是列表，里面存的分别是recall和precision


    plt.figure(1)
    plt.plot(x, y)
    plt.show()
#     plt.savefig('p-r.png')

#计算pr
def compute_pr(pred,gt,throuh):
    tp = float(0)
    fp = float(0)
    fn = float(0)
    tn = float(0)
    for i in range(len(pred)):
        predict = pred[i]
        groundtruth = gt[i]
        if predict>throuh:
            if groundtruth ==1:
                tp = tp+1
            elif groundtruth ==0:
                fp = fp+1
        if predict<throuh:
            if groundtruth ==1:
                fn = fn+1
            elif groundtruth ==0:
                tn = tn+1
    recall = tp/(tp+fn)
    precision = tp/(tp+fp)
    return recall,precision
