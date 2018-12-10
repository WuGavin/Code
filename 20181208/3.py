#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
3. 编辑距离：从一个字符串变成另外一个字符串需要的最小修改次数，单次修改只能删除，修改或者增加一个字母。例如abc变成ade需要2步。
'''

#求三个数中的最小值
def minimum(a, b, c):
    if a > b:
        return b if c > b else c
    else:
        return a if c > a else c

#通过减小字符串的长度往前递推编辑距离，例如'abe'和'adc'的编辑距离由'ab'和'adc'，'abe'和'ad'，'ab'和'ad'的编辑距离决定
def func(a, b):
    m = len(a)
    n = len(b)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = minimum(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
    return dp[m][n]

print(func('wise', 'wiew'))