
# -*- coding:utf-8 -*-
# Author:huaixiangdong

import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ZGLT=ts.get_hist_data('600050',ktype='W',start='2016-01-01',end='2018-03-31')
ZGLT_close0=ZGLT['close']
#ZGLT.p_change=ZGLT['p_change']
print(ZGLT_close0)
#print(ZGLT.p_change)
ZGLT_Return=np.zeros(len(ZGLT_close0))
for i in range(len(ZGLT_close0)-1):
       ZGLT_Return[i+1]=(ZGLT_close0[i+1]-ZGLT_close0[i])/ZGLT_close0[i]
for i in range(len(ZGLT_Return)):
       if ZGLT_Return[i]<-0.04:
           ZGLT_Return[i]=0.01
#for i in range(len(ZGLT_Return)-1):
#      ZGLT_close1[i+1]= ZGLT_Return[i+1]*ZGLT_close0[i]+ZGLT_close0[i]

import matplotlib.pyplot as plt
plt.plot(ZGLT_close0, marker='o', label='ZGLT_close0')
# plt.plot(ZGLT_close1, marker='*',label='ZGLT_close1')
plt.legend()
plt.show()