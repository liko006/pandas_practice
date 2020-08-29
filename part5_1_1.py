
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

