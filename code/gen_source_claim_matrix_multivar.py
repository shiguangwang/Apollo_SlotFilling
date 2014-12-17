#!/usr/bin/env python2.7

import json
from pprint import pprint as pp
import numpy as np

UNKNOWN = 0

def gen_source_claim_matrix(event_file_name, source_file_name, event_index_name, source_index_name, output_file_name):
    '''
    Here we assume that the event file and the source dic keys are not
    trimmed.
    '''
    fevent = open(event_file_name)
    fsource = open(source_file_name)
    feindex = open(event_index_name)
    fsindex = open(source_index_name)

    event_dic = json.load(fevent)
    source_dic = json.load(fsource)

    event_index_dic = json.load(feindex)
    source_index_dic = json.load(fsindex)

    num_events = len(event_index_dic)
    num_sources = len(source_index_dic)

    shape = (num_sources, num_events)
    print(shape)
    sc_mat = np.zeros(shape, dtype=np.int)
    sc_mat[:][:] = UNKNOWN

    for sk in source_dic.keys():
        temp_dic = source_dic[sk]
        for ek in temp_dic.keys():
            assert temp_dic[ek] in event_dic[ek]
            int_source_key = source_index_dic[sk]
            int_event_key = event_index_dic[ek]
            sc_mat[int_source_key][int_event_key] = event_dic[ek].index(temp_dic[ek]) + 1

    np.savetxt(output_file_name, sc_mat, delimiter=",", fmt="%d")
    return sc_mat

def main():
    output_file_name = '../processed_data/source_claim_matrix.csv'
    event_file_name = '../processed_data/2013_event_set.json'
    source_file_name = '../processed_data/2013_sources_claims.json'
    event_index_name = '../processed_data/2013_event_key_index.json'
    source_index_name = '../processed_data/2013_sources_index.json'

    sc_mat = gen_source_claim_matrix(event_file_name, source_file_name, event_index_name, source_index_name, output_file_name)

    pp(sc_mat)


if __name__ == '__main__':
    main()

