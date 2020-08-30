
# example part 5-6

import pandas as pd

df = pd.DataFrame({'c1':['a','a','b','a','b'], 'c2':[1,1,1,2,2], 'c3':[1,1,2,2,2]})

print(df)
print()

# duplicacity of entire row
df_dup = df.duplicated()
print(df_dup)
print()

# duplicacity of data in a column
col_dup = df['c2'].duplicated()
print(col_dup)
print()
