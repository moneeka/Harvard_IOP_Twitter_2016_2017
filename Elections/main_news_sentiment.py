import sys
import NewsSent_Molly
import sentiment_percentage_Monica

def main(argv):

    data_file = argv[0]
    source = argv[1]

    output_file = source + '_political_news_sentimentized_file.txt'
    
    NewsSent_Molly.news_sent(data_file, output_file)
    return sentiment_percentage_Monica.sentiment_percentage(output_file)

if __name__ == "__main__":
   main(sys.argv[1:])