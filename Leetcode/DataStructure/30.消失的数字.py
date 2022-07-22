# -*- coding: utf-8 -*-

"""
给定1，n中没有出现在数组中的数字
input:  [4, 3, 2, 7, 8, 2, 3, 1]
output: [5, 6]
"""


def disappearnumbers(lists):
    if len(lists) == 0:
        return
    for i in lists:
        index = abs(i) - 1
        lists[index] = -abs(lists[index])
    res = []
    for index, nums in enumerate(lists):
        if nums > 0:
            res.append(index)
    return res


ls = [4, 3, 2, 7, 8, 2, 3, 1]
print(disappearnumbers(ls))


