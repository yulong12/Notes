# -*- coding: utf-8 -*-

"""
从二维数组中找出最长上升的序列长度
input = [[9,9,4],
         [6,6,8],
         [2,1,1]]
output = 4
"""


def longestPath(matrix):
    if not matrix: return
    len1, len2 = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(len2)] for _ in range(len1)]
    res = 1
    for i in range(len1):
        for j in range(len2):
            res = max(res, dfs(matrix, i, j, dp))
    return res


def dfs(matrix, i, j, dp):
    if dp[i][j] != 0:
        return dp[i][j]
    dictor = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    res = 1
    for x, y in dictor:
        dx = x + i
        dy = y + i
        if 0 <= dx < len(matrix) and 0 <= dy < len(matrix[0]) and matrix[i][j] < matrix[dx][dy]:
            res = max(res, dfs(matrix, dx, dy, dp) + 1)
    return res


input = [[9,9,4],
         [6,6,8],
         [2,1,1]]
output = 4


print(longestPath(input))
