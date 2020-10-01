
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
