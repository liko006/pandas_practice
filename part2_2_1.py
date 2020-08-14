
# eaxmple part 2-4

import pandas as pd

url = './sample.html'

tables = pd.read_html(url)

print(len(tables))
print()

for i in range(len(tables)):
    print('tables[%s]' % i)
    print(tables[i])
    print()
    
df = tables[1]

df.sex_index(['name'], inplace=True)
print(df)
print()
