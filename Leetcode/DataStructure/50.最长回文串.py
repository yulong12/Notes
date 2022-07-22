# -*- coding: utf-8 -*-
"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
input: "abccccdd"
output: 7
"""

import collections


def longestStrs(strs):
    s_cnt = collections.Counter(strs)
    center = 0
    res = 0
    for rs in s_cnt:
        if s_cnt[rs] % 2:
            center = 1
            res += s_cnt[rs] - 1
        else:
            res += s_cnt[rs]
    return res + center


s = "abccccdd"
print(longestStrs(s))


