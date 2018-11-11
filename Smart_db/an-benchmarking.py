#!/usr/bin/env python3

import resource
import subprocess
import pstats
import cProfile
import argparse


def getArgs():
    parser = argparse.ArgumentParser(description='benmark the program')
    parser.add_argument("src", nargs='+', help="src_file")
    parser.add_argument("-t",'--time', action='store_true')
    parser.add_argument("-m",'--memory', action='store_true')
    parser.add_argument("-n",'--numfunc', action='store_true')
    return parser.parse_args()


def launchFile(src_file):
    file = " ".join(src_file)
    print([file])
    run_file = subprocess.run([file], shell=True)


def getRunTime(resource_consumed_child):
   run_time_child = resource_consumed_child.ru_utime
   print('run-time:', run_time_child, 'sec')


def getMemory(resource_consumed_child):
    memory_child = resource_consumed_child.ru_maxrss
    print('Memory usage:', str(memory_child), 'KB' )


def getNumFunc():
    profile = cProfile.Profile()
    profile.enable()
    count_function = pstats.Stats(profile)
    print_each = count_function.print_stats()
    total_calls = count_function.total_calls
    print('Total calls:\t\t', total_calls, 'function calls')


def handleOutput(args):
    resource_consumed_child = resource.getrusage(resource.RUSAGE_CHILDREN)
    if args.time:
        getRunTime(resource_consumed_child)
    if args.memory:
        getMemory(resource_consumed_child)
    if args.numfunc:
        getNumFunc()


if __name__ == '__main__':
    args = getArgs()
    launchFile(args.src)
    handleOutput(args)
