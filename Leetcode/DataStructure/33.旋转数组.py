# -*- coding: utf-8 -*-

"""
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数
input: [1,2,3,4,5,6,7] k =3
output: [5,6,7,1,2,3,4]
"""


def revolvelists(lists, k):
    if len(lists) == 0:
        return
    n = len(lists)
    if k == n:
        return lists
    lists[:] = lists[-k:] + lists[:-k]
    return lists


ll = [1, 2, 3, 4, 5, 6, 7]
k = 3

# print(revolvelists(ll, k))





