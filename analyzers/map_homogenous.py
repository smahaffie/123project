from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sys
import json
import matplotlib.cm as cm

'''
Generates a plot of the top k homogenous areas in the US
Usage: python3 map_homogenous.py
<file containing all homogenous areas> <file containing names of topk homogenous areas>
<file containing longitudes and latitudes of all places in the US>
'''

def plot_setup():
    '''
    Basic set up for plots
    '''

    fig = plt.figure(figsize=(30,30))
    h = 1500
    my_map = Basemap(llcrnrlon=-130.0,
        llcrnrlat=20.0,
        urcrnrlon=-60.0,
        urcrnrlat=55.0,
        projection='merc',
        resolution='c')

    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='antiquewhite',lake_color='aqua')
    my_map.drawmapboundary()
    my_map.drawstates()
    my_map.drawmapboundary(fill_color='aqua')
    return my_map

def plot_homogenous(vectors,topk,lonlat):
    '''
    Plots the top k largest homogenous areas in the US on a map
    Inputs:
        vectors, file with vectors grouped into homogenous areas
        topk, file containing top k groupings by surface area
        lonlat, json file containing longitude and latitude of every place
    Side effects:
        Generates map
    '''

    with open(lonlat) as f:
        lonlat_dict = json.load(f)

    my_map = plot_setup()
    top_places = []
    with open(topk) as f:
        for line in f:
            l = line.split("\t")
            top_places.append(l[0].strip('"'))

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
            if name_list[0][1:] in top_places:
                name = name_list[0].split("_")
                place_lats.append(float(name_list[1]))
                place_lons.append(float(name_list[2]))
                places.append(name[0]+", " + name[1])
                tups = l[1].split(";")
                size_clusters.append(len(tups))
                for tup in tups:
                    t = tup.split(",")
                    if len(t) == 3:
                        lat = float(lonlat_dict[name_list[0][1:]][0])
                        lon = float(lonlat_dict[name_list[0][1:]][1])
                        x,y = my_map(lon,lat)
                        my_map.plot(x,y,"ro",markersize=10)

    plt.title("Largest Homogenous Areas in the US")
    plt.savefig("Homogenous Areas")

if __name__ == "__main__":
    plot_homogenous(sys.argv[1],sys.argv[2],sys.argv[3])
