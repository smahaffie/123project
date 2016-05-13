'''
Filters a file to only include all geographic "places"
'''

import csv
import re
import sys
import json

def filter_file(filename):
	'''
	Inputs:
		filename, string
	Side effects:
		new csv with only rows for "places" within the states
	'''

	state = filename[:2]
	indexes, list_codes = find_index_places(state)

	with open(filename) as f, open("{}_places.csv".format(filename),"w") as f1:
		counter = 0
		writer = csv.writer(f1)
		for row in f:
			if counter in indexes:
				writer.writerow(row)

def list_index_places(state):
	#state = filename[:2]
	indexes, list_codes = find_index_places(state)
	with open("index_{}.csv".format(state),'w') as f:
		writer = csv.writer(f)
		writer.writerows(indexes)
	with open("list_codes_{}.csv".format(state),'w') as f:
		writer = csv.writer(f)
		writer.writerows(list_codes)


def find_index_places(state):
	'''
	Inputs:
		state, string
	Returns:
		indexes, list
		list_codes, list
	'''

	list_codes = []
	indexes = []
	#abrr = state_dict[state]
	with open("{}geo.txt".format(state)) as f:
		counter = 0
		for line in f:
			l = line.split()
			code = l[3][:5]
			name_approx = line[195:220]
			if l[1][2:5] == "160":
				name = []
				#sorry, this is ugly. header is "fixed width" formatted
				for i in name_approx:
					if not i.isdigit() and i != " ":
						name.append(i)
				name = "".join(name)
				list_codes.append([counter,name])
				indexes.append([counter])
			counter += 1

	return indexes,list_codes


def create_json():
	state_list = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
	"GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
	"MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
	"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
	"VA","WA","WV", "WI", "WY"]
	json_dict = {}
	for state in state_list:
		with open("index_{}.csv".format(state.lower())) as f:
			json_dict[state] = []
			reader = csv.reader(f)
			for row in reader:
				json_dict[state].append(row[0])
	with open("json_dict.json",'w') as f:
		json.dump(json_dict,f)


if __name__=="__main__":
	#filename = sys.argv[1]

	state_list = ["AL"]

	for state in state_list:
		list_index_places(state)
