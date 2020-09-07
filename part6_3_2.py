
# example part 6-10

import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns', 10)

sbsp3 = titanic['sibsp'] == 3
sbsp4 = titanic['sibsp'] == 4
sbsp5 = titanic['sibsp'] == 5
titanic_boolean = titanic[sbsp3 | sbsp4 | sbsp5]
print(titanic_boolean.head())
print()

isin_filter = titanic['sibsp'].isin([3,4,5])
titanic_isin = titanic[isin_filter]
print(titanic_isin.head())
print()
