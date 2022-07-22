# -*- coding: utf-8 -*-
"""
给定两个以字符串形式表示的非负整数，返回字符串表示的乘积
input: "2" "3"
output: "6"
"""


def strtoint(strs):
    return ord(strs) - ord("0")


def mutlstrs(str1, str2):
    s1 = str1[::-1]
    s2 = str2[::-1]
    res = 0
    for i, a in enumerate(s1):
        tmp = 0
        for j, b in enumerate(s2):
            tmp += (ord(a) - ord("0")) * (ord(b) - ord("0")) * 10 ** j
        res += tmp * 10 ** i
    return str(res)


print(mutlstrs("103", "23"))

