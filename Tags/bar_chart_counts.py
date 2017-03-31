#!/usr/bin/env python
'''
Display a virtical bar chart of frequencies of tags stored in a [tag,occurrence] list pickled in the named file.

The display shows most common to least common from top to bottom. An offset (number of entries to skip) can be specified,
as well as the number of entries to show. The default is to show starting with the most common and to show 50 entries.
The hashtag will be diaplayed as the virtical tick bar; this may be hard to red without expanding the default size of
the chart.

Usage: python bar_chart_count.py tag_file.pkl {offset number_to_display}
'''

import numpy as np
import matplotlib.pyplot as plt
import sys, cPickle

def get_offset():
    if len(sys.argv) > 2:
        return int(sys.argv[2])
    else:
        return 0

def get_number():
    if len(sys.argv) > 3:
        return int(sys.argv[3])
    else:
        return 50

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage python bar_chart_count.py tag_file.pkl {offset number_to_display}'
        exit(1)

    fin = open(sys.argv[1], 'r')
    tag_list = cPickle.load(fin)
    fin.close()

    offset = get_offset()
    number_to_chart = get_number()

    tag_vals = []
    tic_vals = []
    for i in range(0, number_to_chart):
        tag_vals.append(tag_list[i + offset][1])
        tic_vals.append(tag_list[i + offset][0])

    tag_vals.reverse()
    tic_vals.reverse()
    ind = np.arange(len(tag_vals))
    width = 0.25
    p1 = plt.barh(ind, tag_vals, width)
    plt.yticks(ind, tic_vals)
    plt.title(sys.argv[1])
    plt.show()
