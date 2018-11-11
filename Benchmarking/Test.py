#!/usr/bin/env python3

import json
import sys

def load_query():
    with open(sys.argv[1],'r') as json_file:
        json_data = json.load(json_file)
    json_file.close()
    return json_data

def compare(a, b, c):
    if b == '=' and a == c:
        return True
    elif b == '>' and a > c:
        return True
    elif b == '<' and a < c:
        return True
    elif b == '!=' and a != c:
        return True
    return False


def check_condition(query, data):  # ({},['a','b','c'])
    pos = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    for x in pos.keys():
        if x in query['left']: # x = 'fd'
            value = data[pos[x]]
            break
    if 'first_letter' in query['left']:
        value = value[0]
    elif 'age' in query['left']:
        query['right'] = int(query['right'])
    return compare(value, query['op'], query['right'])



def main():
    result = []
    pos = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    lines = sys.stdin.readlines()
    query = load_query()
    for line in lines:
        line = line.split(',')
        line[3] = int(line[3])
        line[5] = line[5][:len(line[5]) - 1]
        for x in range(len(query)):
            result.append([])
            flag = 1
            if "where_and" in query[x].keys():
                for a in query[x]['where_and']: # x = {'left': 'fd','op': 'fd','right': 'fd'}
                    if check_condition(a, line) is False:
                        flag = 0
                        break
            elif "where_or" in query[x].keys():
                flag = 0
                for b in query[x]['where_or']: # x = {'left': 'fd','op': 'fd','right': 'fd'}
                    if check_condition(b, line) is True:
                        flag = 1
                        break
            if flag == 1:
                result[x].append(line)


    for x in range(len(query)):
        final = []
        if 'order' in query[x].keys():
            result[x].sort(key = lambda k : k[pos[query[x]['order']]])
        for y in result[x]:
            temp = []
            for z in query[x]['select'].split(", "):
                temp.append(y[pos[z]])
            final.append(temp)
        get_result(final)


def get_result(list1):
    for x in range(len(list1)):
        for e in range(len(list1[x])):
            list1[x][e] = str(list1[x][e])
        print(', '.join(list1[x]))



if __name__ == '__main__':
    print(sys.argv[1])
    main()
