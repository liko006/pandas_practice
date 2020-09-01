
# example part 5-15

import pandas as pd

df = pd.read_csv('./stock-data.csv')

print(df.head())
print()
print(df.info())
print()

df['new_Date'] = pd.to_datetime(df['Date'])

print(df.head())
print()
print(df.info())
print()
print(type(df['new_Date'][0]))
print()

df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)

print(df.head())
print()
print(df.info())
print()
