from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sys

'''
Generates all plots
'''

def plot_setup():
    '''
    Basic set up for plots
    '''

    fig = plt.figure(figsize=(10,10))
    h = 1500
    my_map = Basemap(projection='nsper',lon_0=-105,lat_0=40,
        satellite_height=h*1000.,resolution='l')

    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='coral',lake_color='aqua')
    my_map.drawmapboundary()
    my_map.drawstates()
    my_map.drawmapboundary(fill_color='aqua')
    return my_map

def plot_unique(vectors):
    '''
    Plots most unique places in the US
    '''

    colors = "bgrcmykwbgrcmykw"
    places = []
    lats_list = []
    lons_list = []
    size_clusters = []
    counter = 0
    with open(vectors) as f:
        for line in f:
            line = line.split("\t")
            place = line[0]
            name_list = place.split(",")
            name = name_list[0].split("_")
            places.append(name[0]+", " + name[1])
            lats_list.append(float(name_list[1].strip('"')))
            lons_list.append(float(name_list[2].strip('"')))
    fig = plt.figure(figsize=(10,10))
    h = 1500
    my_map = Basemap(projection='nsper',lon_0=-105,lat_0=40,
        satellite_height=h*1000.,resolution='l')

    my_map.drawcoastlines()
    my_map.drawcountries()
    #my_map.fillcontinents(color='coral',lake_color='aqua')
    my_map.drawmapboundary()
    my_map.drawstates()
    #my_map.drawmapboundary(fill_color='aqua')
    print(lats_list,lons_list)
    x,y = my_map(lons_list,lats_list)
    print(x,y)
    my_map.plot(x,y,'g')
    for label,x,y in zip(places,lons_list,lats_list):
        xi,yi=my_map(x,y)
        plt.text(xi+10000,yi+5000,label[1:])
    plt.title("Most Unique Areas in the US")
    plt.show()
    plt.savefig("Most Unique")





def plot_homogenous(vectors):
    '''
    Plots the 10 largest homogenous areas in the US on a map
    Inputs:
        vectors, file
    Side effects:
        Generates map
    '''
    colors = "bgrcmykwbgrcmykw"
    places = []
    place_lats = []
    place_lons = []
    lats_list = []
    lons_list = []
    size_clusters = []
    counter = 0
    with open(vectors) as f:
        for line in f:
            l = line.split("|")
            place = l[0]
            name_list = place.split(",")
            if name_list[0] in top_k:
                name = name_list[0].split("_")
                place_lats.append(name_list[1])
                place_lons.append(name_list[2])
                places.append(name[0]+", " + name[1])
                tups = l[1].split(";")
                size_clusters.append(len(tups))
                for tup in tups:
                    t = tup.split(",")
                    if len(t) == 3:
                        lats_list.append(float(t[1]))
                        lons_list.append(float(t[2]))

    plot_setup()
    counter = 0
    for i in range(len(places)):
        lons = lons_list[counter:counter+size_clusters[i]]
        lats = lats_list[counter:counter+size_clusters[i]]
        counter += size_clusters[i]
        xi,yi = my_map(lons,lats)
        my_map.plot(xi,yi,colors[i])
    for label,x,y in zip(places,places_lats,places_lons):
        xi,yi=my_map(x,y)
        plt.text(xi+10000,yi+5000,label)
    plt.title("Largest Homogenous Areas in the US")
    plt.savefig("Homogenous Areas")

if __name__ == "__main__":
    #plot_homogenous(sys.argv[1])
    plot_unique(sys.argv[1])
