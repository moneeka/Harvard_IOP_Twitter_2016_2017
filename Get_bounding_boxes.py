import json

def get_bounding_box(state):
	data = []

	read_this= "USA_bounding_boxes.json"
	#file_in = open(read_this, 'r')  
	#all_lines= file_in.readlines()  
	#file_in.close() 
	with open(read_this, 'r') as file_in:
		for line in file_in:
			data.append(json.loads(line))
	
	bb_boundary = []
	for d in data: 
		stateBound = d["display_name"]
		#print state
		if (stateBound == state):
			bb_boundary = d["boundingbox"]
			return bb_boundary
	return [0, 0, 0, 0]
