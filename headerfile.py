'''
Filters a file to only include all geographic "places"
'''

import csv
import re
import sys

def filter_file(filename):
	'''
	Inputs:
		filename, string
	Side effects:
		new csv with only rows for "places" within the states
	'''

	state = filename[:2]
	indexes, list_codes = find_index_places(state)

	with open(filename) as f, open("~/bucket/Summary_File_1/Alabama/{}_places.csv".format(filename),"w") as f1:
		counter = 0
		writer = csv.writer(f1)
		for row in f:
			if counter in indexes:
				writer.writerow(row)

def list_index_places(state):
	state = filename[:2]
	indexes, list_codes = find_index_places(state)
	with open("index_{}.csv".format(state),'w') as f:
		writer = csv.writer(f)
		writer.writerows(indexes)


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



if __name__=="__main__":
	num_args = len(sys.argv)
	filename = sys.argv[1]
	list_index_places(filename)
