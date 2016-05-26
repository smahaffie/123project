from mrjob.job import MRJob as mrj
import json
from scipy.spatial import ConvexHull


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


    def get_xy(self,place):


        placeinfo = self.vectors.get(place,None)

        if placeinfo == None:
            return None

        lon,lat = placeinfo[:2]
        # treat lon lat as x,y

        return (float(lon),float(lat))

    def mapper_init(self):
        '''
        load json file with census places for every state
        '''
        self.vectors = json.load(open(self.options.vectors))

    def mapper(self,_,line):

        centre, nodes = line.split('\t')

        centre = centre.replace('"','')
        nodes = nodes.replace('"','')
        points=[]
        for n in nodes.split(','):

            xy = self.get_xy(n)
            if xy == None:
                continue 
            points.append(xy)

        if len(points)==0:
            return
        hull = ConvexHull(points)
        area  = hull.volume
        yield centre, area



if __name__ == "__main__":
    make_graph.run()













