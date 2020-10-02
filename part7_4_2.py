
# example part 7-8

# DBSCAN 군집분석

import pandas as pd
import folium

# step 1 데이터 준비/기본 설정

file_path = './2016_middle_school_graduates_report.xlsx'
df = pd.read_excel(file_path, header=0)

pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

print(df.columns.values)
