
# example part 6

import seaborn as sns

titanic = sns.load_dataset('titanic')

mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())
print()

mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())
print()

mask3 = (titanic.age < 10) | (titanic.age > 60)
df_under10_above60 = titanic.loc[mask3, :]
print(df_under10_above60.head())
print()

mask3 = (titanic.age < 10) | (titanic.age > 60)
df_under10_above60 = titanic.loc[mask3, ['age','sex','alone']]
print(df_under10_above60.head())
print()
