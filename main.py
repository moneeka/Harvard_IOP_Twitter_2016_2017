import sys
import tweet_divider
import tweet_cleaner2
import sort

def main(argv):

	state = argv[0]
	dataFile = argv[1]

	dateIndex = dataFile.find("2016")
	date = dataFile[dateIndex:]

	stateFile = "tweets_" + state + "_" + date
	coordinateFile = "coordinatePartition_" + state + "_" + date
	dictionaryFile = "dictionary_" + state + "_" + date

	tweet_divider.tweet_divider(dataFile, coordinateFile, 'placePartition.json')
	#eliminate non-political tweets
	tweet_cleaner2.tweet_cleaner2(coordinateFile, stateFile, state)
	return sort.sort(coordinateFile, dictionaryFile, state)


if __name__ == "__main__":
   main(sys.argv[1:])
