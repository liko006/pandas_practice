
# example part 1-25
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print()
print(type(df))
print()

addition = df + 10
print(addition.head())
print()
print(type())
print()

# example part 1-26
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.tail())
print()
print(type(df))
print()

addition = df + 10
print(addition.tail())
print()
print(type(addition))
print()

subtraction = addition - df
print(subtraction.tail())
print()
print(type(subtraction))
print()
