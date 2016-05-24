import csv
import re
import math
import json

'''
Convert place data vectors vectors from a text file to a JSON format
'''
def create_json_vectors():
    json_dict = {}
	state_list = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
	"GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
	"MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
	"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
	"VA","WA","WV", "WI", "WY"]
    for state in state_list:
        json_dict[state] = []
        with open("{}_uSF1.csv", 'r') as f:
            reader = csv.reader(f)
            for line in f:
        

    with open("json_vectors.json",'w') as f:
    json.dump(json_dict,f)

if __name__ == '__main__':
    create_json_vectors()
