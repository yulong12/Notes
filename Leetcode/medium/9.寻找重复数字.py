# -*- coding: utf-8 -*-

"""
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
"""


def serachdupnumber(lists):
    n = len(lists)
    res = set()
    for i in range(len(lists)):
        index = lists[i]
        if index < n:
            if lists[index] < n:
                lists[index] += n
            else:
                res.add(lists[i])
        else:
            if lists[index-n] < n:
                lists[index-n] += n
            else:
                res.add(lists[i]-n)
    return res


ll = [1, 3, 5, 7, 6, 3, 2, 2]
# print(serachdupnumber(ll))




