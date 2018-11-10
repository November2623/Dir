#!/usr/bin/python3
import argparse
import subprocess
import resource
from argparse import Namespace
def give_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('src', nargs='+', help= 'file_src')
    parser.add_argument('-m', '--mem', action= 'store_true', help= 'outputs the memory allocation of the target program')
    parser.add_argument('-t', '--time', action= 'store_true', help= 'outputs the execution time (run-time) of the target program')
    parser.add_argument('-n', action= 'store_true', help= 'outputs the number of function calls of the target program')
    args = parser.parse_args()
    return args

def option():
    Res = resource.getrusage(resource.RUSAGE_CHILDREN)
    if args.time:
        print('run-time:', Res.ru_utime)

def run_file(file_src):
    subprocess.run(file_src,shell=True)

args = give_args()
file = args.src
run_file(file)
option()