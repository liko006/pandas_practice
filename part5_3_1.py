
# example part 5-9

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

print(df.dtypes)
print()

print(df['horsepower'].unique())
print()

import numpy as np

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df['horsepower'].dtypes)
print()

print(df['origin'].unique())

df['origin'].replace({1:'US', 2:'EU', 3:'JP'}, inplace=True)

print(df['origin'].unique())
print(df['origin'].dtypes)

df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)

print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
