import json
import matplotlib.pyplot as plt
import matplotlib
import glob
import re

States = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
        "GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
        "MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
        "ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
        "VA","WA","WV", "WI", "WY"]

def prettify_state():
    """
    returns a dict {states:color code}
    """
    colors = matplotlib.colors.cnames
    chosen = np.random.choice(colors.keys(),len(States),False)

    return dict(zip(states,chosen))


def drawframe(framefile):
    # given a json of position and momentum, plot position

    jsdict = json.load(open(framefile,'r'))
    j = [v for k,v in jsdict.items()]
    points = [(x,y) for x,y,px,py in j]
    xs = [x for x,y in points]
    ys = [y for x,y in points]
    plt.plot(xs,ys,'ro')
    plt.show()

def show():
    i = 0
    while True:
        drawframe('frame{}.json'.format(i))
        i+=1


def draw_pretty_frame(framefile,outfile,colordict):

    jsdict = json.load(open(framefile,'r'))
    for s in States:
        j = [v for k,v in jsdict.items() if k[-2:]== s]
        points = [(x,y) for x,y,px,py in j]
        xs = [x for x,y in points]
        ys = [y for x,y in points]
        plt.plot(xs,ys,colordict[s])

    plt.savefig(outfile)

def draw_pretty_things():

    frames = glob.glob('frame*.json')
    colordict = prettify_state()
    for f in frames:
        outname = f.strip('.json')
        drawframe(f,outname,colordict)
