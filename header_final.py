import csv
import re
import sys
import json

def find_index_places(file):
	'''
	Inputs:
		state, string
	Returns:
		indexes, list
		list_codes, list
	'''
	list_codes = []
	indexes = []
	state = file[:2]
	with open(file) as f:
		counter = 0
		for line in f:
			l = line.split()
			code = l[3][:5]
			sum_file = l[0]
			name_approx = line[195:220]
			if l[1][2:5] == "160":
				name = []
				#sorry, this is ugly. header is "fixed width" formatted
				for i in name_approx:
					if not i.isdigit() and i != " ":
						name.append(i)
				name = "".join(name)
				name = name + "_{}".format(state)
				list_codes.append([counter,name])
			counter += 1

	with open("{}_{}.csv".format(state,sum_file),'w') as f:
		writer = csv.writer(f)
		writer.writerows(list_codes)


if __name__=="__main__":
	find_index_places(sys.argv[1])
