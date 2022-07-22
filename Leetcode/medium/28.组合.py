# -*- coding: utf-8 -*-

"""
77 给定两个整数n和k，返回1-n中所有可能的k个数的组合
input: n = 4  k = 2
output:
[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]
"""


def combines(n, k):
    res = []

    def backstrack(tmp, start, n, flag):
        if len(tmp) == k:
            res.append(tmp)
        for i in range(start, n):
            if i in tmp or i < flag:
                continue
            backstrack(tmp+[i], start+1, n, i)
    backstrack([], 1, n+1, 1)
    return res


# print(combines(4, 2))



