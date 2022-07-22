# -*- coding: utf-8 -*-

"""
给定一个非负整数，反复将各个位上的数字相加，直到为一位数
input: 38
3+8=11 1+1=2
output: 2
"""


def numbersadd(nums):
    if nums <= 0:
        return 0
    if nums % 9 == 0:
        return 9
    else:
        return nums % 9


# print(numbersadd(145))


def addnumbers(nums):
    res = 0
    while nums > 0:
        res += nums % 10
        nums = nums // 10
        if res >= 10 and nums == 0:
            nums = res
            res = 0
    return res


print(addnumbers(145))


