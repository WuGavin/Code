#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
3. 求无序数组中最长连续序列，例如[1,9,3,5,4,10,8,100,2,93]的最长连续序列为1,2,3,4,5。
'''

#看nums[i]+1在不在数组里，当nums[i]-1在数组里时，可以不查找，以减少不必要的查找时间
def func(nums):
    max_length = 0
    start_pos = 0

    d = {}
    for i in nums:
        d[i] = 1

    for i in nums:
        if i - 1 in d:
            continue
        temp = i
        length = 0
        while temp in d:
            length += 1
            temp += 1
        if length > max_length:
            max_length = length
            start_pos = i
    return list(range(start_pos, max_length + start_pos))

print(func([1,9,3,4,10,8,100,2,93]))

