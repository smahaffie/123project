import numpy as np
import json
from functools import partial
from mpi4py import MPI
import sys
import os
import datetime
import glob


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

    y = lon / np.pi
    x = np.log(  (1+np.sin(lat))/(1-np.sin(lat))  ) / (4*np.pi)

    return x,y

def undo_mercator_project(x,y):
    """
    x,y to lon, lat
    """
    lon = y*np.pi
    ex = np.exp(4*np.pi*x)
    lat = np.arcsin((ex - 1)/(ex +1 ))

    lon = lon*360/2/np.pi # radians to degrees
    lat = lat*360 /2/np.pi

    return lon, lat

def difference(a,b,vectors):
    '''
    finds difference between two places
    if data is missing we ignore that dimension
    we calculate the root mean squared distance between each dimension
    '''
    v = vectors[a]#[0].split(',')
    w = vectors[b]#[0].split(',')

    n = 0
    tot = 0
    for vi, wi in zip(v,w):
        if vi == 'missing' or wi == 'missing':
            continue
        n += 1
        tot += (float(vi)-float(wi))**2

    return (tot/n)**.5


def fix_neighbors_vectors(neighbors,vectors,lonlats):
    """
    Make sure the keys are okay
    """
    common = set(neighbors.keys()) & set(vectors.keys()) & set(lonlats.keys())
    n = {}
    v = {}
    for c in common:
        v[c] = vectors[c]
        n[c] = [x for x in neighbors[c] if x in common]
    return n,v


def original_xy(vectors,lonlats):
    """
    turns vectors into names and locations
    """
    xy = {}
    for name,vect in vectors.items():
        lon,lat = lonlats[name]
        try:
            lon,lat = float(lon),float(lat)
        except:
            continue
        x,y = mercator_projection(lon,lat)
        px,py = 0,0
        xy[name] = (x,y,px,py)
    return xy

def resting_length(xy,neighbors,vectors,average_pair_distance):
    """
    finds the resting length of springs
    also fixes xy, neighbors to prevent future key errors
    """
    rl = {}
    remove = []
    for place, position in xy.items():
        xp, yp, _, __ = position
        for n in neighbors[place]:
            npos = xy.get(n,None)
            if npos == None:
                neighbors[place].remove(n)
                continue
            xn, yn,_,__ = npos
            geo_distance = np.sqrt((xp - xn)**2 + (yp - yn)**2)
            rl[(place,n)] = geo_distance * difference(place,n,vectors)/average_pair_distance
        if len(neighbors[place])==0:
            remove.append(place) # place has no good neighbors
    for r in remove:
        xy.pop(r,None)
        neighbors.pop(r,None)
    return rl,neighbors,xy

def next_xy (all_xy, rl, neighbors, name):
    """
    calculates change in location for a place
    returns a tuple to be turned into a dict,
        and change to be compared against epsilon
    """
    damping_coeff  = 0.8
    springconstant = 0.01

    x,y,px,py = all_xy[name]
    Fx = 0
    Fy = 0
    for n in neighbors[name]:
        a = all_xy.get(n,None)
        if a == None:
            continue
        nx, ny, npx, npy = a
        distance_xy_n = np.sqrt((x-nx)**2+(y-ny)**2)
        force = ( rl[(name,n)] - distance_xy_n ) * springconstant
        Fx += force * (x-nx)/distance_xy_n
        Fy += force * (y-ny)/distance_xy_n
    px += Fx    #   change in momentum = force * time
    py += Fy    #   time unit is 1 for simplicity
    px *= damping_coeff    #   friction-like force to damp ossilation
    py *= damping_coeff    #   so we achieve stopping condition

    movement = np.sqrt(px**2 + py**2)
    return (name, (x + px, y + py, px, py)), movement

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

# Establishing globals
neighborsfile           = '../neighbors.json'
vectorsfile             = '../../cleaned_data/json_vectors.json'
lonlatsfile             = 'lonlat.json'
average_pair_distance   = 1.3999
epsilon                 = .001
saveallframes           = True
if len(sys.argv) == 5:
    neighborsfile           = sys.argv[1]
    vectorsfile             = sys.argv[2]
    lonlatsfile             = sys.argv[3]
    average_pair_distance   = float(sys.argv[4])
elif len(sys.argv) != 1:
    print(" Arguments in order:\n "
        "neighbors, vectors, allnames,\n"
        "average pair distance, epsilon,\n"
        " save all frames (0 or 1)")

if __name__ == '__main__':
    # MPI simulation !

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # File details
   
    neighbors,rl,xy,outputdir,epsilon = [None]*5
    if rank == 0:
        outputdir = "springout_"+str(datetime.datetime.now())
        if saveallframes:
            os.mkdir(outputdir)
        print('loading')
        neighbors   = json.load(open(neighborsfile,'r'))
        vectors     = json.load(open(vectorsfile,'r'))
        lonlats     = json.load(open(lonlatsfile,'r'))
        neighbors,vectors = fix_neighbors_vectors(neighbors,vectors,lonlats)
        print('fixed keys')
        xy = original_xy(vectors,lonlats)
        print('xy made with length:%d'%len(xy.items()))
        rl,neighbors,xy = resting_length(xy,neighbors,vectors,average_pair_distance)

#        for n, l in neighbors.items():
 #           neighbors[n]=[x for x in l if x in xy.keys()]

  #      for p in xy.keys():
   #         neighbors[p] = [n for n in neighbors[n] if (p,n) in rl.keys()]

    #    print('fixed keys2')

        if saveallframes:
            json.dump(xy,open("%s/frame0.json"%outputdir,'w'))
            print('saved')
    # Broadcast information that won't change
    epsilon = 0.001
    comm.barrier()
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
        for name in my_xys:                   # do tasks
            r, change = next_xy(xy, rl, neighbors, name)
            res.append(r)
            if change > int_max_change:
                int_max_change = change
      #  print("rank %d: simulation complete"%rank)

        gathered_chunks = comm.gather(res,root = 0)          # gather results
        changes = comm.gather(int_max_change,root = 0)

        if rank == 0:                                        # process results
            xy = dict(sum(gathered_chunks,[]))
            max_change = max(changes)
            if saveallframes:
                json.dump(xy,
                    open("{0}/frame{1}.json".format(outputdir,sim_num),'w'))

        max_change = comm.bcast(max_change,root = 0)         # update max_change
        sim_num += 1
        if rank == 0:
            print("max change:%f\n"%max_change)


    MPI.COMM_WORLD.Abort()
