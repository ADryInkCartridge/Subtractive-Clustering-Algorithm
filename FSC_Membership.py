import pandas as pd
import math

# Membership
miu = []
cluster = 4


# FSC
r = 0.3
accept_ratio = 0.5
reject_ratio = 0.15
squash_factor = 1.25
minmax = []
clusters = []

center = pd.read_csv('C.csv', header=None)
sigmadf = pd.read_csv('S.csv', header=None)
sigma = sigmadf.iloc[0].values
df = pd.read_csv('noPCA.csv')
dataCSV = pd.read_csv('buku.csv')

nums, cols = dataCSV.shape
print(nums)
print(cols)
# dataCSV['member'] = 7


def membershipFunction():
    for x in range(nums):
        row = []
        rowdata = df.iloc[x].values
        for i in range(cluster):
            centerdata = center.iloc[i].values
            ans = 0
            for j in range(cols):
                ans += ((rowdata[j]-centerdata[j]) /
                        (math.sqrt(2)*sigma[j])) ** 2
            math.exp(ans * -1)
            row.append(ans)
        miu.append(row)
        dataCSV.at[x, 'member'] = row.index(max(row))


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
        # print(d)
        total.append(d)
    return total

# print(potensiAkhir[j])
# print(potensiAwal[j])
# ans = [round(elem, 4) for elem in potensiAkhir]
# print(ans)


def iterPotensi():
    while(1):
        Name = input("Please enter your name?")
        potensiAwal = potensiAkhir.copy()
        idx = potensiAkhir.index(max(potensiAkhir))
        TData = dataCSV.loc[idx]
        print(clusters[-1])
        for j in range(nums):
            rowData = dataCSV.loc[j]
            s = 0
            for k in range(cols):
                s += ((clusters[-1][k] - rowData[k]) /
                      (r * squash_factor)) ** 2
            potensiAkhir[j] = M * math.exp(-4 * s)
            potensiAkhir[j] = potensiAwal[j] - potensiAkhir[j]
            if (potensiAkhir[j] < 0):
                potensiAkhir[j] = 0
        Z = max(potensiAkhir)
        print(potensiAkhir)
        if (Z/M > accept_ratio):
            idx = potensiAkhir.index(max(potensiAkhir))
            TData = dataCSV.loc[idx]
            clusters.append(TData)
            print(
                f"Index : {idx} accepted with an acceptance ratio of {Z/M} and Z value of {Z}")
        elif((Z/M < accept_ratio) and (Z/M > reject_ratio)):
            md = -1
            sd = 0
            for j in range(len(clusters)):
                for k in range(cols):
                    sd += ((clusters[j][k] - rowData[k]) / r) ** 2
                if (md > sd or (md == -1 and j == 0)):
                    md = sd
            if((Z/M) + math.sqrt(md) >= 1):
                clusters.append(TData)
                print(
                    f"Index : {idx} accepted with the ratio + mds of {(Z/M) + math.sqrt(md)} and Z value of {Z}")

        elif(max(potensiAkhir) == 0):
            break

        potensiAkhir[idx] = 0
    return


# normalize()
potensiAwal = potensi()
potensiAkhir = potensiAwal.copy()
idx = potensiAkhir.index(max(potensiAkhir))
TData = dataCSV.loc[idx]
print(f"Index : {idx} accepted")
M = max(potensiAkhir)
clusters.append(TData)
# print(potensiAwal)
iterPotensi()
print(clusters)


# print(miu)
# print(dataCSV.head())
# dataCSV.to_csv('hasilFSC.csv',sep=',',decimal='.')
# for i in range (cluster):
#     dfSlice = dataCSV.loc[dataCSV['member'] == i]
#     name = 'member' +  str(i) + '.csv'
#     dfSlice.describe().to_csv(name)
