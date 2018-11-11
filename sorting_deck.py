#!/usr/bin/env python3
import argparse


def take_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('list', type=int, nargs='+')
    parser.add_argument('--algo', default="bubble")
    return parser.parse_args()


def main():
    args = take_args()
    list = args.list
    n = len(list)
    if args.algo == "bubble":
        bubble_sort(list)
    elif args.algo == "insert":
        insertion_sort(list)
    elif args.algo == "quick":
        quick_sort(list, 0, n-1)
    elif args.algo == "merge":
        merge_sort(list)


def bubble_sort(list):
    i = 0
    while i <= len(list) - 2:
        j = len(list) - 1
        while j >= i + 1:
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
        i += 1
    print(*list)


def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        temp = list[i]
        while temp < list[j] and j >= 0:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    print(*list)


def quick_sort(list, start, end):
    if start > end:
        return
    i = start
    j = end
    pivot = list[(start + end)//2]
    while i <= j:
        while list[i] < pivot:
            i += 1
        while list[j] > pivot:
            j -= 1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
        if(start < j):
            quick_sort(list, start, j)
        if(end > i):
            quick_sort(list, i, end)
    print(*list)


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1
        print(*list)


if __name__ == "__main__":
    main()
