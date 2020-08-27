
# install folium library
# In Anaconda prompt window, type 'conda install -c conda-forge folium'

# example part 4-36

import folium

seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)

seoul_map.save('./seoul.html')

# example part 4-37

import folium 

seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)
seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner', zoom_start=12)

seoul_map2.save('./seoul2.html')
seoul_map3.save('./seoul3.html')

# example part 4-38

import pandas as pd
import folium

df = pd.read_excel('./서울지역 대학교 위치.xlsx', index-col=0)

seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat,lng], popup=name).add_to(seoul_map)

seoul_map.save('./seoul_colleges.html')

# example part 4-39

import pandas as pd
import folium

df = pd.read_excel('./서울지역 대학교 위치.xlsx', index-col=0)

seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.CircleMarker([lat,lng], radius=10, color='brown', fill=True, fill_color='coral', fill_opacity=0.7, popup=name).add_to(seoul_map)
    
seoul_map.save('./seoul_colleges2.html')

# example part 4-40

import pandas as pd
import folium
import json

file_path = './경기도인구데이터.xlsx'
df = pd.read_excel(file_path, index_col='구분')
df.columns = df.columns.map(str)

geo_path = './경기도행정구역경계.json'
try:
    geo_data = json.load(open(geo_path, encoding='utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))
    
g_map = folium.Map(location=[37.5502,126.982], tiles='Stamen Terrain', zoom_start=9)

year='2007'

folium.Choropleth(geo_data=geo_data, data=df[year], columns=[df.index,df[year]], fill_color='YlOrRd', fill_opacity=0.7,
                  line_opacity=0.3, threshold_scale=[10000,100000,300000,500000,700000], key_on='feature.properties.name').add_to(g_map)

g_map.save('./gyonggi_population_' + year + '.html')
