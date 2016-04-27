import json

def tweet_divider(dataFile, politicalFile):
	try:
		# Creates the list that will contain the objects contained in the json file 
		data = []
		political_words = ["trump", "cruz", "donald", "bernie", "sanders", "bern", "hillary", "clinton", "kasich"]

		with open(dataFile) as data_file: 

			for line in data_file:
				# converts each line into a json object
				data.append(json.loads(line))
		data_file.close()

		# Opens up the empty file that will store the tweets with actual coordinates
		with open(politicalFile, 'w') as partition1_file:
		# Opens up the empty file that will store the tweets with place and null coordinates
			for s in data:
				# Checks to see if the coordinates field is filled in
					# Writes the json version of tweet into the appropriate file
				contains_politics = False
				content = s['text']
				for word in political_words:
					if word in content.lower():
						partition1_file.write(json.dumps(s))
						partition1_file.write("\n")
		partition1_file.close()

	except BaseException as e:
		print("Error on_data: %s" % str(e))

	def on_error(self, status):
		print(status)
		return True
