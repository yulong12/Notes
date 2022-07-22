# -*- coding: utf-8 -*-

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    res, sign = 0, 1
    if x < 0:
        sign = -1
    x = abs(x)
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    res = res * sign
    return max(min(int_max, res), int_min)


print(reverse(123))


