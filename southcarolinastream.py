import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 
consumer_secret =
access_token =
access_secret =

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('southcarolina.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#Hillary'])
#twitter_stream.filter(track=['#HillaryClinton'])
#twitter_stream.filter(locations=[-122.75,36.8,-121.75,37.8]).filter(track=['#Hillary'])
twitter_stream.filter(locations=[-83.3540, 32.0333, -78.4992, 35.2155])
