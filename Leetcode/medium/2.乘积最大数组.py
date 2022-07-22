# -*- coding: utf-8 -*-

'''
找出数组中乘积最大的连续子数组
'''


def maxsublistsV(lists):
    if len(lists) <= 0: return
    n = len(lists)
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0], dp2[0] = lists[0], lists[0]
    for i in range(1, n):
        dp1[i] = max(lists[i - 1] * lists[i], lists[i])
        dp2[i] = min(lists[i - 1] * lists[i], lists[i])
    return max(dp1)


ll = [-1, 8, 4, 5, 3, -3, 9]
print(maxsublistsV(ll))



