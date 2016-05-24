import json
import networkx as nx
import heapq
import sys


#    neighbor_dict = json.load(open("neighbors.json",'r'))

#    vectors = json.load(open( "../json_vectors.json",'r'))

def difference(a,b,vectors):
    '''
    finds difference between two places
    if data is missing we ignore that dimension
    we calculate the root mean squared distance between each dimension
    '''

    v = vectors[a][0].split(',')
    w = vectors[b][0].split(',')
    
    n = 0
    tot = 0
    for vi, wi in zip(v,w):
        if vi == 'missing' or wi == 'missing':
            continue
        n += 1
        tot += (float(vi)-float(wi))**2

    return (tot/n)**.5


def dykstra(origin, epsilon,neighbor_dict,vectors):
    """
    Uses dykstra's algorithm to find shortest path to neighboring nodes
    returns subgraph of usa such that neighbors are within epsilon of origin 
    """
    G = nx.Graph()
    G.add_node(origin,shortest_path = 0)
    active_nodes = [origin]

    while len(active_nodes) > 0:
        a_n     =  active_nodes.pop()   # active node

        for n in neighbor_dict[a_n]:
            d = difference(n, origin,vectors)**2    # increase cost of extra distance
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

if __name__ == "__main__":

    _, neighbors_file, json_vectors_file, placenames, start, stop = sys.argv

    neighbor_dict = json.load(open(neighbors_file,'r'))
    vectors       = json.load(open(json_vectors_file ,'r'))

    f = open(placenames,'r')
    f.seek(start)

    f2 = open("dykstra_res.txt",'w')

    while f.tell() < stop:
        origin = f.readline()
        epsilon = 5
        G = dykstra(origin,epsilon,neighbor_dict,vectors)
        nodes = G.nodes()
        f2.write("%s|%s \n"%(origin,','.join(nodes)))

    f.close()
    f2.close()

