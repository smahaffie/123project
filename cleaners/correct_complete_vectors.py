from mrjob.job import MRJob as mrj
import csv
import json

'''
MapReduce code to generate vectors for every "place" in the US
Generates vectors with the name of the place, latitude, longtitude,
and data on race,employment,education,language etc.
'''

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

    return [    ("population",population),
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
    households = max(float(line[157]),1)
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
    '''
    tabulates foreign data on a place
    '''

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

    return [("population",pop),
        ("pct_full_time",pct_full_time),
        ("pct_part_time",pct_part_time),
        ("pct_no_work",pct_no_work)
        ]

class gen_vectors(mrj):
    '''
    construct vectors of containing relevant variables for every location
    '''
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(gen_vectors,self).configure_options()
        self.add_file_option('--index')

    def mapper_init(self):
        '''
        load json file with census places for every state
        '''
        with open(self.options.index,'r') as f:
            self.index_dict = json.load(f)

    def mapper(self,num, line):
        '''
        Use columns in the line that indicate which summary file and subfile and state
        the row refers to in order to map a key,value pair with the relevant variables
        yield key, value pairs
            key = place,string
            value = list of relevant variables from the given file
        '''
        line = line.split(",")
        state = line[1].upper()
        sum_file = line[0]
        index = str(int(line[4])-1) #indexing starts at 0
        sub_file = int(line[3])
        if str(index) in self.index_dict[sum_file][state]["indexes"]:
            place = self.index_dict[sum_file][state]["tuples"][index][0]
            lat = self.index_dict[sum_file][state.upper()]["tuples"][index][1]
            lon = self.index_dict[sum_file][state.upper()]["tuples"][index][2]
            if sum_file == "uSF1":
                if sub_file == 1 and (float(line[5]) != 0):
                        pop_d = pop_data(line)
                        for i in range(len(pop_d)):
                            yield (place,lat,lon),(pop_d[i][0], pop_d[i][1])

            if sum_file == "uSF3":
                if sub_file == 2:
                    if (float(line[171]) != 0):
                        lang_d = lang_data(line)
                        vect = lang_d[1:]
                        for i in range(len(vect)):
                            yield (place,lat,lon),(vect[i][0], vect[i][1])

                        foreign_d = foreign_data(line)
                        vect = foreign_d[1:]

                        for i in range(len(vect)):
                            yield (place,lat,lon), (vect[i][0], vect[i][1])

                if sub_file == 3 and float(line[161]) != 0:
                    ed_d = education_data(line)
                    vect2 = ed_d[1:]
                    for i in range(len(vect2)):
                        yield (place,lat,lon), (vect2[i][0], vect2[i][1])

                if sub_file == 5:
                    if float(line[5]) != 0:
                        emp_d = emp_data(line)
                        vect = emp_d[1:]
                        for i in range(len(vect)):
                            yield (place,lat,lon), (vect[i][0],vect[i][1])

                if sub_file == 6:
                    if (float(line[146]) != 0):
                        yield (place,lat,lon), ("hh_income", float(line[87]))

    def combiner(self, place, V):
        '''
        combine data for all characteristics of each place
        '''
        yield place, list(V)

    def reducer_init(self):
        '''
        create header row
        '''

        yield "place,lat,lon,", "population,foreign,native,hh_income,pct_english,pct_asian_lang,pct_spanish,pct_euro,pct_asian,pct_white,pct_black,pct_other,pct_hispanic,pct_full_time,pct_no_work,pct_part_time,pct_urban,less_than_hs,less_bachelors,doctorate"


    def reducer(self, place, V):
        '''
        Combine data for all characteristics of each place and write to file
        '''
        order1 = ["population","foreign","native","hh_income"]
        order2 = ["pct_english","pct_asian_lang","pct_spanish"]
        order3 =["pct_euro","pct_asian","pct_white","pct_black","pct_other"]
        order4 = ["pct_hispanic","pct_full_time","pct_no_work"]
        order5 = ["pct_part_time","pct_urban","less_than_hs","less_bachelors","doctorate"]

        order = order1 + order2 + order3 + order4 + order5

        v = list(V)
        list_tups = []
        for l in v:
            for tup in l:
                list_tups.append(tup)
        v = v[0]
        dictionary = {}
        list_string = []
        fields = []

        all_zeros = True

        for field,value in list_tups:
            dictionary[field] = str(round(value,4))

        for field in order:
            if field in dictionary.keys():
                if field != 0:
                    all_zeros = False
                list_string.append(dictionary[field])
            else:
                list_string.append("missing")

        to_yield = ",".join(list_string)

        place = list(place)
        p = ",".join(place) + ","
        if all_zeros==False: #avoid yielding completely missing data
            yield p, to_yield


if __name__ == '__main__':
    gen_vectors.run()
