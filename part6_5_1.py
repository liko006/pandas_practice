
# example part 6-14

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex','class','fare','survived']]

print('승객 수:', len(df))
print(df.head())
print()

grouped = df.groupby(['class'])
print(grouped)
print()

for key, group in grouped:
    print('* key:', key)
    print('* number:', len(group))
    print(group.head())
    print()

average = grouped.mean()
print(average)
print()

group3 = grouped.get_group('Third')
print(group3.head())
print()

grouped_two = df.groupby(['class','sex'])

for key, group in grouped_two:
    print('* key:', key)
    print('* number:', len(group))
    print(group.head())
    print()
    
average_two = grouped_two.mean()
print(average_two)
print()
print(type(average_two))
print()

group3_two = grouped_two.get_group(('Third', 'female'))
print(group3_two.head())
print()
