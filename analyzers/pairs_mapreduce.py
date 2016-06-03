from mrjob.job import MRJob as mrj
import csv
from math import radians, cos, sin, asin, sqrt

'''
Use of MapReduce code in order to generate all pairs of places in the US
Usage: python3 pairs_mapreduce.py vectors.txt --vectors=vectors.txt
'''

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

def generate_pairs(line,index,vectors,N):
    '''
    For every place, returns all other places in the US that are within
    a certain distance of that place
    Inputs:
        line, place of interest
        index, keeps track of which line in the file map reduce has just
            "mapped", such that pairs are only generated starting at that points
            in the file, to avoid duplicates
            i.e. the first line generates every possible pair but the last line that is mapped
            has no pairs left to be generated
        vectors, complete vector text file to generate pairs
    '''
    name ,lon, lat = line[1:4]
    pairs = []

    for n in range(index+1, N):
        p = vectors[n]
        pname,plon,plat = p[1:4]
        distance = 100
        try:
            distance = haversine(float(lon),float(lat),float(plon),float(plat))
        except:
            print(p)
        if distance<15:
            pairs.append(pname)

    return pairs



class gen_vectors(mrj):
    '''
    construct vectors of containing relevant variables for every location
    '''
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(gen_vectors,self).configure_options()
        self.add_file_option('--vectors')

    def mapper_init(self):
        '''
        load json file with census places for every state
        '''
        self.vectors = []
        with open(self.options.vectors,'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.vectors.append(row)
        self.N = len(self.vectors)

    def mapper(self,_,line):
        '''
        generates a key,value pair for every combination of places in the US
            keys and values are both place names
        '''
        line = line.split(",")
        if line[0]!='place':
            index = int(line[0])
            place = line[1]
            pairs = generate_pairs(line,index,self.vectors,self.N)
            for p in pairs:
                yield place,p

if __name__ == "__main__":
    gen_vectors.run()
