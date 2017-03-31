import json
from urllib2 import urlopen
import os

def json_clean(data_file, output_file):
	jsonfiles = []
	with open(data_file) as data_file:
		for line in data_file:
			if line != None:
				jsonfiles.append(line.rstrip('\n'))
	data_file.close()

	names = jsonfiles

	def cleaner(t_file):
		
		jsons = []

		with open(t_file,'rU') as tweet_file:
			for tweet in tweet_file:
				try:
					j1 = json.loads(tweet[7:])
					jsons.append(j1)
				except:
					pass

		tweet_file.close()

		txt_val = t_file.index('.json')
		pure_name = t_file[:txt_val]

		f = open(pure_name+'_cleaned.txt', 'w')
		json.dump(jsons, f)
		f.close()

		f1 = open(output_file, 'w')
		f1.write(pure_name+'_cleaned.txt' + '\n')
		f1.close()

	for jsonfile in jsonfiles:
		cleaner(jsonfile)