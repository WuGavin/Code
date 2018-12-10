#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
3. 从不知道长度的数组中随机选取n个数
'''

import random

#蓄水池算法：https://www.cnblogs.com/snowInPluto/p/5996269.html
def func(nums, n):
    result = [nums[i] for i in range(n)]
    for i in range(len(nums) - n):
        m = random.randint(0, i + n)
        if m < n:
            result[m] = nums[i + n]
    return result

print(func(list(range(30)), 5))
