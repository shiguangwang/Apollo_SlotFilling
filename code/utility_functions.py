#!/usr/bin/env python2.7
import os
import json


def save_to_json(dic, filename):
    output_file = filename
    with open(output_file, 'w') as outfile:
        json.dump(dic, outfile, sort_keys=True, indent=4, ensure_ascii=False)


def list_all_files_to_be_processed(input_dir):
    fs = filter(lambda x: x[0] != '.', os.listdir(input_dir))
    return fs
