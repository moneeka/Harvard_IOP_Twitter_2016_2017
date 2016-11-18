#get a new API key and install aylienapiclient from https://developer.aylien.com/

from aylienapiclient import textapi
from urllib2 import urlopen
import json
import simplejson
import time
import os

def tweet_sent(data_file):
    tweet_files = []
    with open(data_file) as data_file:
        for line in data_file:
            if line != None:
                tweet_files.append(line.rstrip('\n'))
    data_file.close()

    names = tweet_files


    pro_conservative_w = ['#makeamericagreatagain', '#imwithyou', '#maga', '#trump2016', '#trumptrain', '#defenddonald', '#defendthesecond', '#onenationundergod',
    '#righttobeararms', '#donttreadonme', '#prolife', '#progod', '#progun', '#gunrights', '#latinosfortrump', '#gaysfortrump', '#votetrump', '#alllivesmatter',
    '#trumpforpresident', '#buildthewall']
    pro_liberal_w = ['#berniebros', '#blacklivesmatter', '#imwithher', '#feelthebern', '#berniesanders2016']
    pro_3rd_w = ['#jillnothill','#gogreen','#voteyourconscience','#johnson2016']
    anti_conservative_w = ['#makedonalddrumpfagain','#fucktrump','#dumptrump','#nevertrump','#drumpf','#trumptrainwreck']
    anti_liberal_w = ['#libtards','#liberallogic','#nobama','#stophillary','#nohillary','#notreadyforhillary','#neverhillary','#toosavagefordemocrats'
    '#hillaryforprison2016', '#hillaryforprison', '#fuckhillary', '#neverhillary', '#hillno', '#imnotwithher', '#clintonnewsnetwork', '#hillaryforprison2016',
    '#lockherup', '#crookedhillary']

    def sentize(file_name):
        with open(file_name) as inputfile:
            data = simplejson.load(inputfile)
        inputfile.close()
        

        pro_conservative = 0
        pro_liberal = 0
        pro_3rd = 0
        anti_conservative = 0
        anti_liberal = 0
        total = 0

        for tweet in data:
            content = tweet['text'].encode('ascii', 'ignore')
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

        txt_val = file_name.index('-')
        pure_file_name = file_name[:txt_val]

        date_val_beg = file_name.index('-', txt_val) + 1
        date_val_end = file_name.index('-', date_val_beg)
        file_date = file_name[date_val_beg:date_val_end]

        pro_liberal = ((pro_liberal * 1.0) / total)*100.0
        pro_conservative = ((pro_conservative*1.0) / total)* 100.0
        anti_liberal = ((anti_liberal*1.0) / total)* 100.0
        anti_conservative = ((anti_conservative*1.0) / total)* 100.0
        pro_3rd = ((pro_3rd*1.0) / total)* 100.0

        with open(pure_file_name + '_sentiment_count.txt', 'a') as outputfile:
            output = "Pro Liberal: " + str(pro_liberal) + " Pro Conservative: " + str(pro_conservative) + " Anti Liberal: " + str(anti_liberal) + " Anti Conservative: " + str(anti_conservative) + " Pro 3rd: " + str(pro_3rd) + " Date: " + str(file_date)
            outputfile.write(output)
            outputfile.write("\n")
        outputfile.close()


    for t_file in tweet_files:
        sentize(t_file)