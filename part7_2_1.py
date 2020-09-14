
# example part 7-1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 1 데이터 준비
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

print(df.head())
print()

pd.set_option('display.max_columns', 10)
print(df.head())
print()

# step 2 데이터 탐색
print(df.info())
print()

print(df.describe())
print()

print(df['horsepower'].unique())
print()

df['horsepower'].replace('?', np.nan, inplace=True)     # ? -> NaN 으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)  # 누락 데이터 행 삭제
df['horsepower'] = df['horsepower'].astype('float')

print(df.describe())
print()

# step 3 속성 (feature or variable) 선택
ndf = df[['mpg','cylinders','horsepower','weight']]
print(ndf.head())

# mpg(종속)와 다른 변수간의 선형관계를 산점도로 확인
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10,5))
plt.show()
plt.close()

# seaborn으로 산점도 그리기
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg=False)  # No reg. line 
plt.show()
plt.close()

sns.jointplot(x='weight', y='mpg', data=ndf)
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf)
plt.show()
plt.close()

grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()

# step 4 데이터셋 구분 - train/test
X=ndf[['weight']]   # 독립변수
Y=ndf[['mpg']]      # 종속변수

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)

print('train data 개수: ', len(X_train))
print('test data 개수: ', len(X_test))
