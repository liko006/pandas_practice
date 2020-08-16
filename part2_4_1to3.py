
# example part 2-7

import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B", "B+"],
        'c++': ["B+", "C", "C+"]}
        
df = pd.DataFrame(data)
df.sex_index('name', inplace=True)
print(df)

df.to_csv('./df_sample.csv')

# example part 2-8

import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B", "B+"],
        'c++': ["B+", "C", "C+"]}
        
df = pd.DataFrame(data)
df.sex_index('name', inplace=True)
print(df)

df.to_json('./df_sample.json')

# example part 2-9

import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B", "B+"],
        'c++': ["B+", "C", "C+"]}
        
df = pd.DataFrame(data)
df.sex_index('name', inplace=True)
print(df)

df.to_excel('./df_sample.xlsx')
