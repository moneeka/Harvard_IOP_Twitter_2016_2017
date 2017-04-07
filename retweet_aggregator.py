#This file takes in one parameter. THis is a data file containing all the cleaned phone number files that have been de duplicated and added to the 
#output file. From there, this program counts the number of retweets per tweet 

import json, datetime, unicodedata, os, sys

def retweet_aggregator(infile, date_string):
	data = []
	with open(infile, 'r') as data_file:
		i = 0
		for line in data_file:
			# converts each line into a json object
			data.append(json.loads(line))
			i += 1
	print "total tweets: " + str(i) 
	data_file.close()

	j = 0 
	k = 0
	for tweet in data:
		retweet_dates = {}
		if tweet['retweeted_status'] == {}:
			retweet_dates[date_string] = 1
			retweet_aggregator_dict[str(tweet["tweet_id"])] = retweet_dates

		else:
			original_tweet_id = str(tweet['retweeted_status']['tweet_id'])

			if original_tweet_id in retweet_aggregator_dict:

				if date_string in retweet_aggregator_dict[original_tweet_id]:
					retweet_aggregator_dict[original_tweet_id][date_string] += 1

				else:
					retweet_dates[date_string] = 1
					retweet_aggregator_dict[original_tweet_id].update(retweet_dates)
			
			else:
				retweet_dates[date_string] = 1
				retweet_aggregator_dict[original_tweet_id] = retweet_dates

	print "total original tweets: " + str(j)
	print "total retweets: " + str(k)

	with open('aggregated_retweets.json', 'w') as outfile:
		for tweet in retweet_aggregator_dict:
			outfile.write('{}'.format(json.dumps(tweet)))
			outfile.write(': ')
			outfile.write('{}\n'.format(json.dumps(retweet_aggregator_dict[tweet])))

# works through the directory and aggregates all the cleaned files per day
original_data_path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(original_data_path)
retweet_aggregator_dict = {}

# Assume that original data files contain the phrase 'cleaned_phone_data'
for n in files:
    if 'clean_phone_data_' in n:
        # separate out the parts of the name
        date_string = n[17:-5]
        print "Aggregating file: " + date_string
        retweet_aggregator(n, date_string)