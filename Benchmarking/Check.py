#!/usr/bin/env python3
import json
import sys
def load_query():
    with open(sys.argv[1],'r') as json_file:
        json_data = json.load(json_file)
    for item in json_data:
        print(item)
load_query()
