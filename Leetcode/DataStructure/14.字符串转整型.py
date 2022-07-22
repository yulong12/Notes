# -*- coding: utf-8 -*-
"""
leetcode: 8
"""


def myAtoi(strs):
    if not strs:
        return 0
    res, i, sign = 0, 0, 1
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    n = len(strs)
    while i < n and strs[i] == " ":
        i += 1
    if i == n or n == 0: return 0
    if strs[i] == "-":
        sign = -1
    if strs[i] == "-" or strs[i] == "+":
        i += 1
    for s in strs[i:]:
        if "0" <= s <= "9":
            res = 10 * res + ord(s) - ord("0")
        else:
            break
    res = res * sign
    print(res)
    if res > int_max:
        return int_max
    if res < int_min:
        return int_min
    return res


print(myAtoi("42"))
