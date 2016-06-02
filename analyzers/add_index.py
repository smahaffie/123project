import csv
import sys

'''
Code to add an index column entry to every row in a file
'''

rows = []

def add_index(file):
    with open(file) as f:
        f.readline()
        reader = csv.reader(f)
        counter = 0
        for line in reader:
            line = [counter] + line
            rows.append(line)
            counter += 1

    with open("{}_indexes.csv".format(file[:-3]),'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main___":
    add_index(sys.argv[1])
