import random 

HEADER = ["population, pct_urban, pct_white, pct_indian, pct_black, pct_asian, pct_hispanic"]

with open("fake_data.csv", 'w') as f:
	for i in range(100):
		population = random.randint(10,90)
		pct_urban = random.randint(1,95)
		pct_white = random.randint(1,80)
		pct_indian = random.randint(1,100-pct_white-5)
		pct_black = random.randint(1, 100-pct_white-pct_indian-3)
		pct_asian = 100-pct_white-pct_indian-pct_black-pct_indian
		pct_hispanic = random.randint(2,90)
		f.write("town{}_{}|population,{}|pct_urban,{}|pct_white,{}|pct_indian,{}|pct_black,{}|pct_asian,{}|pct_hispanic,{}\n".format(i,"AL",population,pct_urban,pct_white,pct_asian, pct_black, pct_asian, pct_hispanic))
