#!/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(input_list):
    length = len(input_list)
    for i in range(length):
        for k in range(length - 1, i, -1):
            if (input_list[k] < input_list[k - 1]):
                swap(input_list, k, k - 1)


def swap(input_list, x, y):
    input_list[x], input_list[y] = input_list[y], input_list[x]


if __name__ == '__main__':
    test_list = [54, 22, 756, 1, 23, 3, 77, 43, 9, 2, 32, 97]
    print('Bubble sort')
    print('List before:', test_list)
    bubble_sort(test_list)
    print('List after:', test_list)