
# example part 6-19

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex','class','fare','survived']]

grouped = df.groupby(['class', 'sex'])

gdf = grouped.mean()
print(gdf)
print()
print(type(gdf))
print()

print(gdf.loc['First'])
print()

print(gdf.loc[('First', 'female')])
print()
