# -*- coding: utf-8 -*-

"""
找出字符串中第一个只出现一次的字符串
"""

import collections

def firststr(strs):
    if len(strs) <= 0: return
    dics = collections.defaultdict(int)
    for i in strs:
        dics[i] += 1
    for i in strs:
        if dics[i] == 1:
            return i
    return " "


strs = "abaccdefff"
# print(firststr(strs))


