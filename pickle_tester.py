import pickle

f = open('California2016-04-14.dict', 'r')   # 'r' for reading; can be omitted
mydict = pickle.load(f)         # load file content as mydict
f.close()                       

with open('rawTweetPercentages', 'w') as tweet_percentages:
    combinedDict = {}
    total_tweets = 0
    for key, value in mydict.iteritems():
        if key == 'Bernie' or key == 'Sanders':
            if 'Sanders' in combinedDict:
                combinedDict['Sanders'] += len(value)
                total_tweets += len(value)
            else:
                combinedDict['Sanders'] = len(value)
                total_tweets += len(value)
    
    for key, value in mydict.iteritems():
        if key == 'Clinton' or key == 'Hillary':
            if 'Clinton' in combinedDict:
                combinedDict['Clinton'] += len(value)
                total_tweets += len(value)
            else:
                combinedDict['Clinton'] = len(value)
                total_tweets += len(value)

    for key, value in mydict.iteritems():
        if key == 'Rubio' or key == 'Marco':
            if 'Rubio' in combinedDict:
                combinedDict['Rubio'] += len(value)
                total_tweets += len(value)
            else:
                combinedDict['Rubio'] = len(value)
                total_tweets += len(value)

    for key, value in mydict.iteritems(): 
        if key == 'Ted' or key == 'Cruz':
            if 'Cruz' in combinedDict:
                combinedDict['Cruz'] += len(value) 
                total_tweets += len(value)
            else:
                combinedDict['Cruz'] = len(value)
                total_tweets += len(value)

    for key, value in mydict.iteritems():
        if key == 'John' or key == 'Kasich':
            if 'Kasich' in combinedDict:
                combinedDict['Kasich'] += len(value)
                total_tweets += len(value)
            else:
                combinedDict['Kasich'] = len(value)
                total_tweets += len(value)

    for key, value in mydict.iteritems():
        if key == 'Donald' or key == 'Trump':
            if 'Trump' in combinedDict:
                combinedDict['Trump'] += len(value)
                total_tweets += len(value)
            else:
                combinedDict['Trump'] = len(value)
                total_tweets += len(value)

    for key, value in combinedDict.iteritems():
        tweet_percentages.write(key+': '+str(value)+' Tweet Percentage: '+str((float(value)/total_tweets)*100))
        tweet_percentages.write("\n")

    tweet_percentages.write('Total Tweetsm: ' + str(total_tweets))
    


