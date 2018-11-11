#!/usr/bin/env python3
import subprocess
import argparse
import resource
import runpy
import cProfile, pstats


def take_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("src", nargs='+', help="src_file")
   parser.add_argument("-t",'--time', action='store_true', default=True)
   parser.add_argument("-m",'--memory', action='store_true')
   parser.add_argument("-n",'--numfunc', action='store_true')
   return parser.parse_args()


def launch_file(src_file):
    file = " ".join(src_file)
    run_file = subprocess.run([file], shell=True)
    # runpy.run_module("smart_db", run_name="__main__")
    # run_time_child = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    # print('run-time:', run_time_child)


def option_of_file():
    resource_consumed_child = resource.getrusage(resource.RUSAGE_SELF)
    if args.time:
       run_time_child = resource_consumed_child.ru_utime
       print('run-time:', run_time_child)
    if args.memory:
        memory_child = resource_consumed_child.ru_maxrss
        print('Memory usage: ' + str(memory_child) + ' KB' )
    # if args.numfunc:
    #     pr = cProfile.Profile()
    #     pr.enable()
    #     runpy.run_module("smart_db", run_name="__main__")
    #     pr.disable()
    #     sortby = 'cumulative'
    #     ps = pstats.Stats(pr).sort_stats(sortby)
    #     ps.print_stats()
    #     print(ps)

if __name__ == '__main__':
    args = take_args()
    launch_file(args.src)
    option_of_file()
