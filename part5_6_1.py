
# example part 5-15

import pandas as pd

df = pd.read_csv('./stock-data.csv')

print(df.head())
print()
print(df.info())
print()

df['new_Date'] = pd.to_datetime(df['Date'])

print(df.head())
print()
print(df.info())
print()
print(type(df['new_Date'][0]))
print()

df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)

print(df.head())
print()
print(df.info())
print()

# example part 5-16

import pandas as pd

dates = ['2019-01-01', '2020-03-01', '2021-06-01']

ts_date = pd.to_datetime(dates)
print(ts_date)
print()

pr_day = ts_date.to_period(freq='D')
print(pr_day)
pr_month = ts_date.to_period(freq='M')
print(pr_month)
pr_year = ts_date.to_period(freq='A')
print(pr_year)
