#!/usr/bin/env python3
import subprocess
import argparse
import resource
def take_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("src", nargs='+', help="src_file")
   parser.add_argument("-t",'--time', action='store_true')
   parser.add_argument("-m",'--memory', action='store_true')
   parser.add_argument("-n",'--numfunc', action='store_true')
   return parser.parse_args()
def launch_file(src_file):
    file = ' '.join(args.src)
    run_file = subprocess.run([file], shell=True)
def option_of_file():
    resource_consumed_child = resource.getrusage(resource.RUSAGE_CHILDREN)
    if args.time:
       run_time_child = resource_consumed_child.ru_utime
       print('run-time:', run_time_child)
    if args.memory:
        memory_child = resource_consumed_child.ru_maxrss
        print('Memory usage: ' + str(memory_child) + ' KB' )
    if args.numfunc:
        pass
    # if args.numfunc:
if __name__ == '__main__':
    args = take_args()
    launch_file(args.src)
    #  lay tai nguyen tieu thu cua target file
    option_of_file()
#./test.py ./hello.py -m
#./test.py ./hello.py -t
