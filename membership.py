from code import Xi
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import math 

miu = []
cluster = 4
cols = 52
nums = 177

center = pd.read_csv('C.csv', header=None)
sigmadf = pd.read_csv('S.csv', header=None)
sigma = sigmadf.iloc[0].values
df = pd.read_csv('noPCA.csv')
dataCSV = pd.read_csv('noScale.csv')
dataCSV['member'] = 7


def membershipFunction():
    for x in range(nums):
        row = []
        rowdata = df.iloc[x].values
        for i in range (cluster):
            centerdata = center.iloc[i].values
            ans = 0
            for j in range(cols):
                ans += ((rowdata[j]-centerdata[j]) / ( math.sqrt(2)*sigma[j])) ** 2 
            math.exp(ans * -1)
            row.append(ans)
        miu.append(row)
        dataCSV.at[x,'member'] = row.index(max(row))



# print(miu)
# print(dataCSV.head())
# dataCSV.to_csv('hasilFSC.csv',sep=',',decimal='.')
# for i in range (cluster):
#     dfSlice = dataCSV.loc[dataCSV['member'] == i]
#     name = 'member' +  str(i) + '.csv'
#     dfSlice.describe().to_csv(name)

