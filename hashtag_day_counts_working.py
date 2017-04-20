import cPickle, os, operator

hashtag_date_counts = {}

data_path = os.path.dirname(os.path.abspath(__file__)) + "/TagCounts"
data_files = os.listdir(data_path)

for doc_name in data_files:
	doc = open("TagCounts/"+doc_name, 'r')
	l = cPickle.load(doc)
	date = doc_name.split('tag')[1].split('.pkl')[0]
	for line in l:
		hashtag = line[0].lower()

		if hashtag in hashtag_date_counts:
			if date in hashtag_date_counts[hashtag]:
				hashtag_date_counts[hashtag][date] += line[1]
			else:
				hashtag_date_counts[hashtag][date] = line[1]
		else:
			hashtag_date_counts[hashtag] = {}
			hashtag_date_counts[hashtag][date] = line[1]
	doc.close()

#print hashtag_date_counts

print hashtag_date_counts["trump"]
for k,v in hashtag_date_counts.items():
	print k,v
