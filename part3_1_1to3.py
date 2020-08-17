
# example part 3-1

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.head())
print()
print(df.tail())
print()

print(df.shape)
print()

print(df.info())
print()

print(df.dtypes)
print()
print(df.mpg.dtypes)
print()

print(df.describe())
print()
print(df.describe(include='all'))
print()

# example part 3-2

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.count())
print()
print(type(df.count()))
print()

unique_values = df['origin'].value_counts()
print(unique_values)
print()
print(type(unique_values))
print()
