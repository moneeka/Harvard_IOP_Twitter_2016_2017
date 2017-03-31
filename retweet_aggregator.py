#This file takes in one parameter. THis is a data file containing all the cleaned phone number files that have been de duplicated and added to the 
#output file. From there, this program counts the number of retweets per tweet 

import json, datetime, unicodedata, os, sys

def retweet_aggregator(data_file)
	jsonfiles = []
	with open(data_file) as data_file:
		for line in data_file:
			if line != None:
				jsonfiles.append(line.rstrip('\n'))
	data_file.close()

	retweet_aggregator_dict = {}

	def retweet_aggregator_indiv(infile):
		with open(infile) as phoneFile:
			for tweet in phoneFile:
				if tweet['retweet_subobj'] == None:
					daily_count = {}
					daily_count_key = 'phoneFileDay' #change this to the name of the day, dude
					daily_count_value = 1
					daily_count[daily_count_key] = daily_count_value
					
					key = tweet['tweet_id']
					value = daily_count
					retweet_aggregator_dict[key] = value
				else:
					daily_count_key = 'phoneFileDay'
					retweet_id = tweet['retweet_suboj']['tweet_id']
					if daily_count_key in retweet_aggregator_dict[retweet_id][daily_count]:
						retweet_aggregator_dict[retweet_id][daily_count][daily_count_key] += 1
					else:
						retweet_aggregator_dict[retweet_id][daily_count][daily_count_key] = 1

	for jsonfile in jsonfiles:
		retweet_aggregator_indiv(jsonfile)
