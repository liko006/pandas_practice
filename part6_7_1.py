
# example part 6-20

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]
print(df.head())
print()

pdf1 = pd.pivot_table(df, index='class', columns='sex', values='age', aggfunc='mean')
print(pdf1.head())
print()

pdf2 = pd.pivot_table(df, index='class', columns='sex', values='survived', aggfunc=['mean','sum'])
print(pdf2)
print()

pdf3 = pd.pivot_table(df, index=['class','sex'], columns='survived', values=['age','fare'], aggfunc=['mean','max'])

pd.set_option('display.max_columns', 10)
print(pdf3.head())
print()

print(pdf3.index)
print(pdf3.columns)
print()

print(pdf3.xs('First'))
print()
print(pdf3.xs(('First','female')))
print()
print(pdf3.xs('male', level='sex'))
print()
print(pdf3.xs(('Second','male'), level=[0,'sex']))
print()
print(pdf3.xs('mean',axis=1))
print()
print(pdf3.xs(('mean','age'),axis=1))
print()
print(pdf3.xs(1, level='survived', axis=1))
print()
print(pdf3.xs(('max','fare',0), level=[0,1,2], axis=1))
print()
