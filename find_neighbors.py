import re
import networkx as nx
from math import radians, cos, sin, asin, sqrt
import heapq

ADJACENCY  = "county_adjacency.txt"




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

def find_neighbors(vector):
    """
    takes a vector and find's neighbors
    neighbors are defined as
    places within 96km
    (1 hour * 60mph)
    """
    neighbors = []

    vector_table = []   # :C

    for w in vector_table:
        distance = haversine(w[lon],w[lat],vector[lon],vector[lat])
        if distance <= 96:
            neighbors.append(w)

    return neighbors

def dykstra(origin, epsilon):
    """
    Uses dykstra's algorithm to find shortest path to neighboring nodes
    returns subgraph of usa such that neighbors are within epsilon of origin 
    """
    G = nx.graph()
    G.add_node(origin[name],shortest_path = 0,vector = origin)
    active_nodes = [origin]

    while len(active_nodes) > 0:
        a_n     =  active_nodes.pop()   # active node

        for n in find_neighbors( G.node[a_n]['vector'] ):
            d = difference(n, origin)
            this_path = G.node[a_n]['shortest_path'] + d

            if this_path < epsilon:
                if n[name] in g.node:                                # seen this node before
                    if this_path < g.node[n[name]]['shortest_path']: # if this path is better than previous best path
                        g.node[n[name]]['shortest_path'] = this_path   
                        G.add_edge(a_n,n[name])                      # add edge just because
                    continue

                g.add_node(n[name],shortest_path = this_path, vector = n)   # if this is new, add it to graph
                g.add_edge(a_n,n[name])                 # add edge just because
                active_nodes.append(n[name])            # add new active node

    return G



"""

ALL PAIRS shortest path

Spring thingy

"""




def difference(v,w):
    '''
    returns difference between two census places
    by euclidian distance between attribute vectors
    '''
    return 0
