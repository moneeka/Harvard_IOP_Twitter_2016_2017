#!/usr/bin/env python
'''
Build a word cloud from a list of hashtags and counts found in a pickle file.

Creates a word-cloud from a file containing hashtags and counts for that hashtag. The command line can specify an offset
(i.e., the number of most-common terms to skip) and the number of terms that should be in the cloud. The offset and the
number of entries to display in the cloud must be string representations of integers.

Usage: python tag_cloud.py tag_file {offset number_to_display}
'''

import sys, cPickle
import bar_chart_counts as bcc
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def draw_cloud(f_name, word_list):
    '''
    Draws a wordcloud, labelled withthe name passed in, from the word list passed in.
    :param f_name: Name to use as a title for the wordcloud
    :param word_list: list of names and counts used to create the wordcloud
    :return: None
    '''
    wc = WordCloud(width=600, height=300, max_words=len(word_list))
    tag_c = wc.generate_from_frequencies(tag_list)
    plt.imshow(tag_c)
    plt.axis('off')
    plt.title(f_name)
    plt.show()

def get_tag_list(fname, offset, tag_num):
    '''
    Creates a list of tags and counts from a file containing a pickle of such a list. The returned list will start
    at the index specified by the offset, and will have the number of entries specified by tag_num.
    :param fname:  the file containing the pickle of a list of word, number_of_occurrences to use in building the
        wordcloud
    :param offset: Number of entries in the wordcloud to skip (this will eliminate the most-frequent terms)
    :param tag_num: The number of entries to include in the wordcloud
    :return:
    '''
    f_in = open(fname, 'r')
    full_list = cPickle.load(f_in)
    f_in.close()
    return full_list[offset:offset+tag_num]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: pthon tag_cloud.py tag_file {offset number_to_display'
        exit(1)

    fname = sys.argv[1]

    offset = bcc.get_offset()
    tag_num = bcc.get_number()

    tag_list = get_tag_list(fname, offset, tag_num)
    draw_cloud(fname, tag_list)