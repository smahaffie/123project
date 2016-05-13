import json
import csv

def create_json():
	'''
	Creates a json file containing the list of "places" for each state in the US


	state_list = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
	"GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
	"MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
	"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
	"VA","WA","WV", "WI", "WY"]'''

	state_list = ["AL"]

	json_dict = {}
	names_dict = []

	for state in state_list:
		with open("index_{}.csv".format(state.lower())) as f:
			json_dict[state] = []
			reader = csv.reader(f)
			for row in reader:
				json_dict[state].append(row[0])
		with open("list_codes_{}.csv".format(state),'r') as f:
			json_dict[state] = {}
			reader = csv.reader(f)
			for row in reader:
				json_dict[state][row[0]] = row[1]

	with open("json_dict.json",'w') as f:
		json.dump(json_dict,f)
'''
def create_json_2():
	state_list = ["Alabama","Alaska","Arizona","Arkansas","California",
	"Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho",
	"Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine",
	"Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri",
	"Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
	"New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon",
	"Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee",
	"Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin",
	"Wyoming"]
	json_dict = {}
	for state in state_list:
		with open("index_{}.csv".format(state.lower())) as f:'''

if __name__=="__main__":
	create_json()
