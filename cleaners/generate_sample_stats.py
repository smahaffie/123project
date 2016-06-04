import csv
import re
import sys
import math

def create_summary_files(raw_file, data_file, avgs_file, stds_file):
    with open(raw_file, 'r') as f:
        add_variables = f.readline().strip().split(',')[3:]
        variables = ['lat', 'lon']
        for var in add_variables:
            var = var.replace('"','').strip()
            variables.append(var)

        data = []
        places = []
        for line in f:
            place = line.split('"')[1].split(",")[0]
            places.append(place)
            data_on_line = line.split('"')[1].split(",")[1:3] + line.split('"')[3].split(",")
            if data_on_line[0] != "lat":
                data.append(data_on_line)

    means = []
    stds = []
    for i in range(len(variables)-2):
        tot = 0
        missing = 0
        for line in data:

            if not line[i+2] == "missing":
                tot += float(line[i+2])
            else: 
                missing += 1

        mean = tot/(len(data)-missing)
        means.append("{0:.4f}".format(mean))

        squared_deviations = 0
        for line in data:
            if not line[i+2] == "missing":
                squared_deviations += (float(line[i+2])-mean) ** 2                

        std = math.sqrt(squared_deviations/(len(data)-missing)

        stds.append("{0:.4f}".format(std))

    with open(avgs_file, "w") as f:
        f.write(",".join(variables[2:]) + "\n")
        f.write(",".join(means) + "\n")

    with open(stds_file, "w") as f:
        f.write(",".join(variables[2:]) + "\n")
        f.write(",".join(stds) + "\n")

    with open(data_file, "w") as f:
        f.write("place," + ",".join(variables) + "\n")
        i = 0
        for line in data:
            f.write(places[i] + "," + ",".join(line) + "\n")
            i += 1

if __name__ == "__main__":
    create_summary_files(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

            

