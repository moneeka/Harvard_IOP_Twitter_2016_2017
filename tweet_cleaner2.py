import json
import Get_bounding_boxes

def tweet_cleaner2(coordinateFile, stateTweetsFile, state):
	try:
		data = []
		with open(coordinateFile, 'r') as data_file:
			for line in data_file:
				data.append(json.loads(line))
		data_file.close()
		
		bounding_box = eval('[' + Get_bounding_boxes.get_bounding_box(state) + ']')
		latmin = bounding_box[0]
		latmax = bounding_box[1]
		lonmin = bounding_box[2]
		lonmax = bounding_box[3]
		
		with open(stateTweetsFile, 'w') as clean_data_file:
			for s in data:
				latitude = s["coordinates"]["coordinates"][1]
				longitude = s["coordinates"]["coordinates"][0]
				if latitude > latmin and latitude < latmax:
					if longitude > lonmin and longitude < lonmax:
						clean_data_file.write(json.dumps(s))
						clean_data_file.write("\n")	
	except BaseException as e:
		print("Error on_data: %s" % str(e))
	
	def on_error(self, status):
		print(status)
		return True
