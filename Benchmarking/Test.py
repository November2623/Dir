#!/usr/bin/env python3

import json
import sys

def load_query():
    with open(sys.argv[1], 'r') as data_file:
        query = json.load(data_file)
    data_file.close()
    return query

def check_condition(query, data):
    pos = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    for x in pos.keys():
        if x in query['left']:
            value = data(pos[x])
    print(value)
def main():
    query = load_query()
    dir = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    line = sys.stdin.readline()
    while line!='':
        line = line.split(',')
        line[5] = line[5][:len(line[5]) - 1]
        line = sys.stdin.readline()
        if "where_and" in query.keys():
            flag = 1
            for x in query['where_and']:
                check_condition(x, line)
main()