import re
import json
import os
import itertools


#ADJACENCY  = "county_adjacency.txt"


"""


"""

def place_lon_lat_genearator(js_vectors):

    """
    take place, lon and lat from js vectors file
    """

    vectordict = json.load(open(js_vectors,'r'))

    for k,v in vectordict.items():
        if( k=='place' and v[1] == 'lon' ):
            continue

        yield k + ',' + v[1] + ',' + v[0]


def make_pairs_file(output,js_vectors):
    """
    makes every pair of place, lon and lat
    to pass to mapreduce
    """

    output = open(output,'w')

    for pair in itertools.combinations(place_lon_lat_genearator(js_vectors),2):

        l = pair[0] + '|' + pair[1]
        output.write(l + '\n')


def go(output):
    """
    turns the json vectors into json of who is neighbors with who
    """

    allpairsfile = "all_pairs.csv"
    jsv = "../json_vectors.json"

    make_pairs_file(allpairsfile,jsv)

    os.system('python find_neighbors_MR.py '+ allpairsfile+' > tmp')

    f = open('tmp','r')

    neighbordict = {}
    for line in f:
        place, neighbors = line.split('\t')
        place = place.replace('"','')
        neighbors = neighbors.replace('"','').strip().split(',')
        neighbordict[place] = neighbors

    g = open(output,'w')
    json.dump(neighbordict,g)


    os.system('rm tmp')
