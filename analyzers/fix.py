import json
f = open("json62.json",'r')
j = json.load(f)
new_dict = {}
for state in j["uSF1"].keys():
    for i in j["uSF1"][state]["tuples"].keys():
        new_dict[j["uSF1"][state]["tuples"][i][0]]=[j["uSF1"][state]["tuples"][i][1],j["uSF1"][state]["tuples"][i][2]]

json.dump(new_dict,(open("lon_lat.json",'w')))
