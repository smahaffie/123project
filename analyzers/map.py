from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))
my_map = Basemap(projection='ortho', lat_0 = 50, lon_0 = -100,
              resolution = 'l', area_thresh = 1000.)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
lats = [40.02, 32.73, 38.55, 48.25, 17.29]
lons = [-105.16, -117.16, -77.00, -114.21, -88.10]
cities=['Boulder, CO','San Diego, CA',
    'Washington, DC','Whitefish, MT','Belize City, Belize']
x,y = my_map(lons,lats)
my_map.plot(x,y,'bo')
for name,xpt,ypt in zip(cities,x,y):
    plt.text(xpt+50000,ypt+50000,name)

plt.show()
