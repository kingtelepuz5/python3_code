from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
from sklearn.datasets import load_wine
import numpy as np

x1 = np.array([0, 1])
x2 = np.array([2, 0])

print(np.sqrt(((x1-x2)**2).sum()))
print(np.sqrt(5))

data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)
print(wine.shape)
print(wine.columns)
print(wine.iloc[:,:3].describe())

scatter_matrix(wine.iloc[:,[0,5]])
plt.show()
