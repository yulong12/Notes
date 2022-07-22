# -*- coding: utf-8 -*-

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段
使得 m段绳子 乘积最大
"""


def MaxOptimalValue(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
    return dp[-1]


print(MaxOptimalValue(4))



