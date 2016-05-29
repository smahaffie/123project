import numpy as np
import json
from functools import partial
from mpi4py import MPI
import sys
import os
import datetime


"""
simulation functions
overview:
    we project places from lon,lat to x,y
    let neighboring places (as defined in homogenous.py)
        share a spring between them with spring constant 1
        and resting spring length their attr distance
        as a percentage of mean attr distance
    calculate delta x due to force of surrounding springs
    continue until convergence
"""

def mercator_projection(lon,lat):
    """
    projects longitue, latitude to x,y
    its kind of distortionary but whatever
    """
    lon = lon * 2 * np.pi / 360 # degrees to radians
    lat = lat * 2 * np.pi / 360

    x = lon / np.pi
    y = np.log(  (1+np.sin(lat))/(1-np.sin(lat))  ) / (4*np.pi)

    return x,y

    
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

def original_xy(placenamesfile,vectors):
    """
    reads in places, turns them into names and locations
    """
    xy = {}
    for p in open(placenamesfile,'r'):
        p = p.strip()
        vector_p = vectors.get(p,None)
        if vector_p == None:
            continue
        lon, lat = vector_p[:2]
        xy[p] = mercator_projection(float(lon),float(lat))
    return xy

def resting_length(xy,neighbors,vectors,average_pair_distance):
    """
    generates dict of resting spring lengths
    """
    rl = {}
    for p,neighbors in neighbors.items():
        for n in neighbors:
            px,py = xy.get(p,(None,None))
            if px ==None:
                continue
            nx,ny = xy[n]
            geo_distance = np.sqrt((px - nx)**2 + (py - ny)**2) 
            rl[(p,n)] = geo_distance * difference(p,n,vectors)/average_pair_distance
    return rl



def next_xy (all_xy, rl, neighbors, name):
    """
    calculates change in location for a place
    returns a tuple to be turned into a dict,
        and change to be compared against epsilon
    """
    x,y = all_xy[name]
    deltax = 0
    deltay = 0
    for n in neighbors[name]:
        nx, ny = all_xy[n]
        distance_xy_n = np.sqrt((x-nx)**2+(y-ny)**2)
        force = rl[(name,n)]*distance_xy_n

        deltax += -force*(x-nx)/distance_xy_n
        deltay += -force*(y-ny)/distance_xy_n

    movement = np.sqrt(deltax**2 + deltay**2)
    return (name, (x + deltax, y + deltay)), movement

"""
    MPI stuff
"""

def chunks(somelist, size):
    """
    splits up a list into mostly equal sized bits
    """
    chunks = {}

    for n,stuff in enumerate(somelist):
        c = chunks.get(n%size,[])
        c.append(stuff)
        chunks[n%size] = c

    for i in range(size):
        yield chunks[i]



if __name__ == '__main__':
    # MPI simulation !

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # File details
    neighbors,rl,xy,outputdir,epsilon = [None]*5
    if rank == 0:

        neighborsfile           = 'neighbors.json'
        vectorsfile             = '../cleaned_data/json_vectors.json'
        placenamesfile          = 'allnames.txt'
        average_pair_distance   = 2
        epsilon                 = .001
        outputdir               = "springout_"+str(datetime.datetime.now())
        saveallframes           = True

        if len(sys.argv) == 6:
            neighborsfile           = sys.argv[1]
            vectorsfile             = sys.argv[2]
            placenamesfile          = sys.argv[3]
            average_pair_distance   = sys.argv[4]
            epsilon                 = sys.argv[5]
            saveallframes           = bool(sys.argv[6])
        elif len(sys.argv) != 1:
            print(" Arguments in order:\n "
                "neighbors, vectors, allnames,\n"
                "average pair distance, epsilon,\n"
                " save all frames (0 or 1)")

        os.mkdir(outputdir)

        neighbors   = json.load(open(neighborsfile,'r'))
        vectors     = json.load(open(vectorsfile,'r'))
        xy          = original_xy(placenamesfile,vectors)
        rl          = resting_length(xy,neighbors,vectors,average_pair_distance)

        if saveallframes:
            json.dump(xy,open("%s/frame0.json"%outputdir,'w'))


    # Broadcast information that won't change
    neighbors = comm.bcast(neighbors,root = 0)
    rl = comm.bcast(rl, root = 0)

    # run simulations until maximum change is smaller than epsilon
    max_change = float('inf')
    sim_num = 1
    while epsilon < max_change:
        if rank == 0:
            print("simulation number %d"%sim_num)

        xy = comm.bcast(xy, root = 0)                         # update locations
        my_xys = None
        my_xys = comm.scatter(chunks(xy.keys(),size),root = 0)# distribute tasks
        int_max_change = 0
        res = []

        for num, name in enumerate(my_xys):                   # do tasks
            r, change = next_xy(xy, rl, neighbors, name)
            res.append(r)
            if change > int_max_change:
                int_max_change = change
        print("rank %d: simulation complete"%rank)

        gathered_chunks = comm.gather(res,root = 0)          # gather results         
        changes = comm.gather(int_max_change,root = 0)
        sim_num += 1

        if rank == 0:                                        # process results
            xy = dict(sum(gathered_chunks,[]))
            max_change = max(changes)
            if saveallframes:
                json.dump(xy,
                    open("{0}/frame{1}.json".format(outputdir,sim_num),'w'))  

        max_change = comm.bcast(max_change,root = 0)         # update max_change
        if rank == 0:
            print("max change:%f\n"%max_change)

    if rank == 0:
        print("DONE!")

    MPI.COMM_WORLD.Abort()



