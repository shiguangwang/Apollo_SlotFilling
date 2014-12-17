#!/usr/bin/env python2.7
import json
from pprint import pprint as pp


def trim_keys(input_file_name, input_key_file_name, output_json_file_name):
    '''
    Convert the source keys from text to index.
    '''
    fi = open(input_file_name)
    ki = open(input_key_file_name)
    fo = open(output_json_file_name, 'w')

    input_dic = json.load(fi)
    key_index_dic = json.load(ki)
    output_dic = {}

    for k in input_dic.keys():
        trimmed_key = key_index_dic[k]
        output_dic[trimmed_key] = input_dic[k]

    json.dump(output_dic, fo)
    return output_dic


def trim_sub_keys(input_file_name, input_key_file_name, output_file_name):
    '''
    Convert the source claims from text to index.
    '''
    fi = open(input_file_name)
    ki = open(input_key_file_name)
    fo = open(output_file_name, 'w')

    input_dic = json.load(fi)
    key_index_dic = json.load(ki)
    output_dic = {}

    for k in input_dic.keys():
        temp_dic = {}
        for tk in input_dic[k].keys():
            if tk in key_index_dic.keys():
                trimmed_key = key_index_dic[tk]
                temp_dic[trimmed_key] = input_dic[k][tk]
        output_dic[k] = temp_dic

    json.dump(output_dic, fo)
    return output_dic


def main():
    input_file_name = '../processed_data/2013_sources_claims.json'
    input_key_file_name = '../processed_data/2013_sources_index.json'
    output_json_file_name = '../processed_data/2013_sources_trimmed.json'
    pp(trim_keys(input_file_name, input_key_file_name, output_json_file_name))
    input_file_name = '../processed_data/2013_sources_trimmed.json'
    input_key_file_name = '../processed_data/2013_ground_truth_index.json'
    output_json_file_name = '../processed_data/2013_sources_trimmed_2.json'
    pp(trim_sub_keys(input_file_name, input_key_file_name, output_json_file_name))

if __name__ == '__main__':
    main()
