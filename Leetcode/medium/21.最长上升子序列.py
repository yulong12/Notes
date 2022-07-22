# -*- coding: utf-8 -*-

"""
最长上升子序列
"""


def maxsubs(lists):
    if len(lists) <= 0:
        return
    n = len(lists)
    dp = [1 for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1):
            if lists[j] < lists[i]:
                dp[i] = max(dp[i], dp[j]+1)
        ans = max(ans, dp[i])
    return ans


ls = [10, 9, 2, 5, 3, 7, 101, 10, 18]
print(maxsubs(ls))


