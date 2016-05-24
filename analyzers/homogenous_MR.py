from mrjob.job import MRJob as mrj
import csv
import json
import networkx as nx




class make_graph(mrj):
    '''
    construct vectors of containing relevant variables for every location
    '''
    def configure_options(self):
        '''
        pass additional file to map reduce job
        '''
        super(make_graph,self).configure_options()
        self.add_file_option('--vectors')
        self.add_file_option('--neighbors')
        self.add_file_option('--epsilon')

    def difference(self,a,b):
        '''
        finds difference between two places
        if data is missing we ignore that dimension
        we calculate the root mean squared distance between each dimension
        '''
        v = self.vectors[a][0].split(',')
        w = self.vectors[b][0].split(',')
        
        n = 0
        tot = 0
        for vi, wi in zip(v,w):
            if vi == 'missing' or wi == 'missing':
                continue
            n += 1
            tot += (float(vi)-float(wi))**2

        return (tot/n)**.5

    def dykstra(self,origin):
        """
        Uses dykstra's algorithm to find shortest path to neighboring nodes
        returns subgraph of usa such that neighbors are within epsilon of origin 
        """
        G = nx.Graph()
        G.add_node(origin,shortest_path = 0)
        active_nodes = [origin]

        while len(active_nodes) > 0:
            a_n     =  active_nodes.pop()   # active node

            for n in self.neighbors.get(a_n,[]):    #catch no neighbor exception
                d = self.difference(n, origin)**4    # increase cost of extra distance
                this_path = G.node[a_n]['shortest_path'] + d

                if this_path < self.epsilon:
                    if n in G.node:                                # seen this node before
                        if this_path < G.node[n]['shortest_path']: # if this path is better than previous best path
                            G.node[n]['shortest_path'] = this_path   
                            G.add_edge(a_n,n)                      # add edge just because
                        continue

                    G.add_node(n,shortest_path = this_path)   # if this is new, add it to graph
                    G.add_edge(a_n,n)                 # add edge just because
                    active_nodes.append(n)            # add new active node
        return G

    def mapper_init(self):
        '''
        load json file with census places for every state
        '''
        self.vectors = json.load(open(self.options.vectors))
        self.neighbors = json.load(open(self.options.neighbors))
        self.epsilon = float(self.options.epsilon)

    def mapper(self,_,line):

        G = self.dykstra(line)
        yield line, ','.join(G.nodes())



if __name__ == "__main__":
    make_graph.run()













