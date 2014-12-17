#!/usr/bin/env python2.7
import os
import json
import numpy as np
from pprint import pprint as pp
from utility_functions import save_to_json as savej
from utility_functions import list_all_files_to_be_processed as listfiles

ground_truth_input_dir = '/Users/shiguang/Dropbox/KBP_DATA/new data/KBP_DATA/KBP_DATA/ground_truth/LDC2013E91_TAC_2013_KBP_English_Regular_Slot_Filling_Evaluation_Assessment_Results_V1.1/data'
ground_truth_output_dir = '/Users/shiguang/Dropbox/KBP_DATA/new data/KBP_DATA/KBP_DATA/processed_data'

noneCount = 0


def save_to_json(dic, filename):
    output_file = os.path.join(ground_truth_output_dir, filename)
    savej(dic, output_file)



def list_all_files_to_be_processed():
    fs = listfiles(ground_truth_input_dir)
    print(len(fs))
    return fs


def parse_file_system(fs):
    pairs = [
        parse_each_file(os.path.join(ground_truth_input_dir, f)) for f in fs]
    dic = {}
    for (k, v) in pairs:
        if not k is None:
            dic[k] = []
            if None in v:
                v.remove(None)
            dic[k].extend(v)
    return dic


def parse_each_file(filename):
    f = open(filename)
    dic = {}
    for l in f:
        pair = parse_line(l)
        if pair is None:
            continue
        if pair[0] in dic:
            dic[pair[0]].add(pair[1])
        else:
            dic[pair[0]] = set([pair[1]])
    if len(dic) == 0:
        return (None, set([]))
    return (dic.keys()[0], dic.values()[0])


def parse_line(line):
    fields = line.split('\t')
    key_field = fields[1]
    cond_field = fields[10]
    var_field = fields[3].lower().rstrip().lstrip()
    if cond_field == 'C':
        return (key_field, var_field)
    return (key_field, None)


def main():
    dic = parse_file_system(list_all_files_to_be_processed())
    # pp(dic)
    save_to_json(dic, '2013_ground_truth.json')

    dic_index = {}
    ind = 0
    for k in dic.keys():
        dic_index[k] = ind
        ind = ind + 1
    # pp(dic_index)
    save_to_json(dic_index, '2013_event_key_index.json')

    # print(len(dic.keys()))

    godview_results = np.zeros(len(dic))
    # pp(godview_results)
    for k in dic.keys():
        if len(dic[k]) > 0:
            godview_results[dic_index[k]] = 1
    correct_cnt = sum(godview_results)
    print(correct_cnt/len(dic))
    print(correct_cnt)
    print(len(dic))

if __name__ == '__main__':
    main()
