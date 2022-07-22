# -*- coding: utf-8 -*-

"""
29. 给定两个整数，被除数 dividend 和除数 divisor。
将两数相除，要求不使用乘法、除法和 mod 运算符。
"""


def divide(a, b):
    res = 0
    sign = 1 if a ^ b >= 0 else -1
    a, b = abs(a), abs(b)
    while a >= b:
        tmp, i = b, 1
        while a >= tmp:
            a -= tmp
            res += i
            i <<= 1
            tmp <<= 1
    res = res * sign
    return min(max(-2**31, res), 2**31-1)


print(divide(17, 3))

def dividess(a, b):
    if b == 0: return
    if a == 0: return 0
    res = 0
    sign = 1 if a ^ b >= 0 else -1
    a, b = abs(a), abs(b)
    while a >= b:
        tmp, cnt = b, 1
        while a >= tmp:
            a -= tmp
            res += cnt
            tmp <<= 1
            cnt <<= 1
    return res * sign


print(dividess(17, 3))