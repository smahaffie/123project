from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sys
import json
import matplotlib.cm as cm
import matplotlib

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

def plot_json(file1,num_frame):
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

    plt.savefig(str(num_frame))



def plot_vectors(vectors,my_map,label="vectors"):
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

    for v in vectors:
        places.append(v[0])
        lats_list.append(v[1])
        lons_list.append(v[2])

    x,y = my_map(lons_list,lats_list)
    my_map.plot(x,y,"ro",markersize=20,label=label)


if __name__ == "__main__":
    plot_json(sys.argv[1],sys.argv[2])
