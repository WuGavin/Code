#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1. 假设有数组a和数组b，两个数组都为降序排列，且score(i,j)=a[i]+b[j]，求score(i,j)的前k大的值。
'''

#返回无序数组最大值以及它的下标
def maximum(nums):
    max_num = nums[0]
    max_idx = 0
    for idx, num in enumerate(nums):
        if num > max_num:
            max_num = num
            max_idx = idx
    return max_num, max_idx

#利用递推不等式:
#      a[0] + b[0] >= a[0] + b[1] >= a[0] + b[2] >= ... >= a[0] + b[n]
#      a[1] + b[0] >= a[1] + b[1] >= a[1] + b[2] >= ... >= a[1] + b[n]
#                                 ... 
#      a[m] + b[0] >= a[m] + b[1] >= a[m] + b[2] >= ... >= a[m] + b[n]
#可知道每次比较每行不等式第一个数的大小，取出最大那个数，并将不等式往后移
def func(a, b, k):
    if k > len(a) * len(b):
        k = len(a) * len(b)
    result = []

    num = []   #存每行不等式第一个数
    idx = []   #存每行不等式加到b的那个数

    num.append(a[0] + b[0])
    idx.append(0)

    while k > 0:
        max_num, max_idx = maximum(num)
        result.append(max_num)
        idx[max_idx] += 1
        if idx[max_idx] >= len(b):
            num[max_idx] = -999
        else:
            num[max_idx] = a[max_idx] + b[idx[max_idx]]
        if len(num) < len(a):
            num.append(a[len(num)] + b[0])
            idx.append(0)
        k -= 1
    return result


print(func([10, 8, 7, 6, 4, 1], [11, 9, 8, 6, 5], 20))