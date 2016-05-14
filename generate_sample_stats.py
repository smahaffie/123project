import csv
import re
import math

def create_summary_files():
    with open("sample_vectors.txt", 'r') as f:
        variables = f.readline().strip().split(',')[1:]

        data = []
        places = []
        for line in f:
            place = line.split('"')[1]
            places.append(place[:-1])
            line = line.split('"')[3].split(",")
            data.append(line)

    means = []
    stds = []
    for i in range(len(variables)):
        tot = 0
        for line in data:
            if not line[i] == "missing":
                tot += float(line[i])

        mean = tot/len(data)
        means.append("{0:.4f}".format(mean))

        squared_deviations = 0
        for line in data:
            if not line[i] == "missing":
                squared_deviations += (float(line[i])-mean) ** 2

        std = math.sqrt(squared_deviations/len(data))

        stds.append("{0:.4f}".format(std))

    with open("sample_averages.csv", "w") as f:
        f.write(",".join(variables) + "\n")
        f.write(",".join(means) + "\n")

    with open("sample_stds.csv", "w") as f:
        f.write(",".join(variables) + "\n")
        f.write(",".join(stds) + "\n")

    with open("sample_data.csv", "w") as f:
        f.write("place," + ",".join(variables) + "\n")
        i = 0
        for line in data:
            f.write(places[i] + "," + ",".join(line) + "\n")
            i += 1




            

