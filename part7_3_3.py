
# example part 7-6

import pandas as pd
import numpy as np

# step 1 데이터 준비/기본 설정

uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases//breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

df.columns = ['id','clump','cell_size','cell_shape','adhesion','epithlial','bare_nuclei','chromatin','normal_nucleoli','mitoses','class']

pd.set_option('display.max_columns', 15)

# step 2 데이터 탐색

print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

print(df['bare_nuclei'].unique())
print()

df['bare_nuclei'].replace('?', np.nan, inplace=True)
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)
df['bare_nuclei'] = df['bare_nuclei'].astype('int')
print(df.describe())
print()

# step 3 데이터 셋 구분

X = df[['clump','cell_size','cell_shape','adhesion','epithlial','bare_nuclei','chromatin','normal_nucleoli','mitoses']]
y = df['class']

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_spilt
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
print()

# step 4 Decision Tree 분류 모형 - sklearn
from sklearn import tree

# 모형 객체 생성
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)

# 모형 학습
tree_model.fit(X_train, y_train)

# 결과 예측
y_hat = tree_model.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])
print()

# 모형 성능 평가
from sklearn import metrics
tree_matrix = metrics.confusion_matrix(y_test,y_hat)
print(tree_matrix)
print()

tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)
