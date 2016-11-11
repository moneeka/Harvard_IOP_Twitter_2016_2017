from urllib2 import urlopen
import json

def sentiment_percentage(political_news_sentimentized_file):
    news_data = []
    with open(political_news_sentimentized_file) as data_file:
        for line in data_file:
            if line != None:
                news_data.append(line.rstrip('\n'))
    data_file.close()

    file_names = news_data

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

        date_val_beg = file_name.index('-', txt_val) + 1
        date_val_end = file_name.index('-', date_val_beg)
        file_date = file_name[date_val_beg:date_val_end]

        with open(pure_file_name + '_sentiment_count.txt', 'a') as outputfile:
            output = "Positive Count: " + str(pos) + " Neutral Count: " + str(neutral) + " Negative Count: " + str(neg) + " Date: " + str(file_date)
            outputfile.write(output)
            outputfile.write("\n")
        outputfile.close()

    for name in file_names:
        count_sentiment(name)
