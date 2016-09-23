from urllib2 import urlopen
import json
from textblob import TextBlob

with open('fox.txt') as inputfile:
	data = json.load(inputfile)
inputfile.close()

sent_added = []

for article in data:
	title = TextBlob(article['Title'])

	sentiment = title.sentiment.polarity
	subjectivity = title.sentiment.subjectivity


	piece = {'Title': article['Title'], 'PubDate': article['PubDate'], 'Sentiment': sentiment, 'Subjectivity': subjectivity}
	sent_added.append(piece)


f = open('fox.txt', 'w')
json.dump(sent_added, f)
f.close()

