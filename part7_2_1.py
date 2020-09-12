
# example part 7-1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# step 1 데이터 준비
df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

print(df.head())
print()

pd.set_option('display.max_columns', 10)
print(df.head())
print()

# step 2 데이터 탐색
print(df.info())
print()

print(df.describe())
print()
