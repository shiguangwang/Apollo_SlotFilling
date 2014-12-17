#!/usr/bin/env python2.7

import json
from pprint import pprint as pp
import numpy as np

FALSE = 1
TRUE = 2
UNKNOWN = 3

def gen_source_claim_matrix(event_file_name, source_file_name, event_index_name, source_index_name, output_file_name):
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
            if temp_dic[ek] in event_dic.keys():
                sc_mat[int(sk)][int(ek)] = TRUE
            else:
                sc_mat[int(sk)][int(ek)] = FALSE

    np.savetxt(output_file_name, sc_mat, delimiter=",", fmt='%1d')
    return sc_mat

def main():
    output_file_name = '../processed_data/source_claim_matrix.csv'
    event_file_name = '../processed_data/2013_ground_truth_trimmed.json'
    source_file_name = '../processed_data/2013_sources_trimmed.json'
    event_index_name = '../processed_data/2013_ground_truth_index.json'
    source_index_name = '../processed_data/2013_sources_index.json'

    sc_mat = gen_source_claim_matrix(event_file_name, source_file_name, event_index_name, source_index_name, output_file_name)

    pp(sc_mat)


if __name__ == '__main__':
    main()

