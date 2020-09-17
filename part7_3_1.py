
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
