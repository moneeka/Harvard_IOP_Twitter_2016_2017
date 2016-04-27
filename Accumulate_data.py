import main
import os
import sys 
import json 


# Assumes date is of the format YYYYMMDD converts to YYYY-MM-DD
def format_date(date):
    return date[0:4]+"-"+date[4:6]+"-"+date[6:8]

# Get the candidate totals and put it in totals
state = sys.argv[1]
rootDir = './'+ state + "/"
totals = {}
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
    	if fname.endswith(".json"):
    		print fname
    		# The key of total should just be the date without any dashes
    		pos = fname.find("2016")
    		key = fname[pos:pos+10:1]
    		key = key.replace("-","")
        	totals[key] = main.main([state,rootDir+fname])

nice_format = [{"date":"Date","sanders":"Sanders",
                "cruz":"Cruz","clinton":"Clinton","trump":"Trump",
                "kasich":"Kasich","rubio":"Rubio"}]
for date in totals: 
	results = totals[date]
	dict_template = {"date":"","clinton":"","trump":"","cruz":"","sanders":"","kasich":"","rubio":""}
	dict_template["date"] = format_date(date)
	for candidate in results:
		count = results[candidate]
		candidate = candidate.replace(state+"_","")
		dict_template[candidate] = count
	nice_format.append(dict_template)

#nice_format = json.dumps(nice_format)
#print nice_format

with open(state+"_Results.csv",'a') as f:
    for ob in nice_format:
        line = ""
        for k in ob: 
            line = line + str(ob[k]) + ","
        f.write(line[:-1]+"\n")
f.close()
