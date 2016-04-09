#!/usr/bin/env python

from candidate_twt import candidate_rec as c_rec
import sys, pickle

def get_bbox(c_file):
    '''
    Open and read a configuration file, returning a list of the coordinates that are the bounding box of the config
    :param c_file: name of the flie that contains a configuration, as used by tweet.py
    :return: a list of floats, which are the coordinates of the lower-left (first 2) and upper-right (second 2) of the
        bounding box defined in the
    '''
    cin = open(c_file, 'rU')
    #skip the first 5 lines of the configuration file; they don't matter
    for i in range(0,5):
        cin.readline()
    coords = []
    for i in range(0,4):
        coords.append(float(cin.readline()))
    return coords

def check_point_in_box(in_coord, in_box):
    pass

def check_box_in_box(box1, box2):
    pass

def check_list(t_list, bbox):
    in_box = False
    out_count = 0
    for t in t_list:
        if None != t.get_coords():
            in_box = check_point_in_box(t.get_coords(), bbox)
        else:
            in_box = check_box_in_box(t.get_place_coords(), bbox)
        if not in_box:
            out_count += 1
    return out_count

def check_in_bbox(candid_d, bbox):
    for k in candid_d.iterkeys():
        t_list = candid_d[k]
        misses = check_list(t_list, bbox)
        print misses, 'tweets outside of bounding box for candidate', k

    return

if __name__ == '__main__':
    c_rec_fname = sys.argv[1]
    c_dict = pickle.load(open(c_rec_fname, 'rU'))
    config_fname = sys.argv[2]
    bbox = get_bbox(config_fname)
    check_in_bbox(c_dict, bbox)