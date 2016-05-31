from mrjob.job import MRJob as mrj
import csv
from math import radians, cos, sin, asin, sqrt


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

    name ,lon, lat = line[1:4]
    pairs = []
    #print(index)
    #print(N)
    #index += 1
    for n in range(index+1, N):
        p = vectors[n]
        pname,plon,plat = p[1:4]
        #print(pname,plon,plat)
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
        line = line.split(",")
        if line[0]!='place':
            index = int(line[0])
            place = line[1]
            pairs = generate_pairs(line,index,self.vectors,self.N)
            for p in pairs:
                yield place,p

if __name__ == "__main__":
    gen_vectors.run()
