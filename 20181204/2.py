#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
2. 从m个数中带权随机选择一个数
'''

import random

#二分查找，找到一个插入的区间，返回该区间的下标
def bisect(nums, k):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if k < nums[mid]:
            end = mid
        else:
            start = mid + 1
    return end

#将权重依次相加得到总数m，然后从m中随机选取一个数，落在哪个区间就选择哪个数，区间选择采用折半查找的方法
def func(nums):
    keys = list(nums.keys())
    total = 0
    weight = []
    for i in keys:
        weight.append(total + nums[i])
        total += nums[i]
    return nums[bisect(weight, random.randint(0, weight[-1] - 1))]


number = list(range(20))
weight = [random.randint(0, 20) for i in range(20)]
nums = {}
for i in range(len(number)):
    nums[number[i]] = weight[i]
print(func(nums))