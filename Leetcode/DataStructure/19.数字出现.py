# -*- coding: utf-8 -*-

"""
只出现一次数字,其他元素出现过两次
input : [1, 2, 3, 3, 2]
output: 1
"""


def findonenumber(lists):
    if len(lists) == 0:
        return
    result = 0
    for num in lists:
        result = result ^ num
    return result


ll = [1, 3, 4, 7, 3, 1, 7]
print(findonenumber(ll))


