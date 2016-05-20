import json
import networkx as nx
import heapq

JSV = json.load(open( "../json_vectors.json",'r'))
NEIGHBORS = json.load(open("neighbors.json",'r'))

def difference(a,b):
    '''
    finds difference between two places
    if data is missing we ignore that dimension
    '''

    v = JSV[a][0].split(',')
    w = JSV[b][0].split(',')
    
    n = 0
    tot = 0
    for vi, wi in zip(v,w):
        if vi == 'missing' or wi == 'missing':
            continue
        n += 1
        tot += (float(vi)-float(wi))**2

    return tot**.5


def dykstra(origin, epsilon):
    """
    Uses dykstra's algorithm to find shortest path to neighboring nodes
    returns subgraph of usa such that neighbors are within epsilon of origin 
    """
    G = nx.Graph()
    G.add_node(origin,shortest_path = 0,)
    active_nodes = [origin]

    while len(active_nodes) > 0:
        a_n     =  active_nodes.pop()   # active node

        for n in NEIGHBORS[a_n]:
            d = difference(n, origin)
            this_path = G.node[a_n]['shortest_path'] + d

            if this_path < epsilon:
                if n in G.node:                                # seen this node before
                    if this_path < G.node[n]['shortest_path']: # if this path is better than previous best path
                        G.node[n]['shortest_path'] = this_path   
                        G.add_edge(a_n,n)                      # add edge just because
                    continue

                G.add_node(n,shortest_path = this_path)   # if this is new, add it to graph
                G.add_edge(a_n,n)                 # add edge just because
                active_nodes.append(n)            # add new active node

    return G



"""

ALL PAIRS shortest path
    algorithm
        gotta figure it out...
        edges between neighboring nodes are their attr distances
        returns shortest paths between all pairs of nodes
        can construct homogenous area by filtering pairs by distance
        
        cheaper than running dykstra's for all places

        All pairs is order n^3

        dykstra's is n log n, so its faster to use dykstra's 


    social interpretation
        i dunno


Spring thing

    algorithm
        let each place be node and each edge a spring
        let resting length of a spring be proportional to attr distance
        Let physical location determine starting position 
        project longitude, lattitute onto an xy plane
        calculate how each node moves due to spring forces
        iterate until system stablizes

    social interpretation
        places that are close in both physical and attr spaces will cluster
        neighboring places with very different attributes will push apart
        this deformed picture of usa will be indicative of self segregation
        we should make a picture of the final state (or a gif of evolution)


"""
