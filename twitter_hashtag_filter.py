import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# consumer_key = "#"
# consumer_secret = "#"
# access_token = "#"
# access_secret = "#"

consumer_key = "WUkXAAr4Fr8fnwEWztJC4bZcA"
consumer_secret = "eT7D2y5EuKkmmYmKQWXrF8Sazc9qpHuts0fL3hfaoGcO3MpSEU"
access_token = "781660569132789760-3LR6EC39U2KGQR0ECa9m75MbI8F0t0y"
access_secret = "lrR3gMRIwjbSpHjfjfvMRMvnTcWwy0U1k6OAJWdgvQjAv"
        
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('hashtag_data_files\hashtag_filtered_tweets.json', 'a') as f:
                f.write("HINIFND")
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

data = ''
with open('hashtag_data_files\political_hashtags_for_twitter.txt', 'r') as data_file: 

    for line in data_file:
        data += ', ' + line
data_file.close()



twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=[data])