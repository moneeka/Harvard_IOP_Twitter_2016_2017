import json, datetime, unicodedata, os, sys

def retweeterDict(data_file)	
	jsonfiles = []
	with open(data_file) as data_file:
		for line in data_file:
			if line != None:
				jsonfiles.append(line.rstrip('\n'))
	data_file.close()

	def retweeterDictCleaner(infile):
		dictionary = {}
		with open(infile) as phoneFile:
			for tweet in phoneFile:
				try:
					tweet = json.loads(tweet)
				except:
					continue
				for t in tweet:
					retweet = t['retweeted_status']
					if(any(retweet)):
						key = retweet['user']['screen_name'] + '%' + retweet['user']['user_id'] + '%' + retweet['text'] + '%' + retweet['tweet_id']
						valueText = t['user']['screen_name'] + '%' + t['created_at'] + '%' + t['user']['location'] + '%' + t['user']['user_id']
						value = [valueText]
						if key in dictionary:
							originalList = dictionary[key]
							originalList.append(valueText)
							dictionary[key] = originalList
						else:
							dictionary[key] = value
		print dictionary

	for jsonfile in jsonfiles:
		retweeterDictCleaner(jsonfile)

# retweeterDict('') <--insert name of the file containing the json files.