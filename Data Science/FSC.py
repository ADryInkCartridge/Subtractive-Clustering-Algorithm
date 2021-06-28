import numpy as np
import pandas as pd
import math

r = 0.3
accept_ratio = 0.5
reject_ratio = 0.15
squash_factor = 1.25
xmin1 = -9
xmin2 = -1.5
xmax1 = 3
xmax2 = 1.5
deltax1 = xmax1 - xmin1
deltax2 = xmax2 - xmin2

df = pd.read_csv('Data Science/testdata177n2.csv', header=None)
df['a'] = df[0]
df['b'] = df[1]
df = df.drop([0,1],axis=1)
df['a'] -= xmin1
df['b'] -= xmin2
df['a'] /= deltax1
df['b'] /= deltax2
arr = df.to_numpy()
print(arr)

z = np.zeros((177,4), dtype=float)
acceped = []
i4vals = []
i4vals2 = []

for index in range (177):
    x,y = arr[index]
    arr2 = arr
    maxval = 0
    arr2 = (np.append(arr2, z, axis=1))
    for index2 in range(177):
        arr2[index2][0] -= x
        arr2[index2][1] -= y
        arr2[index2][2] = arr2[index2][0] ** 2 + arr2[index2][1] ** 2 
        arr2[index2][3] = math.exp(arr2[index2][2] * -4)
        maxval+=arr2[index2][3]
    i4vals.append(maxval)


maximum = max(i4vals)
x,y = arr[i4vals.index(maximum)]
arr2 = arr
arr2 = (np.append(arr2, z, axis=1))
for index2 in range(177):
    arr2[index2][0] -= x
    arr2[index2][1] -= y
    arr2[index2][2] = arr2[index2][0] ** 2 + arr2[index2][1] ** 2 
    arr2[index2][3] = math.exp(arr2[index2][2] * -4)
    i4vals2.append(arr2[index2][3])

acceped.append(arr2[i4vals.index(maximum)])
acceped[0][0],acceped[0][1] = arr[i4vals.index(maximum)]
acceped[0][2] = acceped[0][0]** 2 + acceped[0][1] ** 2
acceped[0][3] = math.exp(acceped[0][2] * -4)

for clusters in range (2):
    check = []
    x,y = acceped[-1][0],acceped[-1][1]
    arr2 = arr
    maxval = 0
    arr2 = (np.append(arr2, z, axis=1))
    for index2 in range(177):
            arr2[index2][0] -= x
            arr2[index2][1] -= y
            arr2[index2][2] = arr2[index2][0] ** 2 + arr2[index2][1] ** 2 
            arr2[index2][3] = math.exp(arr2[index2][2] * acceped[-1][3])
            arr2[index2][4] = i4vals2[index2]
            arr2[index2][5] = arr2[index2][3] - arr2[index2][4]
            i4vals2[index2] = arr2[index2][5]
    maximum = max(i4vals2)
    if(clusters == 0 and maximum/acceped[-1][3] > accept_ratio):
        acceped.append(arr2[i4vals2.index(maximum)])
        acceped[-1][0] += x
        acceped[-1][1] += y
    elif (maximum/acceped[-1][5] > accept_ratio):
        acceped.append(arr2[i4vals2.index(maximum)])
        acceped[-1][0] += x
        acceped[-1][1] += y
print(acceped)

clust = pd.DataFrame(acceped,columns=['x','y','d','dc','dbefore','deltaD'])
print(clust.head())
clust['x'] *= xmax1
clust['y'] *= xmax2

sigma1 = r * xmax1 / math.sqrt(8)
sigma2 = r * xmax2 / math.sqrt(8)

df = pd.read_csv('Data Science/testdata177n2.csv', header=None)
df['a'] = df[0]
df['b'] = df[1]
df = df.drop([0,1],axis=1)
df['sigma1'] = sigma1
df['sigma2'] = sigma2

for index, row in clust.iterrows():
    locx = 'x' + str(index)
    locy = 'y' + str(index)
    df[locx] = row['x']
    df[locy] = row['y']
print(df.head())

for index in range (3):
    locx = 'x' + str(index)
    locy = 'y' + str(index)
    miu = 'miu' + str(index)
    df[miu] = np.exp((df['a']-df[locx])/(math.sqrt(2)*df['sigma1']) ** 2 + (df['b']-df[locy])/(math.sqrt(2)*df['sigma2'])**2)
df['max'] = df[['miu0','miu1','miu2']].max(axis=1)
print(df.head())

for index, row in df.iterrows():
    if (row['max']==row['miu0']):
         df.at[index,'cluster']= 0
    elif (row['max']==row['miu1']):
        df.at[index,'cluster']= 1
    else:
        df.at[index,'cluster']= 2
print(df.head())
df.to_csv('pleaseWork.csv',sep=';',decimal=",")
df.to_excel('pleaseWork.excel')