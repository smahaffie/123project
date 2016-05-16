# USAGE: python3 find_most_representative.py sample_data.csv n most_or_least
# most_or_least should be "most" or "least"

import csv
import math
from mrjob.job import MRJob
import heapq
import sys

AVGS = ''
VARIABLES = ''
STDS = ''

def setup_globals(avgs_file="sample_averages.csv",stds_file="sample_stds.csv",data_file="sample_data.csv"):
    with open(avgs_file,"r") as f:
        global VARIABLES
        VARIABLES = f.readline().strip().split(",")
        global AVGS 
        AVGS = f.readline().strip().split(",")
        assert len(AVGS) == len(VARIABLES)
    with open(stds_file,"r") as f:
        check = f.readline().strip().split(",")
        assert check == VARIABLES
        global STDS
        STDS = f.readline().strip().split(",")
        assert len(STDS) == len(VARIABLES)

class MRMostRepresentative(MRJob):

    def mapper(self, _, line):
        if line[0] != 'p':

            num_vars = len(VARIABLES)

            place = line.split(",")[0]
            vect = line.split(",")[1:]
            assert len(vect) == num_vars

            total_squared_std_dists = 0
            for i in range(num_vars):
                if float(STDS[i]) != 0 and vect[i] != 'missing':
                    total_squared_std_dists += ((float(vect[i])-float(AVGS[i]))/float(STDS[i])) ** 2

            assert most_or_least == "most" or most_or_least == "least"
            if most_or_least == "most":
                yield place, -1 * math.sqrt(total_squared_std_dists)
            else:
                yield place, math.sqrt(total_squared_std_dists)

    def reducer_init(self):
        self.h = []
        for i in range(n):
            self.h.append((-99999999999,-9999999999))
        heapq.heapify(self.h)

    def reducer(self, place, dist):
        min_count, min_n = self.h[0]

        dist = sum(dist)

        if dist > min_count:
            heapq.heapreplace(self.h, (dist, place))

    def reducer_final(self):
        '''
        sorts and yields the heap self.h
        '''
        self.h.sort(reverse=True)
        for (dist,place) in self.h:
            yield place, abs(dist)
        

if __name__ == '__main__':
    n = int(sys.argv[2])
    most_or_least = sys.argv[3]
    setup_globals()
    MRMostRepresentative.run()
