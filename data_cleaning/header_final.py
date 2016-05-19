import csv
import re
import sys
import json

def find_lonlat( weirdlist):

	string = weirdlist[0] + weirdlist[1]

	regex = "[\+,-][0-9]{8,11}"
	res = re.findall(regex,string)
	if len(res) != 2:
		print("lan lot fail")
	try:
		lat = res[0][:3] + '.' + res[0][3:]
		lon = res[1][:4] + '.' + res[1][4:]
	except:
		print(res)
		print(string)
	lat = res[0][:3] + '.' + res[0][3:]
	lon = res[1][:4] + '.' + res[1][4:]

	return float(lat),float(lon)

def find_index_places(file):
	'''
	Inputs:
		file, string
	Side effects:
		writes a file where every row is a place and its index in all files within
		the specific summary file
	'''

	list_codes = []
	indexes = []
	state = file[:2]
	with open(file) as f:
		counter = 0
		for line in f:
			l = line.split()
			lat, lon = find_lonlat(l[-2:])

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
				list_codes.append([counter,name,lon,lat])
			counter += 1

	with open("{}_{}.csv".format(state,sum_file),'w') as f:
		writer = csv.writer(f)
		writer.writerows(list_codes)


if __name__=="__main__":
	find_index_places(sys.argv[1])

