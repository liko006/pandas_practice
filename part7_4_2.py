
# example part 7-8

# DBSCAN 군집분석

import pandas as pd
import folium

# step 1 데이터 준비/기본 설정

file_path = './2016_middle_school_graduates_report.xlsx'
df = pd.read_excel(file_path, header=0, index_col='Unnamed: 0')

pd.set_option('display.width', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

print(df.columns.values)

# step 2 데이터 탐색

print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

# 지도에 위치 표시
mschool_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat,lng], radius=5, color='brown', fill=True, fill_color='coral', fill_opacity=0.7, popup=name).add_to(mschool_map)

mschool_map.save('./seoul_mschool_loc.html')

# step 3 데이터 전처리

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

onehot_loc = label_encoder.fit_transform(df['지역'])
onehot_code = label_encoder.fit_transform(df['코드'])
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_loc
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day

print(df.head())
print()                           

# step 4 DBSCAN 군집 모형 - sklean
from sklearn import cluster

# 분석에 사용할 속정 선택 (과학고, 외고국제고, 자사고 진학률)
columns_list = [9,10,13]
X = df.iloc[:, columns_list]
print(X[:5])
print()

# 설명변수 데이터 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# DBSCAN 모형 
dbm = cluster.DBSCAN(eps=0.2, min_samples=5)

# 모형 학습
dbm.fit(X)

# 예측(군집)
cluster_label = dbm.labels_
print(cluster_label)
print()

# 예측 결과 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())
print()

# 클러스터 값으로 그룹화 / 그룹별 내용 출력
grouped_cols = [0,1,3] + columns_list
grouped = df.groupby('Cluster')
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped_cols].head())
    print()
   
# 그래프 시각화
colors = {-1:'grey', 0:'coral', 1:'blue', 2:'green', 3:'red', 4:'purple', 5:'orange', 6:'brown', 7:'brick', 8:'yellow', 9:'magenta', 10:'cyan'}

cluster_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):
    folium.CircleMarker([lat, lng], radius=5, color=colors[clus], fill=True, fill_color=colors[clus], fill_opacity=0.7, popup=name).add_to(cluster_map)
    
cluster_map.save('./seoul_mschool_cluster.html')

# X2 데이터셋에 위의 과정 + 유형 속성을 추가
columns_list2 = [9,10,13,22]
X2 =df.iloc[:, columns_list2]
print(X2[:5])
print()

X2 = preprocessing.StandardScaler().fit(X2).transform(X2)
dbm2 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm2.fit(X2)
df['Cluster2'] = dbm2.labels_

grouped2_cols = [0,1,3] + columns_list2
grouped2 = df.groupby('Cluster')
for key, group in grouped2:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped2_cols].head())
    print()
    
cluster2_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):
    folium.CircleMarker([lat,lng], radius=5, color=colors[clus], fill=True, fill_color=colors[clus], fill_opacity=0.7, popup=name).add_to(cluster2_map)
    
cluster2_map.save('./seoul_mschool_cluster2.html')

# X3 데이터셋에 대하여 위의 과정중 과학고, 외고_국제고만 속성으로 사용
columns_list3 = [9,10]
X3 = df.iloc[:, columns_list3]
print(X3[:5])
print()

X3 = preprocessing.StandardScaler().fit(X3).transfor(X3)
dbm3 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm3.fit(X3)
df['Cluster3'] = dbm3.labels_

grouped3_cols = [0,1,3] + columns_list3
grouped3 = df.groupby('Cluster')
for key, group in grouped3:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped3_cols].head())
    print()
    
cluster3_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster3):
    folium.CircleMarker([lat,lng], radius=5, color=colors[clus], fill=True, fill_color=colors[clus], fill_opacity=0.7, popup=name).add_to(cluster3_map)
    
cluster3_map.save('./seoul_mschool_cluster3.html')
