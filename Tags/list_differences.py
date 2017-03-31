#!/usr/bin/env python
'''
In a directory of pickles of lists of tags and counts, display the differences between the tags in two files. The
assumption is that the files contain tags from a particular date, and that the files contain the date in the name (and,
in fact, that the date can be extracted by removing the first three and the last four characters in the file name). The
most common n tags are considered, where n is determined by a command-line argument.
'''

import os, cPickle, sys


def get_date(file_name):
    '''
    Return the date extracted from the name of the file. Assumes that the date is the file name with the first three
    and last four characters removed.
    :param file_name: name of the file
    :return: date taken from the file name
    '''
    return file_name[3:-4]

def get_tag_set(file_name, number):
    '''
    Builds a set of the first number tags in a file. The file is assumed to be a pickle of an ordered list, with the
    list containing the pair <tag, count> in count order, as built by count_hashtags.py
    :param file_name: File containing the hashtags and their counts
    :param number: The number of hashtags to place in the set
    :return: a set of hashtags extracted from the file
    '''
    f_in = open(file_name, 'r')
    list_in = cPickle.load(f_in)
    f_in.close()

    ret_set = set()
    for i in range(0,number):
        ret_set.add(list_in[i][0])

    return ret_set

if __name__ == '__main__':
    num_entries = int(sys.argv[1])

    f_list = os.listdir('.')
    tag_dict = {}
    for f in f_list:
        if 'pkl' in f:
            tag_set = get_tag_set(f, num_entries)
            tag_date = get_date(f)
            tag_dict[tag_date] = tag_set

    first_key = None
    second_key = None
    for k in sorted(tag_dict):
        if first_key == None:
            first_key = k
        else:
            second_key = k
            diff_list = tag_dict[second_key] - tag_dict[first_key]
            print "tags new on", second_key, '=', ', '.join(diff_list)
            print 'tags dropped on', second_key, ', '.join(tag_dict[first_key] - tag_dict[second_key])
            print ''
            first_key = second_key
