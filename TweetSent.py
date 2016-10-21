#get a new API key and install aylienapiclient from https://developer.aylien.com/

from aylienapiclient import textapi
from urllib2 import urlopen
import json
import time

tweet_files = []

client = textapi.Client("17fd47a3", "e04bf98926505adfbb106de51490b9ce")

def sentize(tweets):
    with open(tweets) as inputfile:
        data = json.load(inputfile)
    inputfile.close()
    
    sent_political_pos = []
    sent_political_neg = []
    sent_political_neutral = []

    x = 0

    for tweet in data:
        content = tweet['text']
        sentiment = client.Sentiment({'text': content})
        
        x=x+1

        sent_tweet = {'text': tweet['text'], 'created_at': article['created_at'], 'Sentiment': sentiment['polarity'], 'Confidence': sentiment['polarity_confidence']}
        
        if(sentiment['polarity'] == 'positive'):
            sent_political_pos.append(piece)
        elif(sentiment['polarity'] == 'negative'):
            sent_political_neg.append(piece)
        else:
            sent_political_neutral.append(piece)

        if (x == 60):
            time.sleep(60)
            x=0


    f = open(tweets + '_political.txt', 'w')
    f.write("\n Positive: \n")
    json.dump(sent_political_pos, f)
    f.write("\n Negative: \n")
    json.dump(sent_political_neg, f)
    f.write("\n Neutral: \n")
    json.dump(sent_political_neutral, f)
    f.close()

for t_file in tweet_files:
    sentize(t_file)