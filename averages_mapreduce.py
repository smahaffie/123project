from mrjob.job import MRJob as mrj
import csv
import json
from mrjob.step import MRStep

def pop_data(line):
    '''
    Tabulate population data for a place
    Returns list of relevant data points
    '''
    population = float(line[5])
    pct_urban = float(line[7])/float(line[5])
    pct_white = float(line[14])/float(line[5])
    pct_indian = float(line[16])/float(line[5])
    pct_black = float(line[15])/float(line[5])
    pct_asian = float(line[17])/float(line[5])
    pct_hispanic = float(line[84])/float(line[5])

    return [    ("total_pop",population),
                ("pct_white", pct_white),
                ("pct_black",pct_black),
                ("pct_asian",pct_asian),
                ("pct_hispanic",pct_hispanic),
                ("pct_urban",pct_urban)
                       ]
def lang_data(line):
    '''
    Tabulate language data for a place

    Inputs:
        line, list
    Returns:
        list of relevant data points
    '''
    households = float(line[157])
    pct_english = float(line[158])/households
    pct_spanish = float(line[159])/households
    pct_euro = float(line[162])/households
    pct_asian = float(line[165])/households
    pct_other = float(line[168])/households

    return [    ("households",households),
                ("pct_english",pct_english),
                ("pct_spanish",pct_spanish),
                ("pct_euro",pct_euro),
                ("pct_asian_lang",pct_asian),
                ("pct_other",pct_other)
                       ]

def foreign_data(line):
    population = float(line[171])
    native = float(line[172])/population
    foreign = float(line[183])/population
    return [("population",population),
            ("native",native),
            ("foreign",foreign)]

def education_data(line):
    '''
    educational attainment data for a place, summing over males and females
    '''

    population = float(line[-35])
    less_than_hs = 0

    for i in range(213,220):
        less_than_hs += float(line[i])
    for i in range(230,237):
        less_than_hs += float(line[i])

    less_than_hs = less_than_hs/population

    hs = float(line[220]) + float(line[237])/population
    less_bachelors = (float(line[221]) + float(line[222]) + float(line[223])
    + float(line[238]) + float(line[239]) + float(line[240]))/population
    bachelors = (float(line[224]) + float(line[241]))/population
    doctorate = (float(line[228]) + float(line[245]))/population

    return [("population",population),
            ("less_than_hs",less_than_hs),
            ("less_bachelors",less_bachelors),
            ("bachelors",bachelors),
            ("doctorate",doctorate)]

def emp_data(line):
    '''
    Employment data, summing over male and female
    '''
    pop = float(line[5])
    pct_full_time = (float(line[8]) + float(line[30]))/pop
    pct_part_time = (float(line[15]) + float(line[22]) + float(line[37]) + float(line[44]))/pop
    pct_no_work = (float(line[29]) + float(line[51]))/pop
    #assert (pct_full_time + pct_part_time + pct_no_work < 1)

    return [("population",pop),
        ("pct_full_time",pct_full_time),
        ("pct_part_time",pct_part_time),
        ("pct_no_work",pct_no_work)
        ]

class make_vectors(mrj):
    '''
    construct vectors of national averages for different measures
    '''
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(make_vectors,self).configure_options()
        self.add_file_option('--index')

    def mapper_init(self):
        '''
        Load json dict that contains file line indexes for places by state
        '''
        with open(self.options.index,'r') as f:
            self.index_dict = json.load(f)

    def mapper(self,num, line):
        '''
        Creates a key, value pair for every variable of interest for every place
        in every state
        Key is a string equal to variable of interest (e.g. "pct_english")
        Value is a tuple (relevant total, value)
            e.g. (population of place,pct_englist)
        '''
        line = line.split(",")
        state = line[1]
        sum_file = line[0]
        index = str(int(line[4])-1) #indexing starts at 0
        sub_file = int(line[3])
        if index in self.index_dict[sum_file][state.upper()]["indexes"]:
            place = self.index_dict[sum_file][state.upper()]["tuples"][index]
            if sum_file == "uSF1":
                if sub_file == 1 and (float(line[5]) != 0):
                        pop_d = pop_data(line)
                        pop = pop_d[0][1]
                        vect = pop_d[1:]
                        for i in range(len(vect)):
                            yield vect[i][0], (pop,vect[i][1])

            if sum_file == "uSF3":
                if sub_file == 2 and (float(line[171]) != 0):
                    lang_d = lang_data(line)
                    households = lang_d[0][1]
                    vect = lang_d[1:]

                    for i in range(len(vect)):
                        yield vect[i][0], (households,vect[i][1])

                    foreign_d = foreign_data(line)
                    population = foreign_d[0][1]
                    vect = foreign_d[1:]

                    for i in range(len(vect)):
                        yield vect[i][0], (population,vect[i][1])

                if sub_file == 3 and float(line[161]) != 0:
                    ed_d = education_data(line)
                    pop = ed_d[0][1]
                    vect2 = ed_d[1:]
                    for i in range(len(vect2)):
                        yield vect2[i][0], (pop,vect2[i][1])

                if sub_file == 5:
                    if float(line[5]) != 0:
                        emp_d = emp_data(line)
                        vect = emp_d[1:]
                        pop = emp_d[0][1]
                        for i in range(len(vect)):
                            yield vect[i][0],(pop,vect[i][1])

                if sub_file == 6 and (float(line[146]) != 0):
                    yield "hh_income", (float(line[146]),float(line[87]))

    def combiner(self, field, V):
        '''
        Find average on node for each field, weighting by total population or
        number of households
        '''
        tot_pop = 0
        agg_v = 0
        v = list(V)
        for pop, v_ele in v:
            tot_pop += pop
            agg_v += v_ele*pop

        avg_ele = agg_v/tot_pop

        yield field , (tot_pop, avg_ele)

    def reducer(self, field, V):
        '''
        Find average on node for each field, weighting by total population or
        number of households
        '''

        tot_pop = 0
        agg_v = 0
        for pop, v_ele in list(V):
            tot_pop += pop
            agg_v += v_ele*pop

        avg_ele = agg_v/tot_pop

        yield field, round(avg_ele,2)

if __name__ == '__main__':
    make_vectors.run()
