import json, datetime, unicodedata, os, sys

def retweeterDict(infile):
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
					key = retweet['user']['screen_name'] + '%' + retweet['text']
					valueText = t['user']['screen_name'] + '%' + t['created_at'] + '%' + t['user']['location']
					value = [valueText]
					if key in dictionary:
						originalList = dictionary[key]
						originalList.append(valueText)
						dictionary[key] = originalList
					else:
						dictionary[key] = value
	print dictionary

retweeterDict('cleanPhoneData_2017-02-19.json')