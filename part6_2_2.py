
# example part 6-8

import pandas as pd

df = pd.read_excel('./주가데이터.xlsx')
print(df.head())
print()
print(df.dtypes)
print()

df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head())
print()

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df.head())
print()
