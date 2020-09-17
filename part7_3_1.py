
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
