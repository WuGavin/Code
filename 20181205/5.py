#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
5. 无序数组求第k大的数。
'''

#利用快速排序的特性
def func(a, k):
    k = len(a) - k
    low = 0
    high = len(a) - 1

    while True:
        start = low
        end = high
        pivot = a[start]
        #
        while start < end:
            while end > start and a[end] > pivot:
                end -= 1
            while start < end and a[start] < pivot:
                start += 1
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
        a[start] = pivot
        if start == k:
            return pivot
        elif start > k:
            high = start - 1
        else:
            low = end + 1

    
print(func([19, 20, 100, 1, 6, 3, 9, 40], 1))