from mrjob.job import MRJob as mrj

def make_vectors(line):
    '''
    Tabulate household data for a place

    Returns list of relevant data points
    '''
    num_households = line[221]
    avg_size = line[223]

    return [    num_households,
                avg_size
                       ]

class make_vectors(mrj):

    def mapper(self,num, line):
        place = CDPS.get(num,None)

        if place == None:
            return
        line = line.split(",")

        yield "household", make_vectors(line)

    def reducer(self, place, vect):

        yield place, vect
