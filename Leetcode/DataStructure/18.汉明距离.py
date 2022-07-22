# -*- coding: utf-8 -*-

"""
汉明距离：两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目
"""

def hanming(x, y):
    xy = x ^ y
    counter = 0
    while xy:
        if xy & 1 == 1:
            counter += 1
        xy = xy >> 1
    return counter


l1 = 10
l2 = 30
print(hanming(l1, l2))


