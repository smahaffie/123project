from mrjob.job import MRJob as mrj
import csv
import json
from mrjob.step import MRStep
import math

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

    population = float(line[161])
    less_than_hs = 0

    for i in range(209,216):
        less_than_hs += float(line[i])
    for i in range(225,233):
        less_than_hs += float(line[i])

    hs = float(line[216]) + float(line[233])
    less_bachelors = (float(line[217]) + float(line[218]) + float(line[219])
    + float(line[234]) + float(line[235]) + float(line[236]))
    bachelors = float(line[220]) + float(line[237])
    doctorate = float(line[223]) + float(line[240])

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
    pct_full_time = (float(line[8]) + float(line[32]))/pop
    pct_part_time = (float(line[15]) + float(line[22]) + float(line[39]) + float(line[46]))/pop
    pct_no_work = (float(line[29]) + float(line[53]))/pop

    return [("population",pop),
        ("pct_full_time",pct_full_time),
        ("pct_part_time",pct_part_time),
        ("pct_no_work",pct_no_work)
        ]

class gen_vectors(mrj):
    '''
    construct vectors of national averages for different measures
    '''
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(gen_vectors,self).configure_options()
        self.add_file_option('--index')

    def mapper_init(self):

        with open(self.options.index,'r') as f:
            self.index_dict = json.load(f)

    def mapper(self,num, line):
        line = line.split(",")
        state = line[1].lower()
        sum_file = line[0]
        index = str(int(line[4])-1) #indexing starts at 0
        sub_file = int(line[3])

        if index in self.index_dict[sum_file][state.upper()]["indexes"]:
            place = self.index_dict[sum_file][state.upper()]["tuples"][index]
            #yield place, ("test","test")
            if sum_file == "uSF1":
                if sub_file == 1 and (float(line[5]) != 0):
                        pop_d = pop_data(line)
                        pop = pop_d[0][1]
                        vect = pop_d[1:]
                        yield place, ("population",pop)
                        for i in range(len(vect)):
                            yield place,(vect[i][0], vect[i][1])

            if sum_file == "uSF3":
                if sub_file == 2 and (float(line[171]) != 0):
                    lang_d = lang_data(line)
                    households = lang_d[0][1]
                    vect = lang_d[1:]
                    for i in range(len(vect)):
                        yield place,(vect[i][0], vect[i][1])

                    foreign_d = foreign_data(line)
                    population = foreign_d[0][1]
                    vect = foreign_d[1:]

                    for i in range(len(vect)):
                        yield place, (vect[i][0], vect[i][1])

                if sub_file == 5:
                    print("!!!")
                    if float(line[5]) != 0:
                        emp_d = emp_data(line)
                        pop = emp_d[0][1]
                        vect = emp_d[1:]
                        for i in range(len(vect)):
                            yield place, (vect[i][0],vect[i][1])

                if sub_file == 6:
                    print("!!")
                    if (float(line[146]) != 0):
                        yield place, ("hh_income", float(line[87]))

    def combiner(self, place, V):
        '''
        Find average on node for each field, weighting by total population or
        number of households
        '''
        yield place, list(V)

    def reducer(self, place, V):
        '''
        Find average on node for each field, weighting by total population or
        number of households
        '''
        order1 = ["population","foreign","native","hh_income"]
        order2 = ["pct_english","pct_asian_lang","pct_spanish"]
        order3 =["pct_euro","pct_asian","pct_white","pct_black","pct_other"]
        order4 = ["pct_hispanic","pct_full_time","pct_no_work"]
        order5 = ["pct_part_time","pct_urban"]
        order = order1 + order2 + order3 + order4 + order5

        v = list(V)[0]
        dictionary = {}
        list_string = []
        fields = []
        for field,value in v:
            dictionary[field] = str(round(value,4))
            #list_string.append(str(round(value,4)))
            #fields.append(field)

        for field in order:
            if field in dictionary.keys():
                list_string.append(dictionary[field])
            else:
                list_string.append("missing")

        to_yield = ",".join(list_string)
        #field = ",".join(fields)

        place = place + ","

        #yield place,field
        yield place, to_yield


if __name__ == '__main__':
    gen_vectors.run()
