import json
import Get_bounding_boxes

def tweet_cleaner2(file, stateTweetsFile, state):
	try:
		data = []
		with open(file, 'r') as data_file:
			for line in data_file:
				data.append(json.loads(line))
		data_file.close()
		
		bounding_box = eval('[' + Get_bounding_boxes.get_bounding_box(state) + ']')
		lonmin = bounding_box[0]
		lonmax = bounding_box[1]
		latmin = bounding_box[2]
		latmax = bounding_box[3]
		
		with open(stateTweetsFile, 'w') as clean_data_file:
			for s in data:
				if s["coordinates"] != None:
					latitude = s["coordinates"]["coordinates"][1]
					longitude = s["coordinates"]["coordinates"][0]
				else:
					lat1 = s["place"]["bounding_box"]["coordinates"][0][0][0]
					lat2 = s["place"]["bounding_box"]["coordinates"][0][1][0]
					lat3 = s["place"]["bounding_box"]["coordinates"][0][2][0]
					lat4 = s["place"]["bounding_box"]["coordinates"][0][3][0]
					lon1 = s["place"]["bounding_box"]["coordinates"][0][0][1]
					lon2 = s["place"]["bounding_box"]["coordinates"][0][1][1]
					lon3 = s["place"]["bounding_box"]["coordinates"][0][2][1]
					lon4 = s["place"]["bounding_box"]["coordinates"][0][2][1]
					latitude = (lat1 + lat2 + lat3 + lat4)/4
					longitude = (lon1 + lon2 + lon3 + lon4)/4				
				if latitude > latmin and latitude < latmax:
					if longitude > lonmin and longitude < lonmax:
						clean_data_file.write(json.dumps(s))
						clean_data_file.write("\n")	
	except BaseException as e:
		print("Error on_data: %s" % str(e))
	
	def on_error(self, status):
		print(status)
		return True
