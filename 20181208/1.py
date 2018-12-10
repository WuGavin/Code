#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
1. 有一个m*n的矩阵，一次行动只能选择往右或者往下走，求从(0,0)到(m-1,n-1)有多少种走法。
'''


#(i,j)位置上的走法等于(i-1,j)和(i,j-1)的走法的和
def func(m, n):
    dp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

print(func(2, 2))