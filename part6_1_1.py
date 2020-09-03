
# example part 6-1

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())

# user defined functions
def add_10(n):
    return n + 10

def add_two_obj(a,b):
    return a + b

print(add_10(10))
print(add_two_obj(10,10))

sr1 = df['age'].apply(add_10)                # n = df['age']의 모든 원소
print(sr1.head())
print()

sr2 = df['age'].apply(add_two_obj, b=5)      # a = df['age']의 모든 원소, b = 5
print(sr2.head())
print()

sr3 = df['age'].apply(lambda x: add_10(x))   # x = df['age']
print(sr3.head())
print()
