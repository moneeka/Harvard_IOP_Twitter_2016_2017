import json
import simplejson
from urllib2 import urlopen
import os


jsonfiles = ['hashtag_filtered_tweets2016-10-30.json']

os.chdir(os.getcwd()+'/hashtag_data_files')

def cleaner(tfile):
	
	jsons = []

	with open(tfile,'rU') as tweet_file:
		for tweet in tweet_file:
			try:
				j1 = json.loads(tweet[7:])
				jsons.append(j1)
			except:
				pass

		tweet_file.close()

	f = open('cleaned_'+tfile, 'w')
	json.dump(jsons, f)
	f.close()

for jsonfile in jsonfiles:
	cleaner(jsonfile)


