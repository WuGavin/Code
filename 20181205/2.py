#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
2. 假设有降序排列的数组a，且score(i,j)=a[i]+a[j]，i不等于j，求score(i,j)的前k大的值。
'''

from functools import reduce

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
#      a[0] + a[1] >= a[0] + a[2] >= a[0] + a[3] >= ... >= a[0] + a[n]
#      a[1] + a[2] >= a[1] + a[3] >= a[1] + a[4] >= ... >= a[1] + a[n]
#                                 ... 
#      a[n-1] + a[n]
#可知道每次比较每行不等式第一个数的大小，取出最大那个数，并将不等式往后移
def func(a, k):
    total = sum(list(range(len(a))))
    if k > total:
        k = total

    result = []

    num = []   #存每行不等式第一个数
    idx = []   #存每行不等式加到b的那个数

    num.append(a[0] + a[1])
    idx.append(1)

    while k > 0:
        max_num, max_idx = maximum(num)
        result.append(max_num)
        idx[max_idx] += 1
        if idx[max_idx] >= len(a):
            num[max_idx] = -999
        else:
            num[max_idx] = a[max_idx] + a[idx[max_idx]]
        if len(num) < len(a) - 1:
            idx.append(len(num) + 1)
            num.append(a[len(num)] + a[len(num) + 1])
        k -= 1
    return result


print(func([10, 8, 7, 6, 4, 1], 20))