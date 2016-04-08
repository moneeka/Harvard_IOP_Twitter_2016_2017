import json

def tweet_cleaner2(coordinateFile, stateTweetsFile, state):
	try:
		data = []
		with open(coordinateFile, 'r') as data_file:
			for line in data_file:
				data.append(json.loads(line))
		data_file.close()
		
		with open(stateTweetsFile, 'w') as clean_data_file:
			for s in data:
				latitude = s["coordinates"]["coordinates"][1]
				longitude = s["coordinates"]["coordinates"][0]
				if latitude > 24.369 and latitude < 31:
					if longitude > -87 and longitude < -79:
						clean_data_file.write(json.dumps(s))
						clean_data_file.write("\n")	
	except BaseException as e:
		print("Error on_data: %s" % str(e))
	
	def on_error(self, status):
		print(status)
		return True
