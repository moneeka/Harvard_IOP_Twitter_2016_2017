import json

class tweet_divider():
	try:
		data = []
		with open('nevada.json') as data_file: 

			for line in data_file:
				data.append(json.loads(line))
		data_file.close()

		with open('partition1.json', 'w') as partition1_file:
			with open('partition2.json', 'w') as partition2_file:

				for s in data:
					if s["coordinates"] != None:
	
						partition1_file.write(json.dumps(s))
						partition1_file.write("\n")
					else:
						partition2_file.write(json.dumps(s))
						partition2_file.write("\n")
			partition2_file.close()
		partition1_file.close()

	except BaseException as e:
		print("Error on_data: %s" % str(e))

	def on_error(self, status):
		print(status)
		return True