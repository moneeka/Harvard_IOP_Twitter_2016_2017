#!/usr/bin/env python
'''
Build a dictionary keyed by hashtag with value the number of occurences of that hashtag from a file of tweets.

Reads through a file with tweets in json format, extracting the hashtags that occur in the file, and building a
dictionary keyed by the hashtag with value the number of times the hashtag occurs in the file. The pickle of the
dictionary is written to the file specified on the command line. The total number of tweets read, along with the number
of tweets ignored because of any problem in reading, are printed on the console.

Usage: count_hashtags.py file_containiing_tweets output_file
'''
import json, sys, cPickle

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: count_hashtags.py file_with_tweets output_file'
        sys.exit(1)

    fin_name = sys.argv[1]
    fin = open(fin_name, 'r')
    count_d = {}
    bad_lines = 0
    total_lines = 0
    for l in fin:
        total_lines += 1
        try:
            lj = json.loads(l)
            l_tags = lj['entities']['hashtags']
            for t in l_tags:
                t_text = t['text']
                if t_text in count_d:
                    count_d[t_text] += 1
                else:
                    count_d[t_text] = 1
        except:
            bad_lines += 1

    s_list = sorted(count_d.items(), key = lambda(k,v):v, reverse = True)

    fout = open(sys.argv[2], 'w')
    cPickle.dump(s_list, fout)

    fin.close()
    fout.close()
    print 'Total lines processed =', total_lines
    print 'Total lines skipped =', bad_lines

