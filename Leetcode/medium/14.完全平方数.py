# -*- coding: utf-8 -*-

"""
完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
"""


def numsqurt(n):
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, int(i**0.5) + 1):
            dp[i] = min(dp[i], dp[i-j**2]+1)
    return dp[-1]


print(numsqurt(17))



