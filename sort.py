import json

#creating the dictionary
candidate_dict = {}

#testbatch3.json will be replaced by whatever file we are using

jsonData = json.loads(open('testbatch3.json').read())

for item in jsonData:
	#print item.has_key("content")

	content = item['content']
	address = item['address']
	#retrieving the index of the first comma in the address (ex: 11111 Euclid Ave, Cleveland, OH)
	index = address.index(',')
	#taking the substring of the address to isolate the town
	town = address[(index+2):]
	index2 = town.index(',')
	town = town[:index2]
	#now, the town should be completely isolated
		
	if 'sanders' in content:
		key = '_'.join([town, 'sanders'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
	if 'clinton' in content:
		key = '_'.join([town, 'clinton'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
	if 'trump' in content:
		key = '_'.join([town, 'trump'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
	if 'cruz' in content:
		key = '_'.join([town, 'cruz'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
print candidate_dict