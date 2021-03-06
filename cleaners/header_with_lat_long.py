import csv
import re
import sys
import json

'''
Parses the geo files for every state in order to determine what row indexes for each state correspond to census places in the US
The csv files that are created are then used by "create_json.py" which creates a dictionary
that stores the key information about every place that we need in order to complete the
analysis

Usage: just call the function from the command line. Requires that all of the geo
header files are located in the directory from which the file is being called
'''

def find_lonlat( line):
'''
Use regex to find the latitude and longitude of a place from the fixed width header file
'''
	regex = "[\+,-][0-9]{8}"
	regex = "[\+,-][0-9]{8,11}"
	res = re.findall(regex,line)
	if len(res) != 2:
		print("lan lot fail")
	try:
		lat = res[0][:3] + '.' + res[0][3:]
		lon = res[1][:4] + '.' + res[1][4:]
	except:
		lat = res[0][:3] + '.' + res[0][3:]
		lon = res[1][:4] + '.' + res[1][4:]

	return float(lat),float(lon)

def find_index_places(file,state):
	'''
	Inputs:
		file, string
	Side effects:
		writes a file where every row is a place and its index in all files within
		the specific summary file
	'''

	list_codes = []
	indexes = []

	with open(file) as f:
		counter = 0
		for line in f:
			l = line.split()
			lat, lon = find_lonlat(line)

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
				list_codes.append([counter,name,round(lat,4),round(lon,4)])
			counter += 1

	with open("{}_{}.csv".format(state,sum_file),'w') as f:
		writer = csv.writer(f)
		writer.writerows(list_codes)


if __name__=="__main__":
	for state in ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
		"GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
		"MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
		"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
		"VA","WA","WV", "WI", "WY"]:
		find_index_places("{}geo.uf1".format(state.lower()),state)
		find_index_places("{}geo.uf3".format(state.lower()),state)
