import re
from math import radians, cos, sin, asin, sqrt
import json

Fails = 0

def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculate the circle distance between two points
    on the earth (specified in decimal degrees)
    totally stolen from PA3 in 122
    '''
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km

def go(rawfile, neighborsfile, allplacesfile):

    f = open(rawfile,'r')

    neighbors = {}

    for line in f:
        a,b, dist = process_line(line)
        if dist < 15:
            aneighbors = neighbors.get(a,[])
            aneighbors.append(b)
            neighbors[a] = aneighbors

    json.dump(neighbors,open(neighborsfile,'w'))

    g = open(allplacesfile,'w')
    for name in neighbors.keys():
        g.write(name+'\n')
    print(Fails)




def process_line(line):

    try:
        a,b = re.sub('[\[\]\"\n]','',line).split('\t')
        a_name,a_lon,a_lat = a.split(',')
        b_name,b_lon,b_lat = b.split(',')

        a_lon = float(a_lon)
        a_lat = float(a_lat)
        b_lon = float(b_lon)
        b_lat = float(b_lat)

        distance = haversine(a_lon,a_lat,b_lon,b_lat)

        return a_name, b_name, distance
    except:
        global Fails
        Fails +=1
   #     print line
        return 0, 0 , float('inf')
