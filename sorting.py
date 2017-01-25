#!/bin/env python3
# -*- coding: utf-8 -*-
import time
import random


# helpers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def swap(input_list, x, y):
    input_list[x], input_list[y] = input_list[y], input_list[x]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def bubble_sort(input_list):
    """
    https://en.wikipedia.org/wiki/Bubble_sort
    """
    length = len(input_list)
    for i in range(length):
        for k in range(length - 1, i, -1):
            if (input_list[k] < input_list[k - 1]):
                swap(input_list, k, k - 1)


def bubble_sort_2(input_list):
    """
    https://en.wikipedia.org/wiki/Bubble_sort
    """
    change = True
    passnum = len(input_list) - 1
    while passnum > 0 and change:
        change = False
        for i in range(passnum):
            if input_list[i] > input_list[i + 1]:
                change = True
                swap(input_list, i, i + 1)
        passnum = passnum - 1


def quick_sort(input_list, begin=0, end=None):
    """
    https://en.wikipedia.org/wiki/Quicksort
    """
    def partition(input_list, begin, end):
        pivot = begin
        for i in range(begin + 1, end + 1):
            if input_list[i] <= input_list[begin]:
                pivot += 1
                swap(input_list, i, pivot)
        swap(input_list, pivot, begin)
        return pivot

    if end is None:
        end = len(input_list) - 1
    if begin >= end:
        return
    pivot = partition(input_list, begin, end)
    quick_sort(input_list, begin, pivot - 1)
    quick_sort(input_list, pivot + 1, end)


def merge_sort(input_list):
    """
    https://en.wikipedia.org/wiki/Merge_sort
    """
    if len(input_list) > 1:
        middle = len(input_list) // 2
        left_half = input_list[:middle]
        right_half = input_list[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i = i + 1
            else:
                input_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            input_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            input_list[k] = right_half[j]
            j = j + 1
            k = k + 1


if __name__ == '__main__':
    """
    Base sorting algorithms
    https://en.wikipedia.org/wiki/Sorting_algorithm

    """

    algorithms = [
        {
            'name': 'Bubble sort 1',
            'code': bubble_sort,
        },
        {
            'name': 'Bubble sort 2',
            'code': bubble_sort_2,
        },
        {
            'name': 'Quick sort 1',
            'code': quick_sort,
        },
        {
            'name': 'Merge sort',
            'code': merge_sort,
        },
    ]

    test_list = [54, 22, 756, 1, 23, 3, 77, 43, 9, 2, 32, 97]
    big_test_list = [random.randint(0, 10000) for x in range(10000)]

    for algorithm in algorithms:
        tmp_list = test_list[:]
        print(algorithm['name'])
        print('List before:', tmp_list)
        algorithm['code'](tmp_list)
        print('List after: ', tmp_list)

        print('Testing performance...')
        tmp_list = big_test_list[:]
        start_time = time.process_time()
        algorithm['code'](tmp_list)
        end_time = time.process_time()
        print('Sort time: {0}'.format(end_time - start_time))
        print()


