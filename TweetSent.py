#get a new API key and install aylienapiclient from https://developer.aylien.com/

from aylienapiclient import textapi
from urllib2 import urlopen
import json
import time
import os

def sentize(file_name):

    pro_conservative_w = ['#makeamericagreatagain', '#imwithyou', '#maga', '#trump2016', '#trumptrain', '#defenddonald', '#defendthesecond', '#onenationundergod',
    '#righttobeararms', '#donttreadonme', '#prolife', '#progod', '#progun', '#gunrights', '#latinosfortrump', '#gaysfortrump', '#votetrump', '#alllivesmatter',
    '#trumpforpresident', '#buildthewall']
    pro_liberal_w = ['#berniebros', '#blacklivesmatter', '#imwithher', '#feelthebern', '#berniesanders2016']
    pro_3rd_w = ['#jillnothill','#gogreen','#voteyourconscience','#johnson2016']
    anti_conservative_w = ['#makedonalddrumpfagain','#fucktrump','#dumptrump','#nevertrump','#drumpf','#trumptrainwreck']
    anti_liberal_w = ['#libtards','#liberallogic','#nobama','#stophillary','#nohillary','#notreadyforhillary','#neverhillary','#toosavagefordemocrats'
    '#hillaryforprison2016', '#hillaryforprison', '#fuckhillary', '#neverhillary', '#hillno', '#imnotwithher', '#clintonnewsnetwork', '#hillaryforprison2016',
    '#lockherup', '#crookedhillary']

    with open('tweets_sentiment_count.csv', 'a') as outputfile:
        outputfile.write('Pro Liberal, Pro Conservative, Anti Liberal, Anti Conservative, Date\n')

    with open(file_name) as inputfile:
        data = json.load(inputfile)
    inputfile.close()
    

    pro_conservative = 0
    pro_liberal = 0
    pro_3rd = 0
    anti_conservative = 0
    anti_liberal = 0
    total = 0

    txt_val = file_name.index('_cleaned')
    pure_file_name = file_name[:txt_val]
    date_val = file_name.index('2016')
    date = pure_file_name[date_val:]
    print date

    for tweet in data:
        try:
            content = tweet['text'].encode('ascii', 'ignore')
        except:
            continue
        if any (word in content.lower() for word in pro_conservative_w):
            pro_conservative += 1
            total +=1
        if any (word in content.lower() for word in pro_liberal_w):
            pro_liberal += 1
            total +=1
        if any (word in content.lower() for word in pro_3rd_w):
            pro_3rd += 1
            total +=1
        if any (word in content.lower() for word in anti_conservative_w):
            anti_conservative += 1
            total +=1
        if any (word in content.lower() for word in anti_liberal_w):
            anti_liberal += 1
            total +=1


    pro_liberal = ((pro_liberal * 1.0) / total)*100.0
    pro_conservative = ((pro_conservative*1.0) / total)* 100.0
    anti_liberal = ((anti_liberal*1.0) / total)* 100.0
    anti_conservative = ((anti_conservative*1.0) / total)* 100.0
    pro_3rd = ((pro_3rd*1.0) / total)* 100.0
    

    with open('tweets_sentiment_count.csv', 'a') as outputfile:
        output = str(pro_liberal) + ',' + str(pro_conservative) + ',' + str(anti_liberal) + ',' + str(anti_conservative) + ',' + date
        outputfile.write(output)
        outputfile.write("\n")
    outputfile.close()