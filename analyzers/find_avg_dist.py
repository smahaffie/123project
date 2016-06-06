from mrjob.job import MRJob as mrj
import csv
import json
from mrjob.step import MRStep
from math import radians, cos, sin, asin, sqrt

'''
Calculate average demographic distance between two places that are within a certain number of miles
of each other
We use this data point as a parameter in the springs simulation
Inputs: tab delimited file of pairs where each item in a pair is the name of a
place AND json file of vectors with all of the vector data in a list
'''


def difference(v,w):
    '''
    finds difference between two places
    if data is missing we ignore that dimension
    we calculate the root mean squared distance between each dimension
    '''


    n = 0
    tot = 0
    for vi, wi in zip(v,w):
        if vi == 'missing' or wi == 'missing':
            continue
        n += 1
        tot += (float(vi)-float(wi))**2

    return (tot/n)**.5

class mr_pairs_dist(mrj):

    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(mr_pairs_dist,self).configure_options()
        self.add_file_option('--vect_dict')

    def mapper_init(self):
        '''
        load json file with vectors
        '''

        with open(self.options.vect_dict,'r') as f:
            self.vectors = json.load(f)


    def mapper(self,_,line):
        '''
        map pairs to distance between pairs
        '''

        line = line.split("\t")
        a = line[0][1:-1]
        b = line[1][1:-1]
        if a != "place" and b != "place":
            v = self.vectors[a][0].split(',')
            w = self.vectors[b][0].split(',')
            d = difference(v,w)
            global COUNTER
            COUNTER += 1
            yield _, d

    def combiner(self,_,d):
        '''
        sum pair differences
        '''

        yield _, sum(d)

    def reducer(self,_,d):
        '''
        yield average difference between all pairs
        '''

        yield "average difference",sum(d)/COUNTER

if __name__ == '__main__':
    COUNTER = 0
    mr_pairs_dist.run()
