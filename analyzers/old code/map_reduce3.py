from mrjob.job import MRJob as mrj
import csv
import json
from mrjob.step import MRStep
import math

class calc_distance(mrj):
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(make_vectors,self).configure_options()
        self.add_file_option('--index')
        self.add_file_option('--averages')

    def mapper_init(self):
        with open(self.options.index,'r') as f:
            self.places_dict = json.load(f)
        with open(self.options.averages,'r') as f:
            self.averages = json.load(f)

    def mapper(self,num, line):
        line = line.split(",")
        state = line[1].lower()
        sum_file = line[0]
        index = str(int(line[4])-1) #indexing starts at 0
        sub_file = line[3]
        if index in self.places_dict[state]:
            place = self.places_dict[state][index]
            if sum_file == "uSF1":
                if int(sub_file) == 1 and float(line[5]) != 0:
                        pop_d = pop_data(line)
                        vect = pop_d[1:]
                        for i in range(len(vect)):
                            yield place, (vect[i][0], vect[i][1])

            if sum_file == "uSF3":
                if int(sub_file) == 2 and float(line[146]) != 0:
                    lang_d = lang_data(line)
                    vect = lang_d[1:]
                    for i in range(len(lang_d)):
                        yield place, (vect[i][0], vect[i][1])

                    foreign_d = foreign_data(line)
                    vect = foreign_d[1:]

                    for i in range(len(vect)):
                        yield place,(vect[i][0], vect[i][1])

                if int(sub_file) == 6 and float(line[146]) != 0:
                    yield place, ("hh_income", float(line[82]))

                if int(sub_file) == 5 and float(line[5]) != 0:
                    emp_d = emp_data(line)
                    vect = emp_d[1:]
                    for i in range(len(vect)):
                        yield place,(vect[i][0], vect[i][1])

    def combiner(self,place,vect):
        distance = 0
        for v in vect:
            average = self.averages[v[0]]
            dev = (v[1] - average)/average
            distance += dev
    def reducer_init(self):
        '''
        Initializes 2 heaps with 10 tuples of (0,0)
        '''
        self.h_min = [(0,0) for i in range(10)]
        heapq.heapify(self.h_min)
        self.h_max = [(math.inf,math.inf) for i in range(10)]
        heapq.heapify(self.h_max)

    def reducer(self,place,vect):
        min_distance, min_place = self.h_min[0]
        max_distance, max_place = self.h_max[10]
        distance = 0
        for v in vect:
            average = self.averages[v[0]]
            dev = (v[1] - average)/average
            distance += dev

        if distance < min_distance:
            heapq.heapreplace(self.h, (distance, place))
