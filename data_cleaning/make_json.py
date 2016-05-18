import json
import csv

def create_json():
	'''
	Creates a json file which has containing the list of "places" for each state in the US
	and their corresponding indexes in each summary file
	'''

	state_list = ["AK","AL","AZ","AR","CA","CO","CT","DE","FL",
	"GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA",
	"MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
	"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
	"VA","WA","WV", "WI", "WY"]

	json_dict = {}
	json_dict["uSF1"] = {}
	json_dict["uSF3"] = {}

	for state in state_list:
		with open("{}_uSF1.csv".format(state.lower())) as f:
			json_dict["uSF1"][state] = {}
			json_dict["uSF1"][state]["indexes"] = []
			json_dict["uSF1"][state]["tuples"] = {}
			reader = csv.reader(f)
			for row in reader:
				json_dict["uSF1"][state]["tuples"][row[0]] = row[1]
				json_dict["uSF1"][state]["indexes"].append(row[0])

		with open("{}_uSF3.csv".format(state.lower())) as f:
			json_dict["uSF3"][state] = {}
			json_dict["uSF3"][state]["indexes"] = []
			json_dict["uSF3"][state]["tuples"] = {}
			reader = csv.reader(f)
			for row in reader:
				json_dict["uSF3"][state]["tuples"][row[0]]=row[1]
				json_dict["uSF3"][state]["indexes"].append(row[0])

	with open("json_dict.json",'w') as f:
		json.dump(json_dict,f)

if __name__=="__main__":
	create_json()
