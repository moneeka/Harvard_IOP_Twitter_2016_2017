import json

class Tweet:
	json = {}
	def __init__(self, candidate, state_town, content, coordinates, created_at):
		self.candidate = candidate
		self.state_town = state_town
		self.content = content
		self.coordinates = coordinates
		self.create_at = created_at
		

def sort(dataFile, outputFile):

		#testbatch3.json will be replaced by whatever file we are using

	candidate_dict = {}
	data = []
	output_array = []
	with open(dataFile) as f:
		for line in f:
			data.append(json.loads(line))

	for item in data:
		content = item['text']
		address = item['address']
		coordinates = item['geo']['coordinates']
		created_at = item['created_at']
		#retrieving the index of the first comma in the address (ex: 11111 Euclid Ave, Cleveland, OH)
		'''index = address.index(',')
		#taking the substring of the address to isolate the town
		town = address[(index+2):]
		#retrieving index of the second comma
		index2 = town.index(',')
		town = town[(index2+2):]
		town_clip = town
		index3 = town_clip.index(',')
		town_clip = town_clip[(index3+2):]
		index4 = town_clip.index(',')
		state_town = town[:(index3+index4)]
		#retrieving index of the third comma
		#now, the town should be completely isolated'''
		state_town = "Nevada"
		candidate = " "
		candidate_mention = False

		if 'sanders' in content or 'bernie' in content or 'bern' in content:
			key = '_'.join([state_town, 'sanders'])
			if candidate_dict.has_key(key):
				candidate_dict[key] += 1
			else:
				candidate_dict[key] = 1
			candidate = "sanders"
			candidate_mention = True
		if 'clinton' in content or 'hillary' in content:
			key = '_'.join([state_town, 'clinton'])
			if candidate_dict.has_key(key):
				candidate_dict[key] += 1
			else:
				candidate_dict[key] = 1
			candidate = "clinton"
			candidate_mention = True
		if 'trump' in content or 'donald' in content or 'apprentice' in content:
			key = '_'.join([state_town, 'trump'])
			if candidate_dict.has_key(key):
				candidate_dict[key] += 1
			else:
				candidate_dict[key] = 1
			candidate = "trump"
			candidate_mention = True
		if 'cruz' in content or ' ted' in content:
			key = '_'.join([state_town, 'cruz'])
			if candidate_dict.has_key(key):
				candidate_dict[key] += 1
			else:
				candidate_dict[key] = 1
			candidate = "cruz"
			candidate_mention = True
		if candidate_mention == True:
			tweet = Tweet(candidate, state_town, content, coordinates, created_at)
			output_array.append(json.dumps(tweet.__dict__))

	print candidate_dict


	# put dictionary in a json file
	with open(outputFile, 'w') as dictionary:
		for item in output_array:
			dictionary.write("%s\n" % item)
		dictionary.close()
