# -*- coding: utf-8 -*-

"""
多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素
"""


def maxtuples(lists):
    lists.sort()
    return lists[len(lists)//2]


ls = [1, 2, 1, 4, 5, 1, 1, 1, 1]
# print(maxtuples(ls))


