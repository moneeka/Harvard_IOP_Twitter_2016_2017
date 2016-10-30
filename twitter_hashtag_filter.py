import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import os
from datetime import date

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

    def __init__(self, out_directory, out_fname):
        self.count = 1
        self.directory = out_directory
        self.fname = out_fname
        self.date = date.today()
        self.outname = os.path.sep.join([out_directory, out_fname])
        self.outname = self.outname + str(self.date) + '.json'
        try:
            self.outfile = open(self.outname, 'w')
        except BaseException as e:
            print 'error on file open', str(e)
            exit(1)

    def on_data(self, t_data):
        try:
            self.outfile.write("HINIFND")
            self.outfile.write(t_data)
            if self.count < 1000:
                self.count += 1
            else:
                self.count = 1
                if self.check_new_date():
                    self.use_file()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

    def use_file(self):
        self.outfile.close()
        if self.date == date.today():
            self.date = self.date + '1'
        else:
            self.date = date.today()
        self.outname = os.path.sep.join([self.directory, self.fname])
        self.outname = self.outname + str(self.date) + '.json'
        try:
            self.outfile = open(self.outname, 'w')
        except BaseException as e:
            print 'error opening new file'
            exit(1)

    def check_new_date(self):
        if self.date != date.today():
            return True
        else:
            return False

data = ''
with open('hashtag_data_files/political_hashtags_for_twitter.txt', 'r') as data_file:
    for line in data_file:
        if line != None:
            data += ', ' + line
data_file.close()



twitter_stream = Stream(auth, MyListener('hashtag_data_files', 'hashtag_filtered_tweets'))
twitter_stream.filter(track=[data])
