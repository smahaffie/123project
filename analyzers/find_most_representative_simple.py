# USAGE: python3 find_most_representative_simple.py --jobconf mapreduce.job.reduces=1 sample_data.csv n most_or_least
# most_or_least should be "most" or "least"

import csv
import math
from mrjob.job import MRJob
import heapq
import sys

AVGS = ''
VARIABLES = ''
STDS = ''
VAR_INDECES = ''

def setup_globals(variables_of_interest,avgs_file="../intermediate_data/alabama_avgs.csv",stds_file="../intermediate_data/alabama_stds.csv",data_file="../intermediate_data/alabama_data.csv"):
    with open(avgs_file,"r") as f:
        global VARIABLES
        all_variables = f.readline().strip().split(",")
        if variables_of_interest == 'all':
            VARIABLES = all_variables
            var_indeces = []
            for i in range(len(VARIABLES)):
                var_indeces.append(i)
        else:
            variables_of_interest = variables_of_interest.split(",")
            var_indeces = []
            for var in variables_of_interest:
                var_indeces.append(all_variables.index(var))
            print(var_indeces)

        global AVGS 
        avgs_from_file = f.readline().strip().split(",")
        if variables_of_interest == 'all':
            AVGS = avgs_from_file
        else:
            AVGS = []
            for var_index in var_indeces:
                AVGS.append(avgs_from_file[var_index])

    with open(stds_file,"r") as f:
        global STDS
        f.readline()
        stds_from_file = f.readline().strip().split(",")
        if variables_of_interest == 'all':
            STDS = stds_from_file
        else:
            STDS = []
            for var_index in var_indeces:
                STDS.append(stds_from_file[var_index])

    global VAR_INDECES 
    VAR_INDECES = var_indeces

    print("VARIABLES: ", VARIABLES, len(VARIABLES))
    print("AVGS: ", AVGS, len(AVGS))

class MRMostRepresentative(MRJob):

    def mapper(self, _, line):
        if line[0] != 'p':

            num_vars = len(VARIABLES)

            place = ",".join(line.split(",")[0:3])

            whole_vect = line.split(",")[3:]
            vect = []
            for index in VAR_INDECES:
                vect.append(whole_vect[index])
            assert len(vect) == num_vars

            total_squared_std_dists = 0
            for i in range(len(vect)):
                try:
                    if float(STDS[i]) != 0 and vect[i] != 'missing':
                        total_squared_std_dists += ((float(vect[i])-float(AVGS[i]))/float(STDS[i])) ** 2
                except:
                    print("PANIC")
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
        print(self.h)

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
    n = int(sys.argv[4])
    print(n)
    most_or_least = sys.argv[5]
    variables_of_interest = sys.argv[6]
    if variables_of_interest != 'all':
        VARIABLES = variables_of_interest.split(",")
        print(VARIABLES)
    setup_globals(variables_of_interest)
    print("set up globals")
    MRMostRepresentative.run()