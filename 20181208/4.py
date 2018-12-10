#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
4. 假设有一个数组，只有一个数出现一次，其他数都出现两次，求出现一次的数。
'''

#利用异或操作，a^a=0，0^a=a，将数组所有的数进行异或，即可得到只出现一次的数
def func(nums):
    result = 0
    for i in nums:
        result ^= i
    return result

print(func([1, 2, 2, 10, 1, 4, 5, 4, 5]))