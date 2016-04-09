#!/usr/bin/env python
'''
Takes a .json file produced by twitter.py and builds a dictionary, keyed by candidate name, with value a list of either
    1) the tweets that contain the candidate's name, or
    2) a candidate_twt.candidate_rec object, which contains a distillation of the tweet (currently the
        text, the coordinates of the tweet, and the place associate with the tweet.
The resulting dictionary is then pickled and saved to a file with a name specified by the command line. Which of the
two options above is followed is determined by an optional 3rd argument; if it is "o", then the second option is followed,
otherwise the full tweets are stored.

Usage: python findTextByName.py Tweets.json dictonaryOutFile {o}
'''
import candidate_twt
import sys, cPickle
'''
The list of candidate names that we are searching for
'''
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

def add_candidate_rec(candidate, raw_line):
    '''
    Create a candidate_rec object from the raw twitter line. If there is an entry in the dictionary for the candidate,
    append this object to the list of objects that is the value. If there is no such entry, create one with value the
    singleton list of this candidate_rec
    :param candidate: The name of the candidate contained in the tweet
    :param raw_line: The raw json line for the candidate
    :return: None
    '''
    cand_twt = candidate_twt.candidate_rec(raw_line)
    if candidate in candidate_dict:
        candidate_dict[candidate].append(cand_twt)
    else:
        candidate_dict[candidate] = [cand_twt]

def add_candidate_twt(candidate, raw_line):
    '''
    If there is an entry in the dictionary for the candidate, append this tweet to the list of tweets that is the
    value. If there is no such entry, create one with value the  singleton list of this tweet.
    :param candidate: The name of the candidate contained in the tweet
    :param raw_line: The raw json line for the candidate
    :return: None
    '''
    if candidate in candidate_dict:
        candidate_dict[candidate].append(raw_line)
    else:
        candidate_dict[candidate] = [raw_line]

'''
The function that will be used to build the list that is the value of each entry in the dictionary. This is placed here
because of the nature of python, even though this is not the right place to have such a function definition.
'''
list_rec_func = add_candidate_twt

def check_candidate(l):
    '''
    See if a candidate's name is mentioned in a tweet. If it is, add either the tweet or an object to the list that is
    indexed by the candidate's name in the dictionary. The only (partially) clever thing is that candidates who are
    often referred to by their first names (Hillary, Bernie, Donald) will not be counted twice; if they are put in to
    one of the lists they won't be put into the list with their other name
    :param l: The line of the tweet file to be examined
    :return: None
    '''
    i = 0;
    while i < len(candidate_list):
        if candidate_list[i] in l:
            list_rec_func(candidate_list[i], l)
            if (i == 0) or (i == 2) or (i == 4) or (i == 6):
                i += 1
        i += 1

def main(fin, fout):
    '''
    Read through the file containing the .json records of the tweets. Call check_candidates for each line, and then
    write the pickled candidate dictionary.
    :param fin: File containing the .json records of all tweets we collected
    :param fout: Ouput file that will contain the dictionary
    :return: None
    '''
    for l in fin:
        check_candidate(l)
    cPickle.dump(candidate_dict, fout)
    fout.close()
    fin.close()
    for k in candidate_dict.iterkeys():
        print k, len(candidate_dict[k])

if __name__ == '__main__':
    '''
    Get the name of the input file of tweets (in .json format) and the name of the output file. If a third argument is
    supplied and it's value is 'o', create a list of candidate_rec objects rather than a list of the full tweet
    '''
    if len(sys.argv) < 3:
        print 'Usage: findTextByName tweetFile dictionary {o}'
        print 'where tweetFile is the name of a json file of tweets'
        print 'and dictionary is the name of the dictionary file to be produced'
        print 'if o is included as the last argument, then the dictionary will be of candidate_rec objects'
        exit(1)

    fname = sys.argv[1]
    try:
        fin = open(fname, 'rU')
    except:
        print 'file with', fname, 'not found'
        exit(1)

    fout = open(sys.argv[2], 'w')
    if len(sys.argv) > 3:
        if 'o' == sys.argv[3]:
            list_rec_func = add_candidate_rec

    main(fin, fout)