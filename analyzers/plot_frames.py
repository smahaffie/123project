from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import sys
import json
import matplotlib.cm as cm
import matplotlib
import glob

'''
Generates all plots
'''
States = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
        "GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
        "MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
        "ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
        "VA","WA","WV", "WI", "WY"]

COLORS = [  u'darkolivegreen', u'darkseagreen', u'darkslategrey', u'dimgray',
            u'darkslategray', u'dodgerblue', u'darkgrey', u'darkturquoise',
            u'darkgreen', u'darkviolet', u'darkgray', u'darkslateblue', u'deeppink',
            u'darkmagenta', u'darkgoldenrod', u'dimgrey', u'darkblue', u'darkkhaki',
            u'darkcyan', u'darkorchid', u'deepskyblue', u'darkred', u'darksage',
            u'darkorange', u'darksalmon',u'gold', u'greenyellow', u'goldenrod',
            u'grey', u'green', u'gainsboro', u'mediumspringgreen', u'mediumorchid',
            u'moccasin', u'mediumvioletred', u'maroon', u'magenta',
            u'mediumblue', u'mediumpurple', u'midnightblue', u'mediumseagreen',
            u'mediumturquoise', u'mediumslateblue', u'mediumaquamarine', 'blue',
            'red', 'green', 'magenta', 'purple', 'brown', 'black']

COLORDICT = dict(zip(States,COLORS))


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

COLORDICT = prettify_state()

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



def plot_json2(file1,num_frame):
    mymap = plot_setup()
    framedict = json.load(open(file1,'r'))
    for state, statecolor in COLORDICT.items():
        stateframe = [points for name, points in framedict.items() if name[-2:]==state]
        lons = [lon for lon,lat,_,__ in stateframe]
        lats = [lon for lon,lat,_,__ in stateframe]
        xs,ys = mymap(lons,lats)
        print(len)
        mymap.plot(xs,ys,color=statecolor,label="vectors")
    plt.show()



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
  #  colors = get_nice_colors(50)
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
    #plt.show()
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
    
    size_clusters = []
    counter = 0


    for s in States:
        lons_list,lats_list = [],[]
        for name,lon,lat in vectors:
            if name[-2:]==s:
                lats_list.append(lon)
                lons_list.append(lat)
        x,y = my_map(lons_list,lats_list)
        my_map.plot(x,y,color=COLORDICT[s],marker='.',markersize=20,linestyle='',label=label)


if __name__ == "__main__":
 f = glob.glob('*.json')
 o = ['out'+x.strip('.json') for x in f]
 for a,b in zip(f,o):
    plot_json(a,b)






