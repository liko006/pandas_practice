
# example part 6-13

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('./stock price.xlsx', index_col='id')
df2 = pd.read_excel('./stock valuation.xlsx', index_col='id')

df3 = df1.join(df2)
print(df3)
print()

df4 = df1.join(df2, how='inner')
print(df4)
print()
