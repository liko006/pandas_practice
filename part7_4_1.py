
# example part 7-7

# k-means 군집 분석

import pandas as pd
import matplotlib.pyplot as plt

# step 1 데이터 준비

# Wholesale customers 데이터 셋 (UCI ML repository)
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)

# step 2 데이터 탐색

print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

# step 3 데이터 전처리

X = df.iloc[:,:]
print(X[:5])
print()

from sklearn import preprocessing
X = preprocessing.StandardScaler.fit(X).transfrom(X)

print(X[:5])
print()

# step 4 k-means 군집 모형 - sklearn

from sklearn import cluster

# 모형 객체
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

# 모형 학습
kmeans.fit(X)

# 예측
cluster_label = kmeans.labels_
print(cluster_label)
print()

df['Cluster'] = cluster_label
print(df.head())
print()
