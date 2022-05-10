from quakeFuncs import *
f = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
feature = f['features']
new = quake_from_feature(feature)
for quake in new:
   print(quake)
