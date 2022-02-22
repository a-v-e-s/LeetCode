#!/usr/bin/env python

"""
recommended use:
$ ./sorting_demonstrations.py | less
or:
$ python sorting_demonstrations.py | less
"""


import random
import timeit


LENGTH = 20

rarr = lambda length=LENGTH: [random.randint(1, length*3) for _ in range(length)]


def bubble_sort(array, printing=True):
    n = len(array)
    if printing: print(array)
    for i in range(n):
        already_sorted = True
        for j in range(n-i-1):
            if printing: print(f'comparing: {array[j]} and {array[j+1]}')
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                if printing: print(array)
                already_sorted = False
        if already_sorted:
            break
    return array


def insertion_sort(array, printing=True):
    if printing: print(array)
    for i in range(1, len(array)):
        key_item = array[i]
        if printing: print(f'key_item: {key_item}')
        j = i-1
        while True:
            if j >= 0:
                if printing: print(f'comparing: key_item({key_item}) and {array[j]}')
            else:
                break
            if array[j] > key_item:
                array[j+1] = array[j]
                j -= 1
            else:
                break
        array[j+1] = key_item
        if printing: print(array)
    return array


def merge_sort(array, printing=True):
    #
    def _split(array):
        if printing: print(f'\nsplit called with {array}')
        if len(array) < 2:
            if printing: print(f'array too small to split; returning {array}')
            return array
        midpoint = len(array) // 2
        if printing: print(f'midpoint slice at: {midpoint}')
        if printing: print(f'left half: {array[:midpoint]}')
        if printing: print(f'right half: {array[midpoint:]}')
        return _merge(_split(array[:midpoint]), _split(array[midpoint:]))
    #
    def _merge(left, right):
        if printing: print(f'\nmerge called for {left} and {right}')
        if len(left) == 0:
            if printing: print(f'left half empty; returning {right}')
            return right
        if len(right) == 0:
            if printing: print(f'right half empty; returning {left}')
            return left
        result = []
        index_left = index_right = 0
        while len(result) < (len(left) + len(right)):
            if printing: print(f'comparing: {left[index_left]} and {right[index_right]}')
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
                if printing: print(f'combined array: {result}')
            else:
                result.append(right[index_right])
                index_right += 1
                if printing: print(f'combined array: {result}')
            if index_right == len(right):
                result += left[index_left:]
                if printing: print(f'right half exhausted; appending {left[index_left:]}')
                break
            if index_left == len(left):
                result += right[index_right:]
                if printing: print(f'left half exhausted; appending {right[index_right:]}')
                break
        if printing: print(f'returning: {result}')
        return result
    #
    return _split(array)


def quicksort(array, printing=False):
    if printing: print(f'\nquicksort called with {array}')
    if len(array) < 2:
        if printing: print(f'array too small; returning {array}')
        return array
    low, same, high = [], [], []
    pivot = array[random.randint(0, len(array)-1)]
    if printing: print(f'pivot = {pivot}')
    for item in array:
        if item < pivot:
            low.append(item)
            if printing: print(f'{item} < {pivot}; assigning to low: {low}')
        elif item == pivot:
            same.append(item)
            if printing: print(f'{item} == {pivot}; assigning to same: {same}')
        elif item > pivot:
            high.append(item)
            if printing: print(f'{item} > {pivot}; assigning to high: {high}')
    if printing: print(f'arrays divided!\nlow: {low}\nsame: {same}\nhigh: {high}')
    combined = quicksort(low) + same + quicksort(high)
    if printing: print(f'\nreturning: {combined}')
    return combined


def timsort(array, min_run=4, printing=True):
    #
    def _timsort_insertion(array, left=0, right=None):
        if printing: print(f'\n\ttimsort_insertion sort called with array={array}, left={left}, right={right}')
        if right is None:
            right = len(array) - 1
            if printing: print(f'\tright set to: {right}')
        for i in range(left+1, right+1):
            key_item = array[i]
            if printing: print(f'\tkey_item: {key_item}')
            j = i - 1
            while True:
                if j >= left:
                    if printing: print(f'\tcomparing {array[j]} and {key_item}')
                else:
                    break
                if array[j] > key_item:
                    array[j+1] = array[j]
                    j -= 1
                else:
                    break
            array[j+1] = key_item
            if printing: print(f'\t{array}')
        return array
    #
    def _timsort_merge(left, right):
        if printing: print(f'\n\ttimsort_merge called for {left} and {right}')
        if len(left) == 0:
            if printing: print(f'\tleft half empty; returning {right}')
            return right
        if len(right) == 0:
            if printing: print(f'\tright half empty; returning {left}')
            return left
        result = []
        index_left = index_right = 0
        while len(result) < (len(left) + len(right)):
            if printing: print(f'\tcomparing: {left[index_left]} and {right[index_right]}')
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
                if printing: print(f'\tcombined: {result}')
            else:
                result.append(right[index_right])
                index_right += 1
                if printing: print(f'\tcombined: {result}')
            if index_right == len(right):
                result += left[index_left:]
                if printing: print(f'\tright half exhausted; appending {left[index_left:]}')
                break
            if index_left == len(left):
                result += right[index_right:]
                if printing: print(f'\tleft half exhausted; appending {right[index_right:]}')
                break
        if printing: print(f'\treturning: {result}')
        return result
    #
    n = len(array)
    for i in range(0, n, min_run):
        _timsort_insertion(array, i, min((i + min_run - 1), n-1))
    size = min_run
    while size < n:
        for start in range(0, n, size*2):
            if printing: print(f'startpoint: {start}')
            midpoint = start + size - 1
            if printing: print(f'midpoint: {midpoint}')
            end = min((start + size*2 - 1), (n-1))
            if printing: print(f'endpoint: {end}')
            merged_array = _timsort_merge(array[start : midpoint+1], array[midpoint+1 : end+1])
            array[start : start+len(merged_array)] = merged_array
        size *= 2
    if printing: print(f'returning: {array}')
    return array


def main():
    print()
    print('### BUBBLE SORT: ###')
    bubble_sort(rarr())

    print(); print('#'*80); print()
    
    print('### INSERTION SORT: ###')
    insertion_sort(rarr())

    print(); print('#'*80); print()
    
    print(); print('### MERGE SORT: ###')
    merge_sort(rarr())

    print(); print('#'*80); print()

    print(); print('### QUICK SORT: ###')
    quicksort(rarr(), True)

    print(); print('#'*80); print()
    
    print(); print('### TIM SORT: ###')
    timsort(rarr(20), min_run=4)

    print(); print('#'*80); print()

    print('### TIMING BUBBLE SORT, LENGTH=100:', end='\t')
    setup = 'from __main__ import bubble_sort, rarr; array=rarr(100)'
    stmt = 'bubble_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING BUBBLE SORT, LENGTH=1000:', end='\t')
    setup = 'from __main__ import bubble_sort, rarr; array=rarr(1000)'
    stmt = 'bubble_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING BUBBLE SORT, LENGTH=10000:', end='\t')
    setup = 'from __main__ import bubble_sort, rarr; array=rarr(10000)'
    stmt = 'bubble_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')

    print(); print('#'*80); print()

    print()
    print('### TIMING INSERTION SORT, LENGTH=100:', end='\t')
    setup = 'from __main__ import insertion_sort, rarr; array=rarr(100)'
    stmt = 'insertion_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING INSERTION SORT, LENGTH=1000:', end='\t')
    setup = 'from __main__ import insertion_sort, rarr; array=rarr(1000)'
    stmt = 'insertion_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING INSERTION SORT, LENGTH=10000:', end='\t')
    setup = 'from __main__ import insertion_sort, rarr; array=rarr(10000)'
    stmt = 'insertion_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')

    print(); print('#'*80); print()

    print()
    print('### TIMING MERGE SORT, LENGTH=100:', end='\t')
    setup = 'from __main__ import merge_sort, rarr; array=rarr(100); printing=False'
    stmt = 'merge_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING MERGE SORT, LENGTH=1000:', end='\t')
    setup = 'from __main__ import merge_sort, rarr; array=rarr(1000); printing=False'
    stmt = 'merge_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING MERGE SORT, LENGTH=10000:', end='\t')
    setup = 'from __main__ import merge_sort, rarr; array=rarr(10000); printing=False'
    stmt = 'merge_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING MERGE SORT, LENGTH=100000:', end='\t')
    setup = 'from __main__ import merge_sort, rarr; array=rarr(100000); printing=False'
    stmt = 'merge_sort(array, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')

    print(); print('#'*80); print()

    print()
    print('### TIMING QUICKSORT, LENGTH=100:', end='\t')
    setup = 'from sorting_demonstrations import quicksort, rarr; array=rarr(100); printing=False'
    stmt = 'quicksort(array, printing)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING QUICKSORT, LENGTH=1000:', end='\t')
    setup = 'from sorting_demonstrations import quicksort, rarr; array=rarr(1000); printing=False'
    stmt = 'quicksort(array, printing)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING QUICKSORT, LENGTH=10000:', end='\t')
    setup = 'from sorting_demonstrations import quicksort, rarr; array=rarr(10000); printing=False'
    stmt = 'quicksort(array, printing)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING QUICKSORT, LENGTH=100000:', end='\t')
    setup = 'from sorting_demonstrations import quicksort, rarr; array=rarr(100000); printing=False'
    stmt = 'quicksort(array, printing)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')

    print(); print('#'*80); print()

    print()
    print('### TIMING TIMSORT, LENGTH=100:', end='\t')
    setup = 'from __main__ import timsort, rarr; array=rarr(100)'
    stmt = 'timsort(array, 32, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING TIMSORT, LENGTH=1000:', end='\t')
    setup = 'from __main__ import timsort, rarr; array=rarr(1000)'
    stmt = 'timsort(array, 32, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING TIMSORT, LENGTH=10000:', end='\t')
    setup = 'from __main__ import timsort, rarr; array=rarr(10000)'
    stmt = 'timsort(array, 32, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')
    print('### TIMING TIMSORT, LENGTH=100000:', end='\t')
    setup = 'from __main__ import timsort, rarr; array=rarr(100000)'
    stmt = 'timsort(array, 32, False)'
    time = timeit.timeit(stmt, setup, number=10) / 10
    print(f'{time} seconds')


if __name__ == '__main__':
    main()