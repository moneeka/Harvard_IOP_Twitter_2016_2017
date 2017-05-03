import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
import json

#make sure phone number data from Google Drive is in a subdirectory of the
#current directory called "PhoneNumberData" 

def nom_mentions(infile, nominee):
    ctr = 0
    with open(infile, 'r') as data_file:
        for line in data_file:
        	try:
        		json_line = json.loads(line)
        		if nominee in json_line['text']:
        			ctr += 1
        	except:
        		pass

    return(ctr)

data_path = os.chdir("PhoneNumberData")
current = os.getcwd()
files = os.listdir(current)

#make sure number of labels and number of colors match
nom_list = ['Tillerson','Sessions','Flynn','DeVos']
color_list = ['g','b','r','k']

for nom, color in zip(nom_list, color_list):
	mention_counts = []
	dates = []
	for n in files:
		date_string = n[11:-5]
		dt_string = dt.strptime(date_string, '%Y-%m-%d')
		dates.append(dt_string)
		mention_count = nom_mentions(n, nom)
		mention_counts.append(mention_count)

	plt.plot(dates, mention_counts, color)

plt.legend(nom_list)
plt.show()
