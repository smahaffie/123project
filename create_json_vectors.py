import csv
import re
import math
import json

'''
Convert place data vectors vectors from a text file to a JSON format
'''
def create_json_vectors():
    json_dict = {}

    with open("json_vectors.txt", 'r') as f:
    variables = f.readline().strip().split(',')[1:]

    data = []
    counter = 0
    for line in f:
        line = line.split('"')
        place = line[1]
        data = line[3:-1]
        place = place.split(",")
        name = place[0]
        lat = place[1]
        lon = place[2]
        data = [lat] + [lon] + data
        if counter == 0:
            print(place,data)
        counter += 1
        json_dict[name] = data

    with open("json_vectors.json",'w') as f:
    json.dump(json_dict,f)

if __name__ == '__main__':
    create_json_vectors()
