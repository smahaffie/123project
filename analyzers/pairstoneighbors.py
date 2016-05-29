import sys
import json


if __name__ == '__main__':
    """
    takes the pairs file and makes a dictionary 
    mapping places to a list of their neighbors
    also writes a file of all placenames as input to surfacearea.py
    """
    _, pairsfile, neighborsfile, allplacesfile = sys.argv

    f = open(pairsfile,'r')

    neighbordict = {}

    for line in f:

        place, neighbor = line.strip().replace('"','').split('\t')

        neighbors = neighbordict.get(place,[])
        neighbors.append(neighbor)
        neighbordict[place] = neighbors

    g = open(neighborsfile,'w')
    json.dump(neighbordict,g)

    h = open(allplacesfile,'w')
    for name in neighbordict.keys():
        h.write(name + '\n')

    f.close()
    g.close()
    h.close()