
# example part 7-5

import pandas as pd
import seaborn as sns

# step 1 데이터 준비

df = sns.load_dataset('titanic')

pd.set_option('display.max_columns', 15)

# step 2 데이터 탐색/전처리

rdf = df.drop(['deck','embark_town'], axis=1)
rdf = df.dropna(subset=['age'], how='any', axis=0)

most_frq = rdf['embarked'].value_counts(dropna=True).idxmax()
rdf['embarked'].fillna(most_frq, inplace=True)

# step 분석에 사용할 속성

ndf = rdf[['survived','pclass','sex','age','sibsp','parch','embarked']]

# 원핫코핫
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_town = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_town], axis=1)

ndf.drop(['sex','embarked'], axis=1, inplace=True)

# step 4 데이터 셋 구분

X = ndf [['pclass','age','sibsp','parch','female','male','town_C','town_Q','town_S']]
y = ndf['survived']

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)

# step 5 SVM 분류 모형 - sklearn 사용
from sklearn import svm

svm_model = svm.SVC(kernel='rbf')
svm_model.fit(X_train, y_train)

y_hat = svm_model.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])
print()

# 모형 성능 평가
from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)
print()

svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)
