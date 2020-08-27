
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

