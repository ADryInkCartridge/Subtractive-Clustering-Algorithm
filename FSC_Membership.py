import pandas as pd
from sklearn.manifold import TSNE
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Membership
miu = []
cluster = 4


# FSC
r = 1.7
accept_ratio = 0.5
reject_ratio = 0.15
squash_factor = 1.25
minmax = []
clusters = []

# center = pd.read_csv('C.csv', header=None)
# sigmadf = pd.read_csv('S.csv', header=None)
# sigma = sigmadf.iloc[0].values
# df = pd.read_csv('noPCA.csv')
dataCSV = pd.read_csv('noScale.csv')

nums, cols = dataCSV.shape
print(nums)
print(cols)
# dataCSV['member'] = 7

check1 = []
check2 = []
check3 = []
check4 = []


def membershipFunction():
    for x in range(nums):
        # Name = input("Please enter your name?")
        row = []
        rowdata = dataCSV.iloc[x].values
        for i in range(len(clusters)):
            centerdata = clustDF.iloc[i].values
            ans = 0
            for j in range(cols):
                ans += ((rowdata[j]-centerdata[j]) /
                        (math.sqrt(2)*sigma[j])) ** 2
                # print(
                #     f'X{i}{j} = {rowdata[j]} - {centerdata[j]} / akar2 * {sigma[j]}')
            ans = math.exp(ans * -1)
            row.append(ans)
        miu.append(row)
        dataCSV.at[x, 'member'] = row.index(max(row)) + 1
        if(row.index(max(row)) + 1 == 1):
            check1.append(x)
        if(row.index(max(row)) + 1 == 2):
            check2.append(x)
        if(row.index(max(row)) + 1 == 3):
            check3.append(x)
        if(row.index(max(row)) + 1 == 3):
            check4.append(x)


def normalize():
    x = 0
    for i in (dataCSV.columns.values):
        xmin = dataCSV[i].min() - 1
        xmax = dataCSV[i].max() + 1
        dataCSV[i] = (dataCSV[i]-xmin)/(xmax-xmin)
        minmax.append([xmin, xmax])


def potensi():
    total = []
    for i in range(nums):
        TData = dataCSV.loc[i]
        d = 0
        for j in range(nums):
            rowData = dataCSV.loc[j]
            ds = 0
            for k in range(cols):
                ds += ((TData[k] - rowData[k]) / r) ** 2
            # print(ds)
            d += math.exp(-4 * ds)
        # Kasus 3.4
        # if(i <= 19):
        #     d *= 0.4
        # else:
        #     d *= 0.6
        total.append(d)
    return total

# print(potensiAkhir[j])
# print(potensiAwal[j])
# ans = [round(elem, 4) for elem in potensiAkhir]
# print(ans)


def iterPotensi():
    M = max(potensiAkhir)
    loopcount = 1
    flag = False
    Z = max(potensiAkhir)
    idx = potensiAkhir.index(max(potensiAkhir))
    TData = dataCSV.loc[idx]
    while(1):
        print(loopcount)
        loopcount += 1
        # Name = input("Please enter your name?")
        potensiAwal = potensiAkhir.copy()
        if (Z/M > accept_ratio):
            clusters.append(TData)
            print(
                f"Index : {idx+1} accepted with an acceptance ratio of {Z/M} and Z value of {Z}")
            flag = True
        elif((Z/M < accept_ratio) and (Z/M > reject_ratio)):
            md = -1
            sd = 0
            # print(TData)
            for j in range(len(clusters)):
                sd = 0
                for k in range(cols):
                    sd += ((TData[k] - clusters[j][k]) / r) ** 2
                # print(
                #     f"Index : MD = {md} SD = {sd}")
                if (md > sd or (md < 0)):
                    md = sd
            if((Z/M) + math.sqrt(md) >= 1):
                # print(
                #     f"Index : Rasio = {Z/M} MDS = {math.sqrt(md)}")
                clusters.append(TData)
                print(
                    f"Index : {idx+1} accepted with the ratio + mds of {(Z/M) + math.sqrt(md)} and Z value of {Z}")
                flag = True
            else:
                print(
                    f"Index : {idx+1} Rejected with ratio + mds of {(Z/M) + math.sqrt(md)} and Z value of {Z}")
                flag = False
        else:
            print(
                f"Index : {idx+1} Rejected with ratio of {(Z/M)} and Z value of {Z}")
            flag = False
        if(max(potensiAkhir) == 0):
            break

        if(flag == True):
            # print(next)
            flag = False
            for j in range(nums):
                rowData = dataCSV.loc[j]
                s = 0
                for k in range(cols):
                    s += ((clusters[-1][k] - rowData[k]) /
                          (r * squash_factor)) ** 2
                potensiAkhir[j] = M * math.exp(-4 * s)
                # print(f"{potensiAwal[j]} - {potensiAkhir[j]}")
                potensiAkhir[j] = potensiAwal[j] - potensiAkhir[j]
                if (potensiAkhir[j] < 0):
                    potensiAkhir[j] = 0
            Z = max(potensiAkhir)
            idx = potensiAkhir.index(max(potensiAkhir))
            TData = dataCSV.loc[idx]
        else:
            potensiAkhir[idx] = 0
            Z = max(potensiAkhir)
            idx = potensiAkhir.index(max(potensiAkhir))
            TData = dataCSV.loc[idx]
        # print(potensiAkhir)
    return


def denormalize():
    x = 0
    for i in (dataCSV.columns.values):
        dataCSV[i] = dataCSV[i] * (minmax[x][1] - minmax[x][0]) + minmax[x][0]
        clustDF[i] = clustDF[i] * (minmax[x][1] - minmax[x][0]) + minmax[x][0]
        sigma.append(r * (minmax[x][1] - minmax[x][0]) / math.sqrt(8))
        x += 1


normalize()
# print(len(clusters))
potensiAwal = potensi()
potensiAkhir = potensiAwal.copy()
# print(potensiAwal)
iterPotensi()
print(len(clusters))
clustDF = pd.DataFrame(clusters)
print(clustDF)
# minmax = [[0, 50000000], [0, 70000000], [0, 120], [0, 50000000]]
sigma = []
denormalize()
print(clustDF)
print(clustDF.shape)
print(sigma)
scaler = MinMaxScaler()
data = scaler.fit_transform(dataCSV)

X_embedded = TSNE(n_components=2, random_state=1).fit_transform(data)
membershipFunction()

miuDF = pd.DataFrame(miu)
print(miuDF)
# miuDF.to_csv('miu.csv', sep=';', decimal=',')
print(dataCSV)
print(check1)
print(check2)
print(check3)
print(check4)


df = pd.DataFrame()
df['target'] = dataCSV['member']
df['x'] = X_embedded[:, 0]
df['y'] = X_embedded[:, 1]

print(df.head())
print(df.tail())
plt.figure(figsize=(16, 7))
sns.scatterplot(x='x', y='y', hue='target', palette=sns.color_palette("hls", len(clusters)), data=df,
                legend="full")
plt.show()
# dataCSV.to_csv('hasilFSCBuku.csv', sep=',', decimal='.')
# for i in range (cluster):
#     dfSlice = dataCSV.loc[dataCSV['member'] == i]
#     name = 'member' +  str(i) + '.csv'
#     dfSlice.describe().to_csv(name)
