# -*- coding: utf-8 -*-

"""
输入一个递增排序的数组和一个数字 S，在数组中查找两个数，
使得他们的和正好是 S，如果有多对数字的和等于 S，输出两个数的乘积最小的。
"""


def Twonumbers(lists, target):
    if not lists:
        return
    left = 0
    right = len(lists) - 1
    while left < right:
        sums = lists[left] + lists[right]
        if sums == target:
            return [lists[left], lists[right]]
        elif sums > target:
            right -= 1
        elif sums < target:
            left += 1


ll = [-13, -2, 0, 1, 2, 4, 5, 6, 10, 21, 32]
print(Twonumbers(ll, 19))
