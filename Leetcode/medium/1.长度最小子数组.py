# -*- coding: utf-8 -*-

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。
如果不存在符合条件的连续子数组，返回 0。
"""


from ast import List


def minsubarray(lists, s):
    if not lists: return
    left, right = 0, 0
    N = len(lists)
    window_num = lists[0]
    res = N + 1
    while right < N:
        if window_num < s:
            right += 1
            if right < N:
                window_num += lists[right]
        else:
            res = min(right-left+1, res)
            window_num -= lists[left]
            left += 1
    return res if res < N+1 else 0


ll = [1, 8, 4, 5, 3, 3, 9,10]

print(minsubarray(ll, 15))


