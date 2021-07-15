from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('noScale.csv')


print(df.head())
scaler = MinMaxScaler()
data = scaler.fit_transform(df)

# tot = 0.

# for i in range(data.shape[0]-1):
#     tot += ((((data[i+1:]-data[i])**2).sum(1))**.5).sum()

# avg = tot/((data.shape[0]-1)*(data.shape[0])/2.)

X_embedded = TSNE(n_components=2, random_state=1).fit_transform(data)
plt.scatter(X_embedded[:, 0], X_embedded[:, 1])
plt.show()
