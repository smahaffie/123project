import csv
import re
import math
import json
import sys

'''
Convert place data vectors vectors from a text file to a JSON format
'''
def create_json_vectors(inputfile):
    json_dict = {}
    state_list = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
    "GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
    "MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
    "ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
    "VA","WA","WV", "WI", "WY"]
    for state in state_list:
        json_dict[state] = []

    with open(inputfile, 'r') as f:
        reader = csv.reader(f)
        for line in f:
            _, name,lon,lat = line.split(',')

            placename,state = name.split('_')
            json_dict[state].append(name)


    with open("vectors_by_state.json",'w') as f:
        json.dump(json_dict,f)

if __name__ == '__main__':
    create_json_vectors(sys.argv[1])
