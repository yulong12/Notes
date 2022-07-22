# -*- coding: utf-8 -*-

"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

"""


def removeElement(lists, val):
    if len(lists) == 0:
        return
    j = 0
    for i in range(len(lists)):
        if lists[i] != val:
            # lists[j] = lists[i]
            j += 1
    return j


ll = [3, 2, 2, 3]
print(removeElement(ll, 3))





