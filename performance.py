#!/bin/env python3
# -*- coding: utf-8 -*-
import time


def make_simple_dict(size):
    data = {}
    for i in range(size):
        data[i] = i
    return data


def make_complex_dict(size, with_random_values=False):
    data = {}
    for i in range(size):
        data[i] = {
            'index': i,
            'char': 'a',
        }
    return data


def make_simple_calculations(size):
    data = {}
    for i in range(size):
        data[i] = i + i
    return data


def make_complex_calculations(size):
    data = {}
    for i in range(size):
        data[i] = ((i * i) / (i + 2)) + (i ** 2)
    return data


if __name__ == '__main__':
    """
    It's show basic conceptions about time of code execution
    """

    SIZES = [1000, 10000, 100000, 1000000, 10000000]

    FUNCTIONS = [
        make_simple_dict,
        make_complex_dict,
        make_simple_calculations,
        make_complex_calculations,
    ]

    for func in FUNCTIONS:
        print('\n{0}:'.format(func.__name__))
        for size in SIZES:
            start_time = time.process_time()
            dna = func(size)
            end_time = time.process_time()
            delta = end_time - start_time
            print('\t{0} elements: {1} sec.'.format(
                size,
                delta,
            ))



