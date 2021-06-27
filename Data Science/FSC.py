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

df = pd.read_csv('testdata177n2.csv', header=None)
df['a'] = df[0]
df['b'] = df[1]
df = df.drop([0,1],axis=1)
df['a'] -= xmin1
df['b'] -= xmin2
df['a'] /= deltax1
df['b'] /= deltax2
arr = df.to_numpy()
print(arr)

for clusters in range (3):
    for index in range (177):
        x,y = arr[index]
        arr2 = arr
        for index2 in range(177):
            arr2[index2][0] -= x
            arr2[index2][1] -= y
            arr2[index2][2] = arr2[index2][0] ** 2 + arr2[index2][1] ** 2 
            arr2[index2][3] = math.exp(arr2[index2][2] * -4)