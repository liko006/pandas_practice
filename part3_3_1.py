
# example part 3-4

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South', 'North']
df_ns.colums = df_ns.columns.map(int)

print(df_ns.head())
print()
df_ns.plot()

# 시간에 따른 발전전력량을 보기 위해서는, 
# 연도가 columns에 있으므로 T 함수를 이용해서 행과 열을 바꾸어 준다.
tdf_ns = df_ns.T
print(tdf_ns.head())
print()
tdf_ns.plot()

# example part 3-5

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South', 'North']
df_ns.colums = df_ns.columns.map(int)

tdf_ns = df_ns.T
print(tdf_ns.head())
print()
tdf_ns.plot(kind='bar')

# example part 3-6 

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South', 'North']
df_ns.colums = df_ns.columns.map(int)

tdf_ns = df_ns.T
tdf_ns.plot(kind='hist')

# example part 3-7

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df.plot(x='weight', y='mpg', kind='scatter')

# example part 3-8

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df[['mpg','cylinders']].plot(kind='box')
