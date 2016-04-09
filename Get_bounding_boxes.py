import json

def get_bounding_boxes():
	data = []

	read_this= "USA_bounding_boxes.txt"
	file_in = open(read_this, 'r')  
	all_lines= file_in.readlines()  
	file_in.close() 
	with open(read_this, 'r') as file_in:
	    for line in file_in:
			data.append(json.loads(line))
		
	bb_dict = {}
	for d in data: 
		state = str((d[0]["display_name"].split(","))[0])
		#print state
		for i in range(0,4):
			# Cast the coordinates from strings to floats
			d[0]["boundingbox"][i] = float(d[0]["boundingbox"][i])
		#print d[0]["boundingbox"]
		bb_dict[state] = d[0]["boundingbox"]
	print bb_dict
	return bb_dict
	