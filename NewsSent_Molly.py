#get a new API key and install aylienapiclient from https://developer.aylien.com/

from aylienapiclient import textapi
from urllib2 import urlopen
import json

names = ['nyt.txt']

#note: only 1 newsource is included here, as the free API does not allow for the number of calls made by all sources
#other sources: ['fox.txt', 'breitbart.txt', 'cnn.txt', 'wsj.txt']

client = textapi.Client("17fd47a3", "e04bf98926505adfbb106de51490b9ce")

def sentize(publication_name):
    with open(publication_name) as inputfile:
            data = json.load(inputfile)
    inputfile.close()

    sent_added = []

    for article in data:
            title = article['Title'].encode('ascii', 'ignore')
            print title
            sentiment = client.Sentiment({'text': title})

            piece = {'Title': article['Title'], 'PubDate': article['PubDate'], 'Sentiment': sentiment['polarity'], 'Confidence': sentiment['polarity_confidence']}
            sent_added.append(piece)


    f = open(publication_name, 'w')
    json.dump(sent_added, f)
    f.close()



for name in names:
    sentize(name)