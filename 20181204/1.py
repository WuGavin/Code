#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1. 从m个数中随机不放回选取n个数字（m >= n）
'''

import random


#每次从0-m-1中选择一个数，然后将这个数与m-1位的数字交换，接着m-1，重复上面的过程
def func(nums, n):
    result = []
    m = len(nums)
    for i in range(n):
        j = random.randint(0, m - 1)
        result.append(nums[j])
        nums[j] = nums[m - 1]
        m -= 1
    return result

print(func(list(range(20)), 5))