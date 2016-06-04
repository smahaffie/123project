
from math import radians, cos, sin, asin, sqrt
from mrjob.job import MRJob

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

        name1,lon1,lat1 = place1.split(',')
        name2,lon2,lat2 = place2.split(',')

        distance = haversine(   float(lon1), float(lat1),
                                float(lon2), float(lat2) )



        if distance < 96: #96km is 1 hour of driving so thats sort of neighbory right?

            yield name1, name2
            yield name2, name1

    def combiner(self, place, neighbors):

            yield place, ','.join(neighbors)


    def reducer(self, place , neighbors):

        yield place , ','.join(neighbors)


if __name__ == "__main__":

    MR_neighbors.run()
