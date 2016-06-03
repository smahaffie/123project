from mrjob.job import MRJob as mrj
import json
from scipy.spatial import ConvexHull
import heapq


class make_graph(mrj):
    '''
    construct vectors of containing relevant variables for every location
    '''

    def configure_options(self):
        '''
        pass additional arg to map reduce job
        '''
        super(make_graph,self).configure_options()
        self.add_file_option('--n')

    def mapper(self,_,line):
        """
        takes in a line, seperate centre of homeogenous area
        from all the nodes, then makes hull of points to proxy for area
        """
        line = line.strip('\tnull\n').replace('"','')
        centre, nodes = line.split('|')

        cname, clon, clat = centre.split(',')

        points = []
        for n in nodes.split(';'):
            if n == '':
                continue
            nname, nlon, nlat = n.split(',')
            points.append((nlon,nlat))
        if len(points) > 2:
            try:
                hull = ConvexHull(points)
                area  = hull.volume
                yield cname, area

            except:
                # dykstra failed for some reason, most likely because
                # all points were in a line (unlikely, as we are dealing with floats)
                global NUM_INCORRECT
                NUM_INCORRECT += 1
                pass

        #hull = ConvexHull(points)
        #area  = hull.volume
        #yield cname, area

    def reducer_init(self):
        """
        find top n with a heap
        """
        self.n = int(self.options.n)
        self.h = []
        for i in range(self.n):
            self.h.append((-99999999999,-9999999999))
        heapq.heapify(self.h)

    def reducer(self, place, area):
        """
        find top n with a heap
        """
        min_count, min_n = self.h[0]

        l = list(area)
        assert len(l)==1
        area = l[0]

        if area > min_count:
            heapq.heapreplace(self.h, (area, place))

    def reducer_final(self):
        '''
        sorts and yields the heap self.h
        '''
        self.h.sort(reverse=True)
        for (area,place) in self.h:
            yield place, abs(area)


if __name__ == "__main__":
    NUM_INCORRECT = 0
    make_graph.run()
