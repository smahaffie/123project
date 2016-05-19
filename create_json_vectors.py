import csv
import re
import math
import json

#def create_summary_files():
json_dict = {}

with open("checkvectors.txt", 'r') as f:
    variables = f.readline().strip().split(',')[1:]

    data = []
    #places = []
    counter = 0
    for line in f:
        line = line.split('"')
        place = line[1]
        data = line[3:-1]
        place = place.split(",")
        name = place[0]
        lat = place[1]
        lon = place[2]
        #places.append(place[:-1])
        #line = line.split('"')[3].split(",")
        data = [lat] + [lon] + data
        if counter == 0:
            print(place,data)
        counter += 1
        json_dict[name] = data

with open("json_vectors.json",'w') as f:
	json.dump(json_dict,f)
