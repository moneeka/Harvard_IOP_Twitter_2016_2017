import csv

files = ['wsj_political_count.csv', 'wsj_nonpolitical_count.csv']

def accumulate(currFile):
	index = currFile.index('_')
	frontName = currFile[:index]
	#print frontName
	backName = currFile[index+1:]
	#print backName
	lean = backName.index('_')
	#print lean
	leanName = backName[:lean]
	#print leanName
	name = frontName + '_' + leanName + '.csv'
	#print name
	#print currFile
	with open(name, 'wb') as newFile:
		writer = csv.writer(newFile, delimiter = ',')
		header = ["Positive", "Neutral", "Negative", "Date"]
		writer.writerow(header)
		with open(currFile, 'rb') as csvfile:
			count = csv.reader(csvfile, delimiter=',')
			count.next()
			for row in count:
				positiveCount = float(row[0])
				neutralCount = float(row[1])
				negativeCount = float(row[2])
				date = row[3]
				positivePercent = 0
				negativePercent = 0
				neutralPercent = 0
				total = positiveCount + negativeCount + neutralCount
				print total
				if total > 0:
					positivePercent = (positiveCount / (total))*100
					neutralPercent = (neutralCount / (total))*100
					negativePercent = (negativeCount / (total))*100
				
				row = [positivePercent, neutralPercent, negativePercent, date]
				writer.writerow(row)

for f in files:
	accumulate(f)