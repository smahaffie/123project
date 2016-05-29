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

    fig = plt.figure(figsize=(30,30))
    h = 1500
    my_map = Basemap(llcrnrlon=-130.0,
        llcrnrlat=20.0,
        urcrnrlon=-60.0,
        urcrnrlat=55.0,
        projection='mill',
        resolution='c')

    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='antiquewhite',lake_color='aqua')
    my_map.drawmapboundary()
    my_map.drawstates()
    my_map.drawmapboundary(fill_color='aqua')
    return my_map

def plot_unique_avg(unique,average):
    '''
    Set up for plotting most unique and most average places in the US
    Inputs:
        unique, filename
        average, filename
    Side effects:
        Saves image file
    '''
    my_map = plot_setup()
    unique = plot_vectors(unique,my_map,"bo","Most Unique")
    average = plot_vectors(average,my_map,"ro","Most Average")
    plt.legend()
    plt.title("Most Average and Unique Areas in the US")
    plt.savefig("Most Average and Unique")


def plot_vectors(vectors,my_map,color,label):
    '''
    Plots set of vectors places in the US

    Inputs:
        vectors, filename
        my_map, map object
        color, string
        label, string
    '''
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
            name = name_list[0]
            #if "city" in name:
            name = name.replace("city","")
            name = name.replace("CDP","")
            name = name.split("_")
            places.append(name[0] + "," + name[1])
            #+", " + name[1])
            lats_list.append(float(name_list[1].strip('"')))
            lons_list.append(float(name_list[2].strip('"')))
    x,y = my_map(lons_list,lats_list)
    my_map.plot(x,y,color,markersize=20,label=label)

    '''
    for label,x,y in zip(places,lons_list,lats_list):
        xi,yi=my_map(x,y)
        plt.text(xi+10000,yi+10000,label[1:])'''






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
    plot_unique_avg(sys.argv[1],sys.argv[2])
