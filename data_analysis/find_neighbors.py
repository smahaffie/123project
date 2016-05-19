import re
import networkx as nx
from math import radians, cos, sin, asin, sqrt
import heapq
import itertools
from mrjob.job import MRJob

ADJACENCY  = "county_adjacency.txt"



def make_pairs_file(filename):

    f = open(filename,'r')
    lines = f.readlines()

    output = open("all_pairs.csv",'w')

    for pair in itertools.combinations(lines,2):
        l = str(pair[0]).strip() + '|' + str(pair[1]).strip()
        output.write(l+'\n')

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


class MR_neighbors(MRJob):

    def mapper(self,_,line):
        
        place1, place2 = line.split('|')

        code1,name1,lon1,lat1 = place1.split(',')
        code2,name2,lon2,lat2 = place2.split(',')

        distance = haversine(lon1,lat1,lon2,lat2)

        if distance < 96: #96km is 1 hour of driving so thats sort of neighbory right?
            key = ','.join(code1,name1,code2,name2)

            yield key, distance


    def combiner(self, key, distance):
        yield key, distance

    def reducer(self, key, distance):
        code1, name1, code2, name2 = key.split()

        yield ','.join(code1,name1,code2,name2) , distance
        yield ','.join(code2,name2,code1,name1) , distance



if __name__ == "__main__":

    MR_neighbors.run()


