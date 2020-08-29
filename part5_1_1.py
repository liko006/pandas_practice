
# example part 5-1

import seaborn as sns

df = sns.load_dataset('titanic')

df.head()
df.info()

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)

print(df.head().isnull())

print(df.head().notnull())

print(df.head().isnull().sum(axis=0))
