import glob
import json
import matplotlib.pyplot as plt

'''
Condensed code to plot the json frames created by the springs simulation
'''

for filename in glob.glob('*.json'):
    outputname = filename.strip('.json')

    j   = json.load(open(filename,'r'))

    lons, lats = [],[]
    for placename, xy in j.items():

    plt.plot(xs,ys)
    plt.title(outputname)
    plt.savefig(outputname+'.png')
