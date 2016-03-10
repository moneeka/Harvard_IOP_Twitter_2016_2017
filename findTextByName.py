#!/usr/bin/env python

import json
import sys, pickle

candidate_list = ['Hillary',
                  'Clinton',
                  'Bernie',
                  'Sanders',
                  'Donald',
                  'Trump',
                  'Marco',
                  'Rubio',
                  'Cruz',
                  'Kasich']

candidate_dict = {}

def add_candidate_text(candidate, raw_line):
    text = json.loads(raw_line)['text']
    if candidate in candidate_dict:
        candidate_dict[candidate].append(text)
    else:
        candidate_dict[candidate] = [text]


def check_candidate(l):
    i = 0;
    while i < len(candidate_list):
        if candidate_list[i] in l:
            add_candidate_text(candidate_list[i], l)
            if (i == 0) or (i == 2) or (i == 4) or (i == 6):
                i += 1
        i += 1

def main(fin, fout):
    for l in fin:
        check_candidate(l)
    pickle.dump(candidate_dict, fout)
    fout.close()
    fin.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: findTextByName tweetFile dictionary'
        print 'where tweetFile is the name of a json file of tweets'
        print 'and dictionary is the name of the dictionary file to be produced'
        exit(1)

    fname = sys.argv[1]
    try:
        fin = open(fname, 'rU')
    except:
        print 'file with', fname, 'not found'
        exit(1)

    fout = open(sys.argv[2], 'w')

    main(fin, fout)
