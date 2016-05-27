from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def plot_homogenous(vectors):
    colors = "bgrcmykw"
    places = []
    places_lats = []
    places_lons = []
    lats_list = []
    lons_list = []
    with open(vectors) as f:
        for line in f:
            lons = []
            lats = []
            line = line.split("\t")
            places.append(line[0][0])
            places_lats.append(line[0][1])
            places_lons.append(line[0][1])
            lats.append(line[0][1])
            lons.append(line[0][2])
            for tup in line[1]:
                #places.append(tup[0])
                lats.append(tup[1])
                lons.append(tup[2])
            lats_list.append(lats)
            lons_list.append(lons)

    fig = plt.figure(figsize=(10,10))
    my_map = Basemap(projection='ortho', lat_0 = 39, lon_0 = -98,
                  resolution = 'l', area_thresh = 1000.)
    my_map.drawcoastlines()
    my_map.drawcountries()
    #my_map.fillcontinents(color='coral')
    my_map.drawmapboundary()
    for i in range(len(places)):
        lons = lons_list[i]
        lats = lats_list[i]
        x,y = my_map(lons,lats)
        my_map.plot(x,y,colors[i])
    x,y = my_map(places_lons,places_lats)
    for name,xpt,ypt in zip(places,x,y):
        plt.text(xpt+50000,ypt+50000,name)

    plt.show()
if __name__ == "__main__":
    plot_homogenous(sys.argv[1])
