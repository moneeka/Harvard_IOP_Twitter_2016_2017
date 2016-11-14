from aylienapiclient import textapi
from urllib2 import urlopen
import json
import time

def news_sent(data_file, output_file):
    news_files = []
    with open(data_file) as data_file:
        for line in data_file:
            if line != None:
                news_files.append(line.rstrip('\n'))
    data_file.close()

    names = news_files
    neg_words = ['kill', 'killed', 'killing', 'bomb', 'bombing', 'threat', 'threatening', 'crash', 'dead', 'death', 'die'];
    #note: only 1 newsource is included here, as the free API does not allow for the number of calls made by all sources
    #other sources: ['fox.txt', 'breitbart.txt', 'cnn.txt', 'wsj.txt']

    client = textapi.Client("ae899f48", "c1535a8c6bd267b39581c7c53d8c10d8")
    political_words = ['trump', 'clinton', 'debate', 'hillary', 'donald']

    def sentize(publication_name):
        with open(publication_name) as inputfile:
                data = json.load(inputfile)
        inputfile.close()
        txt_val = publication_name.index('.txt')
        pure_name = publication_name[:txt_val]

        sent_political = []
        sent_nonpolitical = []

        x = 0
        for article in data:
                title = article['Title'].encode('ascii', 'ignore')
                print title
                try:
                    sentiment= client.Sentiment({'text': title})
                except:
                    print("Sleeping for 60 seconds...")
                    time.sleep(60)
                    sentiment= client.Sentiment({'text': title})
                sent = sentiment['polarity']
                if any (word in article['Title'].lower() for word in neg_words):
                    sent = 'negative'
                piece = {'Title': article['Title'], 'PubDate': article['PubDate'], 'Sentiment': sent, 'Confidence': sentiment['polarity_confidence']}
                print piece['Sentiment']
                if any (word in article['Title'].lower() for word in political_words):
                    sent_political.append(piece)
                else:
                    sent_nonpolitical.append(piece)
                
                if (x == 60):
                    time.sleep(60)
                    x=0
        
        f = open(pure_name + '_political.txt', 'w')
        json.dump(sent_political, f)

        f2 = open(pure_name + '_nonpolitical.txt', 'w')
        json.dump(sent_nonpolitical, f2)

        f3 = open(output_file, 'a')
        f3.write(pure_name + '_political.txt' + '\n')

        f.close()
        f2.close()
        f3.close()

    for name in names:
        sentize(name)

