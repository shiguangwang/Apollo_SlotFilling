#!/usr/bin/env python2.7

import json
from pprint import pprint as pp
import numpy as np


def gen_event_size(event_size_file_name, event_index_name, output_file_name):
    '''
    We assume that the event file is not trimmed.
    '''
    fevent_size = open(event_size_file_name)
    feindex = open(event_index_name)

    event_size_dic = json.load(fevent_size)
    event_index_dic = json.load(feindex)

    num_events = len(event_index_dic)

    esize_vec = np.zeros(num_events, dtype=np.int)

    for ek in event_size_dic.keys():
        int_event_key = event_index_dic[ek]
        esize_vec[int_event_key] = event_size_dic[ek]

    np.savetxt(output_file_name, esize_vec, delimiter=",", fmt="%d")
    return esize_vec


def main():
    output_file_name = '../processed_data/event_size_vec.csv'
    event_size_file_name = '../processed_data/2013_event_size.json'
    event_index_name = '../processed_data/2013_event_key_index.json'

    esize_vec = gen_event_size(event_size_file_name, event_index_name, output_file_name)
    pp(esize_vec)


if __name__ == '__main__':
    main()
