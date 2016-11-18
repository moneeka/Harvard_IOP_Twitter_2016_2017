import sys
import jsonCleaner
import TweetSent

def main(argv):

    data_file = argv[0]

    cleaned_file = 'cleaned' + data_file
    
    jsonCleaner.json_clean(data_file, cleaned_file)
    return TweetSent.tweet_sent(cleaned_file)

if __name__ == "__main__":
   main(sys.argv[1:])