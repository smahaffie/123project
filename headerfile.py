'''
Generates a list of all places within a state 
'''
import csv
import re
#def main(state,header_file):
'''
Inputs:
	state, string
	header_file, string
Side effects:
	csv listing the index of each place within the header file
'''
header_file = "algeo.txt"
state = "Alabama"

list_codes = []

with open(header_file) as f:
	counter = 0
	for line in f:
		l = line.split()
		code = l[3][:5]
		name_approx = line[195:220]
		if l[1][2:5] == "160":
			name = []
			for i in name_approx:
				if not i.isdigit() and i != " ":
					name.append(i)
			list_codes.append([counter,name])

with open("header_{}.csv".format(state),"w") as f:
	writer = csv.writer(f)
	writer.writerows(list_codes)
