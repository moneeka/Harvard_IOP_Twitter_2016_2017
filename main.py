import sys
import tweet_divider
import tweet_cleaner
import sort

def main(argv):

	state = argv[0]
	dataFile = argv[1]
	
	stateFile = state + "_tweets.json"
	
	tweet_divider.tweet_divider(dataFile, 'coordinatePartition.json', 'placePartion.json')
	tweet_cleaner.tweet_cleaner('coordinatePartition.json', stateFile, state)
	sort.sort(stateFile, 'dictionary.json')

if __name__ == "__main__":
   main(sys.argv[1:])