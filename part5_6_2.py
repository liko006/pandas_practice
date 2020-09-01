
# example part 5-17

import pandas as pd

ts_ms = pd.date_range(start='2019-01-01', end=None, periods=6, freq='MS', tz='Asia/Seoul')

print(ts_ms)
print()

ts_me = pd.date_range(start='2019-01-01', periods=6, freq='M', tz='Asia/Seoul')
print(ts_me)
print()

ts_3m = pd.date_range(start='2019-01-01', periods=6, freq='3M', tz='Asia/Seoul')
print(ts_3m)
print()
