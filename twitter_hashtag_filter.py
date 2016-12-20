import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import os
from datetime import date



def load_dict(auth_d, l):
    '''
    Load the contents of a line into a dictionary, using the first word of the
    line as the key and the rest of the line as the value.
    :param auth_d: The dictionary to be populated
    :param l: The line that contains the key and the value, both as strings
    :return: None
    '''
    s = l.find(' ')
    k = l[ :s]
    v = l[s+1:]
    auth_d[k] = v

def make_auth(from_file):
    '''
    Create a tweepy auth object. This will use the contents of the file that has been handed in as the
    access token and comsumer keys. The assumption is that the first four lines of the file contain the
    name of the auth parameter followed by a space followed by the value of the parameter.
    :param from_file: Name of the file containing the authentication information
    :return: A tweepy auth object
    '''
    fin = open(from_file, 'r')
    auth_dict = {}
    for i in range(0,4):
        l = fin.readline()
        load_dict(auth_dict, l[:-1])

    auth = OAuthHandler(auth_dict['consumer_key'], auth_dict['consumer_secret'])
    auth.set_access_token(auth_dict['access_token'], auth_dict['access_secret'])
    fin.close()

    return auth


class MyListener(StreamListener):

    def __init__(self, out_directory, out_fname):
        self.count = 1
        self.directory = out_directory
        self.fname = out_fname
        self.date = date.today()
        self.outname = os.path.sep.join([out_directory, out_fname])
        self.outname = self.outname + str(self.date) + '.json'
        try:
            self.outfile = open(self.outname, 'a')
        except BaseException as e:
            print 'error on file open', str(e)
            exit(1)

    def on_data(self, t_data):
        try:
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
        if self.date != date.today():
            self.date = date.today()
        self.outname = os.path.sep.join([self.directory, self.fname])
        self.outname = self.outname + str(self.date) + '.json'
        try:
            self.outfile = open(self.outname, 'a')
        except BaseException as e:
            print 'error opening new file'
            exit(1)

    def check_new_date(self):
        if self.date != date.today():
            return True
        else:
            return False


auth = make_auth('authenticationKeys.txt')
api = tweepy.API(auth)

data = ''
with open('hashtag_data_files/political_hashtags_for_twitter.txt', 'r') as data_file:
    for line in data_file:
        if line != None:
            data += ', ' + line
data_file.close()



twitter_stream = Stream(auth, MyListener('hashtag_data_files', 'hashtag_filtered_tweets'))
twitter_stream.filter(track=[data])
