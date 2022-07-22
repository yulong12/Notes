# -*- coding: utf-8 -*-
"""
连续子数组的最大和
"""


def Sumlists(lists):
    if not lists:
        return
    n = len(lists)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1] + lists[i-1]
        else:
            dp[i] = lists[i-1]
    return max(dp[1:])


ll = [-3, 2, -2, 3, 4, -30, 6, 10, 20]
print(Sumlists(ll))

