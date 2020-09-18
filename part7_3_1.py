
# example part 7-4

import pandas as pd
import seaborn as sns

# step 1 데이터 준비
df = sns.load_dataset('titanic')
print(df.head())
print()

pd.set_option('display.max_columns', 15)
print(df.head())
print()

# step 2 데이터 탐색
print(df.info())

# 누락데이터가 많은 deck열과 embarked열과 중복되는 embark_town열을 제거
rdf = df.drop(['deck','embark_town'], axis=1)
print(rdf.columns.values)

# age열의 누락데이터가 있는 행들을 삭제한다 (데이터가 없는 곳에 평균 age로 치환하는 방법도 가능)
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))

# embarked 열의 NaN 값을 승선도시 중 최빈값으로 치환
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)
print()

print(rdf.describe(include='all'))
print()

rdf['embarked'].fillna(most_freq, inplace=True)

# step 3 분석에 사용할 속성 선택
ndf = rdf[['survived','pclass','sex','age','sibsp','parch','embarked']]
print(ndf.head())

# sex와 embarked 열의 범주형 데이터를 숫자형으로 변환 (더미 변수를 만드는 one-hot-encoding)
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_town = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_town], axis=1)

ndf = ndf.drop(['sex','embarked'], axis=1, inplace=True)
print(ndf.head())
print()

# step 4 데이터 셋 구분 train/test
X = ndf[['pclass','age','sibsp','parch','female','male','town_C','town_Q','town_S']]
y = ndf['survived']

# 설명변수 데이터를 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)

# step 5 KNN 분류 모형 - sklearn
from sklearn.neighbors import KNeighborsClassifier

# 모형 객체 생성 (k=5r)
knn = KNeighborsClassifier(n_neighbors=5)

# train data로 학습
knn.fit(X_train, y_train)

# test data로 y_hat 예측
y_hat = knn.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])
print()

# 모형 성능 평가 - Confusion Matrix
from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test,y_hat)
print(knn_matrix)
print()

# 모형 성능 평가 - 평가 지표 계산
knn_report = metrics.classification_report(y_test,y_hat)
print(knn_report)
print()
