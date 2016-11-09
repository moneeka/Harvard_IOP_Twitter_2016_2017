from urllib2 import urlopen
import json
import time

file_names = ['nyt-20161017-054836_political.txt', 'wsj-20161101-025813_political.txt', 'nyt-20161023-131346_political.txt']

def count_sentiment(file_name):
    with open(file_name) as inputfile:
        data = json.load(inputfile)
    inputfile.close()

    pos = 0
    neg = 0
    neutral = 0

    for article in data:
        if article['Sentiment'] == 'neutral':
            neutral += 1
        elif article['Sentiment'] == 'negative':
            neg += 1
        else:
            pos += 1
    
    txt_val = file_name.index('-')
    pure_file_name = file_name[:txt_val]

    with open(pure_file_name + '_sentiment_count.txt', 'a') as outputfile:
        output = "Positive Count: " + str(pos) + " Neutral Count: " + str(neutral) + " Negative Count: " + str(neg)
        outputfile.write(output)
        outputfile.write("\n")
    outputfile.close()

for name in file_names:
    count_sentiment(name)
