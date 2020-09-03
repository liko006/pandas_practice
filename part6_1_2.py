
# example part 6-3

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[: ,['age','fare']]
print(df.head())
print()

def missing_value(series):
    return series.isnull()

result = df.apply(missing_value, axis=0)
print(result.head())
print()
print(type(result))
print()

# example part 6-4

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[: ,['age','fare']]
print(df.head())
print()

def min_max(x):
    return x.max() - x.min()

result = df.apply(min_max)
print(result)
print()
print(type(result))
print()

# example part 6-5

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[: ,['age','fare']]
df['ten'] = 10
print(df.head())
print()

def add_two_obj(a,b):
    return a + b

df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)
print(df.head())
