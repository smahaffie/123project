from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sys
import json
import matplotlib.cm as cm

'''
Generates all plots
'''
def prettify_state():
    """
    returns a dict {states:color code}
    """
    States = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
        "GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
        "MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
        "ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
        "VA","WA","WV", "WI", "WY"]
    colors = matplotlib.colors.cnames
    chosen = np.random.choice(colors.keys(),len(States),False)

    return dict(zip(States,chosen))

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
    lons_list = []
    lats_list = []
    c = 0

    rows = []

    for key in dictionary:
        lat = dictionary[key][0]
        lon = dictionary[key][1]
        row = [key, lat, lon]
        rows.append(row)
    plot_vectors(rows,my_map)

    '''lons_list.append(lon)
        lats_list.append(lat)
        state = key[-2:]
        #x,y = my_map(lon,lat)


        #lon,lat = undo_mercator_project(x,y)
        #print(key,lon,lat)

        if state in color_dict:
            color = color_dict[state]
        else:
            color_dict[state] = colors[counter]
            color = colors[counter]
            if counter < 15:
                counter += 1
            else:
                counter = 0
        x,y =my_map(lon,lat)
        my_map.plot(x,y)
        #print(lon,lat)
        #my_map.plot(lon,lat,"ro",markersize=10,latlon=True)
    #x,y = my_map(lons_list,lats_list)
    #my_map.plot(x[:200],y[:200],color,markersize=20)
    #print(len(x),len(y))
    #for i in range(200):
    #    my_map.plot(y[i],x[i],color,markersize=20)'''
    plt.savefig("please.png")



def plot_vectors(vectors,my_map,color="ro",label="vectors"):
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
    '''
    with open(vectors) as f:
        for line in f:
            line = line.split("\t")
            place = line[0]
            name_list = place.split(",")
            if len(name_list) > 2:
                name = name_list[0]
                name = name.replace("city","")
                name = name.replace("CDP","")
                name = name.split("_")
                #print(name_list)'''
    for v in vectors:
        print(v)
        places.append(v[0])
        lats_list.append(v[1])
        lons_list.append(v[2])
                #places.append(name[0] + "," + name[1])
                #lats_list.append(float(name_list[1].strip('"')))
                #lons_list.append(float(name_list[2].strip('"')))

    x,y = my_map(lons_list,lats_list)
    my_map.plot(x,y,color,markersize=20,label=label)

    '''
    for label,x,y in zip(places,lons_list,lats_list):
        xi,yi=my_map(x,y)
        plt.text(xi+10000,yi+10000,label[1:])'''

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

    colors = "bgrcmykwbgrcmykwbgrcmykwbgrcmykwbgrcmykwbgrcmykwbgrcmykwbgrcmykw"
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

    counter = 0
    '''
    for i in range(len(places)):
        lons = lons_list[counter:counter+size_clusters[i]]
        lats = lats_list[counter:counter+size_clusters[i]]
        counter += size_clusters[i]
        xi,yi = my_map(lons,lats)
        my_map.plot(xi,yi,colors[i])'''
    plt.title("Largest Homogenous Areas in the US")
    plt.savefig("Homogenous Areas")

if __name__ == "__main__":
    plot_homogenous(sys.argv[1],sys.argv[2],sys.argv[3])
