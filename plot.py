import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('noScale.csv')

print(df.head())
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
normal = scaler.fit_transform(df)

X_embedded = TSNE(n_components=2,random_state=1).fit_transform(normal)
plt.scatter(X_embedded[:, 0], X_embedded[:, 1])
