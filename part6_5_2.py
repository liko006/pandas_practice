
# example part 6-15

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all)
print()
print(type(std_all))
print()

std_fare = grouped.fare.std()
print(std_fare)
print()
print(type(std_fare))
print()

def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg(min_max)
print(agg_minmax)
print()

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print()

agg_sep = grouped.agg({'fare':['min','max'], 'age':'mean'})
print(agg_sep.head())
print()

age_mean = grouped.age.mean()
print(age_mean)
print()

age_std = grouped.age.std()
print(age_std)
print()

for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key])/age_std.loc[key]
    print('* origin:', key)
    print(group_zscore.head(3))
    print()

def z_score(x):
    return (x - x.mean())/x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1,9,0]])
print()
print(len(age_zscore))
print()
print(age_zscore.loc[0:9])
print()
print(type(age_zscore))
print()

# example part 6-17

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex','class','fare','survived']]

grouped = df.groupby(['class'])

grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head())
print()
print(type(grouped_filter))
print()

age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.tail())
print()
print(type(age_filter))
print()
