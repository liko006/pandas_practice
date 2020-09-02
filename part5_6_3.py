
# example part 5-19

import pandas as pd

df = pd.read_csv('./stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
print(df.head())
print()

df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())
print()

df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())
print()

df.set_index('Date_m', inplace=True)
print(df.head())
print()

# example part 5-20

import pandas as pd

df = pd.read_csv('./stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df.set_index('new_Date', inplace=True)

print(df.head())
print()
print(df.index)
print()

df_y = df['2018']
print(df_y.head())
print()
df_ym = df['2018-07']
print(df_ym)
print()
df_ym_cols = df.loc['2018-07', 'Start':'High']
print(df_ym_cols)
print()
df_ymd = df['2018-07-02']
print(df_ymd)
print()
df_ymd_range = df['2018-06-25':'2018-06-20']
print(df_ymd_range)
print()

today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta', inplace=True)
df_180 = df['180 days':'189 days']
print(df_180)
