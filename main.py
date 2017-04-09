import sys
import deduplicate_phone_data
import twitter_phone_numbers
import retweet_aggregator
import json_to_csv

def main(argv):

	#As a first step, we merge all the twitter files from the same day and delete the duplicates. The new file name will be "mergedPhoneData_[insert date]".
	#For example, mergedPhoneData_2017_03_06.json
	deduplicate_phone_data
	twitter_phone_numbers
	retweet_aggregator
	json_to_csv


if __name__ == "__main__":
   main(sys.argv[1:])