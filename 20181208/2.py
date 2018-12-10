#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
2. 有一个m*n的矩阵，一次行动只能选择往右或者往下走，并且有些格子有障碍物，不能通过，求从(0,0)到(m-1,n-1)有多少种走法。
'''


#(i,j)位置上的走法等于(i-1,j)和(i,j-1)的走法的和，如果被堵住了，就置为0
def func(maze):
    m = len(maze)
    if m == 0:
        return 0
    n = len(maze[0])
    dp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
    
maze = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
print(func(maze))