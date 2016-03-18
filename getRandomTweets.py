#!/usr/bin/env python
'''
Get a random set of tweets concerning a candidate from a dictionary of the sort created by findTextByName.py

'''
import candidate_twt
import sys, cPickle, random, json

def get_rand_tweets(td, cand, t_num):
    if cand not in td:
        print 'no candidate records for', candidate
        exit(1)

    t_list = td[cand]
    t_total = len(t_list)
    print cand, t_total
    for i in range(0,t_num):
        r_ind = random.randint(0, t_total)
        if type(t_list[r_ind]) == type(''):
            js = json.loads(t_list[r_ind])
            print js['text']
        else:
            print t_list[r_ind].get_text()

if __name__ == '__main__':
    fname = sys.argv[1]
    fin = open(fname, 'rU')
    t_dict = cPickle.load(fin)
    candidate = sys.argv[2]
    tweet_num = int(sys.argv[3])
    get_rand_tweets(t_dict, candidate, tweet_num)


