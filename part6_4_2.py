
# example part 6-12

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')

print(df1)
print()
print(df2)
print()

merge_inner = pd.merge(df1,df2)
print(merge_inner)
print()

merge_outer = pd.merge(df1,df2, how='outer', on='id')
print(merge_outer)
print()
