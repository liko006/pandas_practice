
# example part 7-3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 1 ~ 3 데이터 준비
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

ndf = df[['mpg','cylinders','horsepower','weight']]

# step 4 데이터셋 구분 - train/test
X = ndf[['cylinders','horsepower','weight']]
y = ndf['mpg']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)

# step 5 다중회귀분석 - sklearns
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train, y_train)

r_sq = lr.score(X_test, y_test)
print(r_sq)
print()

print('X 변수의 계수 a: ', lr.coef_)
print()
print('상수항 b: ', lr.intercept_)

# 산점도와 예측 그래프
y_hat = lr.predict(X_test)

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y_test, hist=False, label='y_test')
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)
plt.show()
plt.close()
