#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
4. 反转数字，如120转成21。
'''

#每次取模10的数即可
def func(num):
    result = 0

    while num != 0:
        result = result * 10 + num % 10
        num //= 10

    return result

print(func(230))