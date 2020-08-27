
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

