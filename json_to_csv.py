import json, os, csv

header_list = ["id", "tweet_string", "02-09", "02-10", "02-11", "02-12", "02-13", "02-14", "02-15", "02-16", "02-17", "02-18", "02-19", "02-20", "02-21", "02-22", "02-23", "02-24", "02-25", "02-26", "02-27", "02-28", "03-01", "03-02", "03-03", "03-04", "03-05", "03-06", "03-07", "03-08", "03-09", "03-10", "03-11", "03-12", "03-13", "03-14", "03-15", "03-16", "03-17", "03-18", "03-19", "03-20", "03-21", "03-22", "03-23", "03-24", "03-25", "03-26", "03-27", "03-28", "03-29", "03-30", "03-31", "04-01", "04-02", "04-03", "04-04", "04-05", "04-06", "04-07", "04-08", "04-09", "04-10", "04-11", "04-12", "04-13", "04-14", "04-15"]



def convert_to_csv(infile_name, outfile_name):
	data = []

	with open (infile_name, 'r') as infile:
		print ("reading json file in")
		for line in infile:
			try:
				id_string = line[1:19]
				tweet_object = json.loads(line[22:])
				data.append({"id":id_string, "tweet":tweet_object})
				print("succeed")
			except:
				print("fail")
				continue
	
	with open (outfile_name, 'w') as outfile:
		print ("writing csv file out")
		writer = csv.DictWriter(outfile, fieldnames=header_list)
		writer.writeheader()
		for retweet in data:
			try:
				placeholder_dict = {"id":retweet["id"], "tweet_string":retweet["tweet"]["Text"]}
				for date in header_list[2:]:
					if date in retweet["tweet"]:
						placeholder_dict[date] = retweet["tweet"][date]
					else:
						placeholder_dict[date] = "0"
				writer.writerow(placeholder_dict)
			except:
				continue
	


original_data_path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(original_data_path)

for n in files:
	if 'aggregated_retweets' in n:
		infile_name = n
		outfile_name = "aggregated_retweets.csv"
		convert_to_csv(infile_name, outfile_name)
