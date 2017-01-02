#!/bin/env python3
# -*- coding: utf-8 -*-


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


def swap(input_list, x, y):
    input_list[x], input_list[y] = input_list[y], input_list[x]


if __name__ == '__main__':
    test_list = [54, 22, 756, 1, 23, 3, 77, 43, 9, 2, 32, 97]
    test_list_2 = [54, 22, 756, 1, 23, 3, 77, 43, 9, 2, 32, 97]

    print('Bubble sort (1)')
    print('List before:', test_list)
    bubble_sort(test_list)
    print('List after: ', test_list)
    print()

    print('Bubble sort (2)')
    print('List before:', test_list_2)
    bubble_sort_2(test_list_2)
    print('List after: ', test_list_2)
    print()
