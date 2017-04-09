import json, datetime, unicodedata, os

def tweet_cleaner(infile, outfile):
    data = []
    with open(infile, 'r') as data_file:
        for line in data_file:
            # converts each line into a json object
            try:
                data.append(json.loads(line))
            except:
                continue
    data_file.close()
    out =  []
    for d in data:
        try:
            obj = {}
            obj['created_at'] = str(d['created_at'])
            t = unicodedata.normalize('NFKD', d['text']).encode('ascii','replace')
            obj['text'] = t
            obj['in_reply_to_user_id_str'] = str(d['in_reply_to_user_id_str'])
            obj['in_reply_to_screen_name'] = str(d['in_reply_to_screen_name'])
            if d['coordinates'] != None:
                obj['coordinates'] = str(d['coordinates']['coordinates'][1]) + ',' + str(d['coordinates']['coordinates'][0])
            else:
                obj['coordinates'] = None
            obj['geo'] = d['geo']
            obj['place'] = d['place']
            obj['retweeted'] = d['retweeted']
            obj['favorited'] = d['favorited']
            obj['tweet_id'] = d['id']
            # user subdict
            user_subobj = {}
            user_subobj['verified'] = d['user']['verified']
            user_subobj['friends_count'] = d['user']['friends_count']
            user_subobj['screen_name'] = str(d['user']['screen_name'])
            user_subobj['user_id'] = d['user']['id']
            user_subobj['followers_count'] = d['user']['followers_count']
            user_subobj['favourites_count'] = d['user']['favourites_count']
            user_subobj['statuses_count'] = d['user']['statuses_count']
            user_subobj['time_zone'] = d['user']['time_zone']
            if (d['user']['location'] == None):
                user_subobj['location'] = 'None'
            else:
                user_subobj['location'] = unicodedata.normalize('NFKD', d['user']['location']).encode('ascii','replace')
            #retweeted_status subdict
            retweet_subobj = {}
            if 'retweeted_status' in d:
                retweet_subobj['created_at'] = d['retweeted_status']['created_at']
                retweet_subobj['tweet_id'] = d['retweeted_status']['id']
                retweet_subobj['text'] = d['retweeted_status']['text']
                retweet_subobj['in_reply_to_user_id_str'] = d['retweeted_status']['in_reply_to_user_id_str']
                retweet_subobj['in_reply_to_screen_name'] = d['retweeted_status']['in_reply_to_screen_name']
                retweet_subobj['geo'] = d['retweeted_status']['geo']
                retweet_subobj['place'] = d['retweeted_status']['place']
                if d['retweeted_status']['coordinates'] != None:
                    retweet_subobj['coordinates'] = str(d['retweeted_status']['coordinates']['coordinates'][1]) + ',' + str(d['retweeted_status']['coordinates']['coordinates'][0])
                else:
                    retweet_subobj['coordinates'] = None
                retweet_subobj['retweet_count'] = d['retweeted_status']['retweet_count']
                retweet_user_subobj = {}
                retweet_user_subobj['verified'] = d['retweeted_status']['user']['verified']
                retweet_user_subobj['screen_name'] = d['retweeted_status']['user']['screen_name']
                retweet_user_subobj['user_id'] = d['retweeted_status']['user']['id']
                retweet_user_subobj['location'] = d['retweeted_status']['user']['location']
                retweet_user_subobj['friends_count'] = d['retweeted_status']['user']['friends_count']
                retweet_user_subobj['followers_count'] = d['retweeted_status']['user']['followers_count']
                retweet_user_subobj['favourites_count'] = d['retweeted_status']['user']['favourites_count']
                retweet_user_subobj['statuses_count'] = d['retweeted_status']['user']['statuses_count']
                retweet_subobj['user'] = retweet_user_subobj
            obj['user'] = user_subobj
            obj['retweeted_status'] = retweet_subobj
            out.append(obj)
        except:
            continue
    with open(outfile, 'w') as outfile:
        for o in out:
            outfile.write('{}\n'.format(json.dumps(o)))

# works through the directory and creates a separate file of cleaned data for each day
original_data_path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(original_data_path)

# Assume that original data files contain the phrase 'merged_phone_data'
for n in files:
    if 'phoneTweets20' in n: 
        # separate out the parts of the name
        date_string = n[16:-5]
        print "Cleaning file: " + date_string
        outfile_name = "clean_phone_data_" + date_string + ".json"
        merged_name = "merged_phone_data_2017-" + date_string + ".json"
        if not outfile_name in files:
            if merged_name in files:
                    tweet_cleaner(merged_name, outfile_name)
            else:
                tweet_cleaner(n, outfile_name)