
# example part 4-1

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./시도별 전출입 인구수.xlsx', fillna=0, header=0)

df = df.fillna(method='ffill')

temp = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')

df_seoul = df[temp]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

sr_one = df_seoul.loc['경기도']

plt.plot(sr_one.index, sr_one.values)    # same result with plt.plot(sr_one)
