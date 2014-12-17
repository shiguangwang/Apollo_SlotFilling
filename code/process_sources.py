#!/usr/bin/env python2.7
import os
import json
from pprint import pprint as pp
from utility_functions import save_to_json as savej
from utility_functions import list_all_files_to_be_processed as listfiles


sources_input_dir = '/Users/shiguang/Dropbox/KBP_DATA/new data/KBP_DATA/KBP_DATA/system_output/TAC_2013_KBP_Slot_Filler_Validation_Evaluation_Queries_V1.1/data/slot-filling_system_output'

sources_output_dir = '/Users/shiguang/Dropbox/KBP_DATA/new data/KBP_DATA/KBP_DATA/processed_data'


def save_to_json(dic, filename):
    output_file = os.path.join(sources_output_dir, filename)
    savej(dic, output_file)


def list_all_files_to_be_processed():
    return listfiles(sources_input_dir)
    # fs = filter(lambda x: x[0] != '.', os.listdir(sources_input_dir))
    # return fs


def parse_all_file(fs):
    dic = {}
    for f in fs:
        d = parse_each_file(os.path.join(sources_input_dir, f))
        dic[f] = d
    return dic


def parse_each_file(filename):
    f = open(filename)
    dic = {}
    for l in f:
        pair = parse_line(l)
        dic[pair[0]] = pair[1]
    return dic


def parse_line(line):
    fields = line.split('\t')
    key_field_1 = fields[0]
    key_field_2 = fields[1]
    key_field = key_field_1 + ':' + key_field_2
    var_field = fields[4].lower().rstrip().lstrip()
    return (key_field, var_field)


def main():
    fs = list_all_files_to_be_processed()
    dic = parse_all_file(fs)
    pp(dic)
    save_to_json(dic, '2013_sources_claims.json')

    dic_index = {}
    ind = 0
    for k in dic.keys():
        dic_index[k] = ind
        ind = ind + 1
    save_to_json(dic_index, '2013_sources_index.json')


if __name__ == '__main__':
    main()
