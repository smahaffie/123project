from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sys
import json
import matplotlib.cm as cm

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
        projection='merc',
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

def get_nice_colors(n_colors):
    '''
    Not Original code:
    Generages list of n "nice" colors
    '''
    return cm.Accent( [1 - (i/n_colors) for i in range(n_colors)] )

def undo_mercator_project(x,y):
    """
    x,y to lon, lat
    """
    lon = y*np.pi
    ex = np.exp(4*np.pi*x)
    lat = np.arcsin((ex - 1)/(ex +1 ))
    lon = lon*360/2/np.pi
    lat = lat*360 /2/np.pi
    return lon, lat

def plot_json(file1):
    '''
    Plots latitude and longitudes stored in a json direction
    where the key is the place and the value is a list of latitudes and longitudes
    Inputs:
        file1, string
    Side effects:
        Save png image in current directory
    '''
    my_map = plot_setup()
    dictionary = json.load(open(file1,'r'))
    colors = get_nice_colors(50)
    color_dict = {}
    counter = 0
    colors = "bgrcmykwbgrcmykw"

    for key in dictionary:
        y = dictionary[key][0]
        x = dictionary[key][1]
        state = key[-2:]

        lon,lat = undo_mercator_project(x,y)

        if state in color_dict:
            color = color_dict[state]
        else:
            color_dict[state] = colors[counter]
            color = colors[counter]
            if counter < 15:
                counter += 1
            else:
                counter = 0
        my_map.plot(lat,lon,color+"o",markersize=10,latlon=True)

    plt.savefig("{}_plot.png".format(file1[:-4]))



def plot_vectors(vectors,my_map,color,label):
    '''
    Plots set of vectors places in the US

    Inputs:
        vectors, filename
        my_map, map object
        color, string
        label, string
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
            name = name_list[0]
            name = name.replace("city","")
            name = name.replace("CDP","")
            name = name.split("_")
            places.append(name[0] + "," + name[1])
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
    #print(sys.argv[1])
    plot_json(sys.argv[1])
    #plot_unique_avg(sys.argv[1],sys.argv[2])
