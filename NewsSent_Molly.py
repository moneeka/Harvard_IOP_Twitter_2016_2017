#get a new API key and install aylienapiclient from https://developer.aylien.com/

from aylienapiclient import textapi
from urllib2 import urlopen
import json
import time

names = ['wsj-20161015-105619.txt']
neg_words = ['kill', 'killed', 'killing', 'bomb', 'bombing', 'threat', 'threatening', 'crash', 'dead', 'death', 'die'];
#note: only 1 newsource is included here, as the free API does not allow for the number of calls made by all sources
#other sources: ['fox.txt', 'breitbart.txt', 'cnn.txt', 'wsj.txt']

client = textapi.Client("17fd47a3", "e04bf98926505adfbb106de51490b9ce")
political_words = ['trump', 'clinton', 'debate', 'hillary', 'donald']
def sentize(publication_name):
    with open(publication_name) as inputfile:
            data = json.load(inputfile)
    inputfile.close()
    txt_val = publication_name.index('.txt')
    pure_name = publication_name[:txt_val]

    sent_political_pos = []
    sent_political_neg = []
    sent_political_neutral = []
    sent_nonpolitical_pos = []
    sent_nonpolitical_neg = []
    sent_nonpolitical_neutral = []
    x = 0
    for article in data:
            title = article['Title'].encode('ascii', 'ignore')
            print title
            sentiment= client.Sentiment({'text': title})
            sent = sentiment['polarity']
            if any (word in article['Title'].lower() for word in neg_words):
                sent = 'negative'
            piece = {'Title': article['Title'], 'PubDate': article['PubDate'], 'Sentiment': sent, 'Confidence': sentiment['polarity_confidence']}
            print piece['Sentiment']
            if any (word in article['Title'].lower() for word in political_words):
                if(piece['Sentiment'] == 'positive'):
                    sent_political_pos.append(piece)
                elif(piece['Sentiment'] == 'negative'):
                    sent_political_neg.append(piece)
                else:
                    sent_political_neutral.append(piece)
            else:
                if(piece['Sentiment'] == 'positive'):
                    sent_nonpolitical_pos.append(piece)
                elif(piece['Sentiment'] == 'negative'):
                    sent_nonpolitical_neg.append(piece)
                else:
                    sent_nonpolitical_neutral.append(piece)
            if (x == 60):
                time.sleep(60)
                x=0


    f = open(pure_name + '_political.txt', 'w')
    f.write("\n Positive: \n")
    json.dump(sent_political_pos, f)
    f.write("\n Negative: \n")
    json.dump(sent_political_neg, f)
    f.write("\n Neutral: \n")
    json.dump(sent_political_neutral, f)
    f2 = open(pure_name + '_nonpolitical.txt', 'w')
    f2.write("\n Positive: \n")
    json.dump(sent_nonpolitical_pos, f2)
    f2.write("\n Negative: \n")
    json.dump(sent_nonpolitical_neg, f2)
    f2.write("\n Neutral: \n")
    json.dump(sent_nonpolitical_neutral, f2)
    f.close()
    f2.close()



for name in names:
    sentize(name)
