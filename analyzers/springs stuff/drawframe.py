import json
import matplotlib.pyplot as plt

def drawframe(framefile):
    # given a json of position and momentum, plot position

    jsdict = json.load(open(framefile,'r'))
    j = [v for k,v in jsdict.items()]
    points = [(x,y) for x,y,px,py in j]
    xs = [x for x,y in points]
    ys = [y for x,y in points]
    plt.plot(xs,ys,'ro')
    plt.xlim([-1.75,0.25])
    plt.ylim([-0.75,0.75])
    plt.show()