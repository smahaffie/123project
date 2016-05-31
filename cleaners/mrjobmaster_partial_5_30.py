from mrjob.job import MRJob as mrj
import csv
import json
from mrjob.step import MRStep
import re
from math import radians, cos, sin, asin, sqrt
import networkx as nx
import sys
from scipy.spatial import ConvexHull
import heapq

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

def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculate the circle distance between two points
    on the earth (specified in decimal degrees)
    totally stolen from PA3 in 122
    '''
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km

def generate_pairs(line,index,vectors,N):

    name ,lon, lat = line[1:4]
    pairs = []
    #print(index)
    #print(N)
    #index += 1
    for n in range(index+1, N):
        p = vectors[n]
        pname,plon,plat = p[1:4]
        #print(pname,plon,plat)
        distance = 100
        try:
            distance = haversine(float(lon),float(lat),float(plon),float(plat))
        except:
            print("PANIC", p)
            pass
        if distance<15:
            pairs.append(pname)

    return pairs

def difference(a,b):
    '''
    finds difference between two places
    if data is missing we ignore that dimension
    we calculate the root mean squared distance between each dimension
    '''
    v = VECTORS_DICT[a][0].split(',')
    w = VECTORS_DICT[b][0].split(',')

    n = 0
    tot = 0
    for vi, wi in zip(v,w):
        if vi == 'missing' or wi == 'missing':
            continue
        n += 1
        tot += (float(vi)-float(wi))**2

    return (tot/n)**.5

def dykstra(origin):
    """
    Uses dykstra's algorithm to find shortest path to neighboring nodes
    returns subgraph of usa such that neighbors are within epsilon of origin
    """
    G = nx.Graph()
    G.add_node(origin,shortest_path = 0)
    active_nodes = [origin]

    while len(active_nodes) > 0:
        a_n     =  active_nodes.pop()   # active node

        for n in NEIGHBORDICT.get(a_n,[]):    #catch no neighbor exception
            d = difference(n, origin) ** 4    # increase cost of extra distance
            this_path = G.node[a_n]['shortest_path'] + d

            if this_path < EPSILON:
                if n in G.node:                                # seen this node before
                    if this_path < G.node[n]['shortest_path']: # if this path is better than previous best path
                        G.node[n]['shortest_path'] = this_path
                        G.add_edge(a_n,n)                      # add edge just because
                    continue

                G.add_node(n,shortest_path = this_path)   # if this is new, add it to graph
                G.add_edge(a_n,n)                 # add edge just because
                active_nodes.append(n)            # add new active node

    return G

class mr_master(mrj):
    '''
    construct vectors of containing relevant variables for every location
    '''
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(mr_master,self).configure_options()
        self.add_file_option('--index')

        self.add_file_option('--epsilon')

    def mapper_init_create_vectors(self):
        '''
        load json file with census places for every state
        '''
        with open(self.options.index,'r') as f:
            self.index_dict = json.load(f)

    def mapper_create_vectors(self,num, line):
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

    def combiner_create_vectors(self, place, V):
        '''
        combine data for all characteristics of each place
        '''
        yield place, list(V)

    def reducer_init_create_vectors(self):

        yield "place,lat,lon,population,foreign,native,hh_income,pct_english,pct_asian_lang,pct_spanish,pct_euro,pct_asian,pct_white,pct_black,pct_other,pct_hispanic,pct_full_time,pct_no_work,pct_part_time,pct_urban,less_than_hs,less_bachelors,doctorate", None

    def reducer_create_vectors(self, place, V):
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
        if all_zeros==False:
            global COUNTER
            global VECTORS
            global PLACES
            global VECTORS_DICT
            vector = str(COUNTER) + "," + p.replace('"','') + to_yield.strip().replace('"','')
            COUNTER += 1
            VECTORS.append(vector.split(","))
            VECTORS_DICT[place[0]] = place[1:] + vector.split(',')
            PLACES.append(place[0])
            yield vector, None

    def mapper_pairs(self,vector,_):
        global VECTORS
        line = vector.split(",")
        if line[0]!='place':
            index = int(line[0])
            place = line[1]
            pairs = generate_pairs(line,index,VECTORS,len(VECTORS))
            for p in pairs:
                yield place,p

    def reducer_pairs(self,place,p):
        '''
        global PAIRS
        PAIRS.append([place,p])
        '''
        for place2 in p:
            PAIRS.append([place,place2])

    def reducer_final_pairs(self):
        global NEIGHBORDICT
        for pair in PAIRS:
            place, neighbor = pair
            #print("PAIR",place,neighbor)
            neighbors = NEIGHBORDICT.get(place,[])
            neighbors.append(neighbor)
            NEIGHBORDICT[place] = neighbors
        with open("neighbors_json.json",'w') as f:
            json.dump(NEIGHBORDICT,f)

        global PLACES
        for place in PLACES:
            yield None, place

    def mapper_init_homogenous(self):
        '''
        load json file with census places for every state
        '''
        self.vectors = VECTORS_DICT
        self.neighbors = NEIGHBORDICT

    def mapper_homogenous(self,_,line):
        G = dykstra(line)

        selfv = self.vectors.get(line,None)
        if selfv == None:
            pass

        else:
            slon,slat = selfv[:2]

            output = []
            for n in G.nodes():
                v = self.vectors.get(n,None)
                if v == None:
                    continue
                lon,lat = v[:2]
                yield (line,slon,slat) , (n,lon,lat)

    def reducer_homogenous_to_surface_area(self,centre,nodes):
        """
        takes in a line, seperate centre of homeogenous area
        from all the nodes, then makes hull of points to proxy for area
        """

        cname, clon, clat = centre
        points = []
        for n in nodes:
            if n == '':
                continue
            nname, nlon, nlat = n
            points.append((float(nlon),float(nlat)))

        print(points)

        hull = ConvexHull(points)
        area  = hull.volume
        yield cname, area

    def mapper_surface_area(self, cname, area):
        yield cname, area

    def reducer_init_surface_area(self):
        """
        find top n with a heap
        """
        self.n = int(self.options.n)
        self.h = []
        for i in range(self.n):
            self.h.append((-99999999999,-9999999999))
        heapq.heapify(self.h)

    def reducer_surface_area(self, place, area):
        """
        find top n with a heap
        """
        min_count, min_n = self.h[0]

        l = list(area)
        assert len(l)==1
        area = l[0]

        if area > min_count:
            heapq.heapreplace(self.h, (area, place))

    def reducer_final_surface_area(self):
        '''
        sorts and yields the heap self.h
        '''
        self.h.sort(reverse=True)
        for (area,place) in self.h:
            yield place, abs(area)

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init_create_vectors,
                    mapper=self.mapper_create_vectors,
                    combiner=self.combiner_create_vectors,
                    reducer_init=self.reducer_init_create_vectors,
                    reducer=self.reducer_create_vectors),
            MRStep(mapper=self.mapper_pairs,
                    reducer=self.reducer_pairs,
                    reducer_final=self.reducer_final_pairs)
            #MRStep(mapper_init=self.mapper_init_homogenous,
            #        mapper=self.mapper_homogenous,
            #        reducer=self.reducer_homogenous_to_surface_area),
            #MRStep(mapper=self.mapper_surface_area,
            #        reducer_init=self.reducer_init_surface_area,
            #        reducer=self.reducer_surface_area,
            #        reducer_final=self.reducer_final_surface_area)
        ]

if __name__ == '__main__':
    VECTORS = []
    VECTORS_DICT = {}
    COUNTER = 0
    PAIRS = []
    NEIGHBORDICT = {}
    PLACES = []
    EPSILON = int(sys.argv[7])
    N = int(sys.argv[8])

    mr_master.run()
