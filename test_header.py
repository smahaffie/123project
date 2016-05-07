import csv

with open("header_Alabama.csv") as f, open("al00001.txt") as f1:
	reader = csv.reader(f)
	indexes = []
	test = []

	for line in reader:
		indexes.append(line[0])

	counter = 0
	print(indexes)

	for line in f1:
		if counter == "190095":
			print("!!!")
		if str(counter) in indexes:
			l = line.split()
			l1 = l[0].split(",")
			print(l1)
			test.append([l1[5],counter])
		counter += 1

print(test)

