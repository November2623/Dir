#!/usr/bin/env python3
import json
import sys
def load_query():
    with open(str(sys.argv[1]), "r") as f:
        query = json.load(f)
    f.close()
    return query
def check(query, data):
    pos = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    for x in pos.keys():
        if x in query['left']:
            value = data[pos[x]]
            break
    if "first_letter" in query['left']:
        value = value[0]
    if query['op'] == '=' and value == query['right']:
        return True
    elif query['op'] == '>' and value > query['right']:
        return True
    elif query['op'] == '<' and value < query['right']:
        return True
    elif query['op'] == '!=' and value != query['right']:
        return True
    return False
def output(result):
    for x in result:
        print(", ".join(x))
def main():
    query = load_query()
    pos = {'first_name': 0, 'last_name': 1, 'username': 2, 'age': 3,
           'gender': 4, 'city': 5}
    result = []
    line = sys.stdin.readline()
    while line != "":
        line = line.split(",")
        line[5] =  line[5][:len(line[5]) - 1]
        if "where_and" in query.keys():
            flag = 1
            for x in query['where_and']:
                if check(x, line) is False:
                    flag = 0
                    break
        elif "where_or" in query.keys():
            flag = 0
            for x in query['where_or']:
                if check(x, line) is True:
                    flag = 1
                    break
        if flag == 1:
            list = []
            for x in query['select'].split(", "):
                list.append(line[pos[x]])
            result.append(list)
        line = sys.stdin.readline()
    output(result)
main()