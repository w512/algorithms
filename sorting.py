#!/bin/env python3
# -*- coding: utf-8 -*-


# helpers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def swap(input_list, x, y):
    input_list[x], input_list[y] = input_list[y], input_list[x]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def bubble_sort(input_list):
    length = len(input_list)
    for i in range(length):
        for k in range(length - 1, i, -1):
            if (input_list[k] < input_list[k - 1]):
                swap(input_list, k, k - 1)


def bubble_sort_2(input_list):
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


if __name__ == '__main__':

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
            'name': 'Quick sort',
            'code': quick_sort,
        },
    ]

    test_list = [54, 22, 756, 1, 23, 3, 77, 43, 9, 2, 32, 97]

    for algorithm in algorithms:
        tmp_list = test_list[:]
        print(algorithm['name'])
        print('List before:', tmp_list)
        algorithm['code'](tmp_list)
        print('List after: ', tmp_list)
        print()


