import sys
import jsonCleaner
import TweetSent

def main(argv):

    cleaned_file = argv[0]

    # cleaned_file = 'cleaned' + data_file
    
    # jsonCleaner.json_clean(data_file, cleaned_file)
    return TweetSent.sentize(cleaned_file)

if __name__ == "__main__":
   main(sys.argv[1:])