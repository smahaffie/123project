from mrjob.job import MRJob 

class find_average(MRJob):

    def mapper(self,line):
        place, pop, vect = line

        for i in range(len(vect)):
            yield i, (pop,vect[i])

    def combiner(self, field, V):
        tot_pop = 0
        agg_v = 0
        for pop, v_ele in list(V):
            tot_pop += pop
            agg_v += v_ele*pop

        avg_ele = agg_v/tot_pop

        yield field , (tot_pop, avg_ele)

    def reducer(self, field, V):
        tot_pop = 0
        agg_v = 0
        for pop, v_ele in list(V):
            tot_pop += pop
            agg_v += v_ele*pop

        avg_ele = agg_v/tot_pop

        yield field, avg_ele