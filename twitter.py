#!/usr/bin/env python

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from datetime import date
import sys


class TweetConfig(object):
    def __init__(self, config_fname):
        """
        Initialize the configuration object, reading the values from a file. The file should contain, on separate lines,
        the consumer_key and consumer_secret used to register with twitter, the access_token and access_secret used
        to register with twitter, the name of the state that is being observed (which will be used to generate the
        file names for the state), and four coordinates for the bounding box around the state. Note that if there is
        an error in reading the configuration file, the program will print a simple error message and exit.

        :param config_fname: the name of the file containing the configuration information.
        :return: An initialized configuration object
        """
        try:
            with open (config_fname, 'rU') as c:
                self.a_key = c.readline()[:-1]
                self.a_secret = c.readline()[:-1]
                self.c_token = c.readline()[:-1]
                self.c_secret = c.readline()[:-1]
                self.state_name = c.readline()[:-1]
                self.auth = OAuthHandler(self.a_key, self.a_secret)
                self.auth.set_access_token(self.c_token, self.c_secret)
                self.api = tweepy.API(self.auth)
                self.loc = []
                for i in range(0,4):
                    self.loc.append(float(c.readline()))
        except BaseException as e:
            print 'Unable to read configuration file', config_fname
            print 'Exiting because of exception', str(e)
            exit(1)



class MyListener(StreamListener):
    """
    The listener object for the stream. This is meant to listen until interrupted; it will change file names when a new
    day occurs, although it only checks every 1000 tweets. This is a number that was picked arbitrarily; it may need
    to be adjusted.
    """

    def __init__(self, tc):
        """
        Initialize the stream, using a configuration object.
        :param tc: a configuration object, created from a configuration file
        :return: An initialized listener object
        """

        StreamListener.__init__(self, tc.api)

        self.line_count = 0
        self.date = date.today()
        self.config = tc
        fname = tc.state_name + str(self.date) + '.json'
        try:
            self.wout = open(fname, 'w')
        except BaseException as e:
            print 'error on file open', str(e)
            exit(1)


    def on_data(self, data):
        """
        Listener for the twitter data. The data will be written to a file. Every 1k tweets, the listener checks to
        see if the date has change; if it has, it closes the current file, opens a new one named for the state
        obtained from the configuration file with the current date appended, and starts writing to that file.
        :param data: The tweet that has been received
        :return: True
        """
        try:
            self.wout.write(data)
            if self.line_count < 1000:
                self.line_count += 1
            else:
                self.line_count = 1
                if self.check_new_date():
                    self.use_file()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        """
        Error listener; activated when an error is returned from the stream. Simply prints the error to the console
        and continues
        :param status: The error returned from the stream
        :return: True
        """
        print(status)
        return True

    def use_file(self):
        """
        Constructs the name of the file where the tweet will be written, using the state name found in the configuration.
        The current file being written is closed, and a file with the new name is then opened for writing and returned.
        :param tc: A configuration object
        :return: an open file handle where the tweets are to be written
        """
        self.wout.close()
        self.date = date.today()
        f_name = self.config.state_name + str(self.date) + '.json'
        self.wout = open(f_name, 'w')

    def check_new_date(self):
        """
        Checks to see if the current date is different from the date used to name the current file. If it is different,
        return True, as that indicates that it is time to close the file currently being used to write the tweets and
        open a new one. Otherwise, return False
        :return: True if the current date is different from the stored date, and False otherwise
        """
        if self.date != date.today():
            return True
        else:
            return False

def main (config_file):
    """
    The main routine of the program; creates a configuration object from the named file handed in as a parameter,
    creates a stream listener object using that configuration object, uses that object to create a twitter stream, and
    then does a filtered listen on that stream using the coordinates in the configuration object.
    :param config_file: Name of the file used to create the configuration object.
    :return: None
    """
    tc = TweetConfig(config_file)
    ml = MyListener(tc)
    twitter_stream = Stream(tc.auth, ml)
    twitter_stream.filter(locations=tc.loc)


if __name__ == '__main__':
    """
    The driver; get the name of the configuration file from the command line, and call the main routine with that
    named file.
    """

    config_name = sys.argv[1]
    main(config_name)

