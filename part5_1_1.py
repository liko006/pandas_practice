
# example part 5-1 (Checking NaN data)

import seaborn as sns

df = sns.load_dataset('titanic')

df.head()
df.info()

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)

print(df.head().isnull())

print(df.head().notnull())

print(df.head().isnull().sum(axis=0))

# example part 5-2 (Deleting NaN data)

import seaborn as sns

df = sns.load_dataset('titanic')

missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()
    
    try:
        print(col, ': ', missing_count[True])
    except:
        print(col, ': ', 0)

# droping 'deck' column
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

# deleting rows which have NaN in 'age' column
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))

# example part 5-3 (Replacing NaN by mean of a column)

import seaborn as sns

df = sns.load_dataset('titanic')

print(df['age'].head(10))  # NaN in 5th row
print()

mean_age = df['age'].mean(axis=0)  # mean of 'age' column
df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))

# example part 5-4 (Replacing NaN by most freq. data in a column)

import seaborn as sns

df = sns.load_dataset('titanic')

print(df['embark_town'][825:830])
print()

most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)
print()

df['embark_town'].fillna(most_freq, inplace=True)

print(df['embark_town'][825:830])
