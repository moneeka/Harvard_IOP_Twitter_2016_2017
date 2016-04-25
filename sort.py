import json

class Tweet:
	json = {}
	def __init__(self, candidate, state_town, content, coordinates, created_at):
		self.candidate = candidate
		self.state_town = state_town
		self.content = content
		self.coordinates = coordinates
		self.create_at = created_at


def sort(dataFile, outputFile, state, isCoord):

		#testbatch3.json will be replaced by whatever file we are using
	total_count = 0
	total_dem_count = 0
	total_repub_count = 0

	candidate_dict = {state+"_sanders":0, state+"_clinton": 0, state+"_trump": 0, state+"_cruz": 0, state+"_rubio": 0, state+"_kasich": 0}
	data = []
	output_array = []
	with open(dataFile) as f:
		for line in f:
			data.append(json.loads(line))

	for item in data:
		content = item['text']
		if isCoord:
			coordinates = item['coordinates']['coordinates']
		else:
			lat1 = item["place"]["bounding_box"]["coordinates"][0][0][0]
			lat2 = item["place"]["bounding_box"]["coordinates"][0][1][0]
			lat3 = item["place"]["bounding_box"]["coordinates"][0][2][0]
			lat4 = item["place"]["bounding_box"]["coordinates"][0][3][0]
			lon1 = item["place"]["bounding_box"]["coordinates"][0][0][1]
			lon2 = item["place"]["bounding_box"]["coordinates"][0][1][1]
			lon3 = item["place"]["bounding_box"]["coordinates"][0][2][1]
			lon4 = item["place"]["bounding_box"]["coordinates"][0][2][1]
			latitude = (lat1 + lat2 + lat3 + lat4)/4
			longitude = (lon1 + lon2 + lon3 + lon4)/4
			coordinates = [latitude, longitude]
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
		state_town = state
		candidate = " "
		candidate_mention = False

		sanders_key = '_'.join([state_town, 'sanders'])
		clinton_key = '_'.join([state_town, 'clinton'])
		trump_key = '_'.join([state_town, 'trump'])
		cruz_key = '_'.join([state_town, 'cruz'])
		rubio_key = '_'.join([state_town, 'rubio'])
		kasich_key = '_'.join([state_town, 'kasich'])

		if 'sanders' in content.lower() or 'bernie' in content.lower() or 'bern' in content.lower():
			if candidate_dict.has_key(sanders_key):
				candidate_dict[sanders_key] += 1
			else:
				candidate_dict[sanders_key] = 1
			candidate = "sanders"
			total_count = total_count + 1
			total_dem_count += 1
			candidate_mention = True
		if 'clinton' in content.lower() or 'hillary' in content.lower():
			if candidate_dict.has_key(clinton_key):
				candidate_dict[clinton_key] += 1
			else:
				candidate_dict[clinton_key] = 1
			candidate = "clinton"
			total_count = total_count + 1
			total_dem_count += 1
			candidate_mention = True
		if 'trump' in content.lower() or 'donald' in content.lower() or 'apprentice' in content.lower():
			if candidate_dict.has_key(trump_key):
				candidate_dict[trump_key] += 1
			else:
				candidate_dict[trump_key] = 1
			candidate = "trump"
			total_count = total_count + 1
			total_repub_count += 1
			candidate_mention = True
		if 'cruz' in content.lower() or 'ted' in content.lower():
			if candidate_dict.has_key(cruz_key):
				candidate_dict[cruz_key] += 1
			else:
				candidate_dict[cruz_key] = 1
			candidate = "cruz"
			total_count = total_count + 1
			total_repub_count += 1
			candidate_mention = True
		if 'rubio' in content.lower() or 'marco' in content.lower():
			if candidate_dict.has_key(rubio_key):
				candidate_dict[rubio_key] += 1
			else:
				candidate_dict[rubio_key] = 1
			candidate = "rubio"
			total_count = total_count + 1
			total_repub_count += 1
			candidate_mention = True
		if 'kasich' in content.lower() or 'john' in content.lower():
			if candidate_dict.has_key(kasich_key):
				candidate_dict[kasich_key] += 1
			else:
				candidate_dict[kasich_key] = 1
			candidate = "kasich"
			total_count = total_count + 1
			total_repub_count += 1
			candidate_mention = True

		if candidate_mention == True:
			tweet = Tweet(candidate, state_town, content, coordinates, created_at)
			output_array.append(json.dumps(tweet.__dict__))

	print candidate_dict
	candidate_dict[sanders_key] = (candidate_dict[sanders_key]/float(total_dem_count))*100
	candidate_dict[clinton_key] = (candidate_dict[clinton_key]/float(total_dem_count))*100
	candidate_dict[cruz_key] = (candidate_dict[cruz_key]/float(total_repub_count))*100
	candidate_dict[trump_key] = (candidate_dict[trump_key]/float(total_repub_count))*100
	candidate_dict[rubio_key] = (candidate_dict[rubio_key]/float(total_repub_count))*100
	candidate_dict[kasich_key] = (candidate_dict[kasich_key]/float(total_repub_count))*100
	print candidate_dict

	# put dictionary in a json file
	with open(outputFile, 'w') as dictionary:
		for item in output_array:
			dictionary.write("%s\n" % item)
		dictionary.close()

	return candidate_dict
