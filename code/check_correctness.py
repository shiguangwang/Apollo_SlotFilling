#!/usr/bin/env python2.7

import json
import numpy as np
from pprint import pprint as pp
from reverse_index import reverse_index_only as reverse_index


def checking_result(
    result_csv_file,
    ground_truth_json_file,
    event_set_json_file,
    event_set_index_file):
    '''
    This function checks the accuracy of the estimation.
    '''
    ground_truth_json = open(ground_truth_json_file)
    event_set_json = open(event_set_json_file)
    event_set_index = open(event_set_index_file)

    ground_truth_dic = json.load(ground_truth_json)
    event_set_dic = json.load(event_set_json)
    event_index_dic = json.load(event_set_index)
    index_event_dic = reverse_index(event_index_dic)

    # pp(ground_truth_dic)
    # pp(event_set_dic)
    # pp(event_index_dic)
    # pp(index_event_dic)

    result_vec = np.genfromtxt(result_csv_file,
        delimiter = ',', dtype = np.int)
    # pp(result_vec)
    [num_events] = result_vec.shape

    result_events = {}
    for j in range(num_events):
        key = index_event_dic[j]
        if result_vec[j] > 0:
            val = event_set_dic[key][result_vec[j] - 1]
        else:
            val = None
        result_events[key] = val
    # pp(result_events)

    result_correctness = np.zeros(num_events, dtype= np.int)
    for k in result_events.keys():
        # print(k)
        # print(result_events[k])
        # print(ground_truth_dic[k])
        # print('=====')
        if result_events[k] in ground_truth_dic[k]:
            result_correctness[event_index_dic[k]] = 1
    print(np.sum(result_correctness)*1.0/num_events)


def main():
    ground_truth_json_file = '../processed_data/2013_ground_truth.json'
    event_set_json_file = '../processed_data/2013_event_set.json'
    event_set_index_file = '../processed_data/2013_event_key_index.json'

    # Voting results:
    result_csv_file = '../processed_data/voting_results.csv'
    checking_result(result_csv_file,ground_truth_json_file,
        event_set_json_file,event_set_index_file)

    # EM results:
    em_result_csv_file = '../processed_data/em_results_no_category.csv'
    checking_result(em_result_csv_file,ground_truth_json_file,
        event_set_json_file, event_set_index_file)

if __name__ == '__main__':
    main()
