from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('noScale.csv')
clusters4 = [3, 4, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 3, 1, 3, 3, 3, 1, 3, 3, 3, 1, 3, 3, 3, 3, 1, 1, 3, 1, 1, 1, 4, 3, 3, 3, 3, 3, 3,
             1, 3, 1, 3, 4, 3, 3, 1, 1, 4, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 3,
             3, 1, 3, 4, 3, 1, 3, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3, 3, 1, 3, 3, 1, 4, 3,
             3, 3, 3, 3, 4, 3, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 1, 1, 1, 3,
             3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 4, 3, 3, 3, 1, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 3, 3, 2, 3, 1, 4, 4, 3, 1, 4, 1, 1, 3, 4, 3, 1, 3, 4, 4, 3, 3, 1, 2, 3, 3, 1, 1, 4, 3, 3, 3, 3, 1, 3, 3, 4, 3]

clusters3 = [3, 2, 1, 1, 3, 1, 1, 3, 3, 3, 3, 1, 3, 1, 3, 3, 3, 1, 3, 3, 3, 1, 3, 3, 3, 3, 1, 1, 3, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 1, 3, 1, 3, 2, 3, 3, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3,
             1, 3, 3, 3, 1, 3, 3, 1, 3, 2, 3, 1, 3, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3, 3, 1, 3, 3, 1, 2, 3, 3, 3, 3, 3, 2, 3, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 1, 1, 1, 3, 3,
             3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 2, 3, 3, 3, 1, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 3, 3, 1, 3, 1, 2, 2, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 2, 2, 3, 3, 1, 3, 3, 3, 1, 1, 2,
             3, 3, 3, 3, 1, 3, 3, 2, 3]
print(df.head())
scaler = MinMaxScaler()
data = scaler.fit_transform(df)

# tot = 0.

# for i in range(data.shape[0]-1):
#     tot += ((((data[i+1:]-data[i])**2).sum(1))**.5).sum()

# avg = tot/((data.shape[0]-1)*(data.shape[0])/2.)
X_embedded = TSNE(n_components=2, random_state=1).fit_transform(data)
df = pd.DataFrame()
df['target'] = clusters3
df['x'] = X_embedded[:, 0]
df['y'] = X_embedded[:, 1]
plt.figure(figsize=(16, 7))
sns.scatterplot(x='x', y='y', hue='target', palette=sns.color_palette("hls", 3), data=df,
                legend="full")
plt.show()
