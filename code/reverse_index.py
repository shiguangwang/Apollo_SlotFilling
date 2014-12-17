#!/usr/bin/env python2.7

import json
from pprint import pprint as pp


def reverse_index(input_json_file_name, output_json_file_name):
    fi = open(input_json_file_name)
    dic = json.load(fi)
    pp(dic)
    reverse_dic = {}
    for k in dic.keys():
        reverse_dic[dic[k]] = k
    fo = open(output_json_file_name, 'w')
    json.dump(reverse_dic, fo, sort_keys=True, indent=4, ensure_ascii=False)
    return reverse_dic

def reverse_index_only(input_dic):
    reverse_dic = {}
    for k in input_dic.keys():
        reverse_dic[input_dic[k]] = k
    return reverse_dic

if __name__ == '__main__':
    input_json_file_name = '../processed_data/2013_sources_index.json'
    output_json_file_name = '../processed_data/2013_sources_reverse_index.json'
    reverse_dic = reverse_index(input_json_file_name, output_json_file_name)
    pp(reverse_dic)
