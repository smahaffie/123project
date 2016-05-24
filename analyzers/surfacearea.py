from mrjob.job import MRJob as mrj
import json
from scipy.spatial import ConvexHull




"""
input, 
"""

class make_graph(mrj):
    '''
    construct vectors of containing relevant variables for every location
    '''

    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(make_graph,self).configure_options()
        self.add_file_option('--vectors')
        self.add_file_option('--neighbors')


    def get_xy(self,place):

        lon,lat = self.vectors[:1]

        # need lon lat to x,y

    def mapper_init(self):
        '''
        load json file with census places for every state
        '''
        self.vectors = json.load(open(self.options.vectors))
        self.neighbors = json.load(open(self.options.neighbors))

    def mapper(self,_,line):

        centre, nodes = line.split('\t')
        points = [get_xy(n) for n in nodes.split(',')]
        hull = ConvexHull(points)
        area  = hull.volume



if __name__ == "__main__":
    make_graph.run()













