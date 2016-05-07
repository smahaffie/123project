from mrjob.job import MRJob as mrj


FILE = 'eg: al0000001'
CDPS = []   # list of places we're looking at


def vectorize(line):

    line = line.split(',')

    pct_white = line[10]/line[1] # for example

    return [    population,
                pct_white,
                pct_asian,
                pct_native,
                etc             ]


class make_vectors(mrj):

    def mapper(self,num, line):

        place = CDPS.get(num,None)

        if place == None:
            return


        vector = vectorize(line)
        yield place, vector

    def reducer(self, place, vect):

        yield place, vect

