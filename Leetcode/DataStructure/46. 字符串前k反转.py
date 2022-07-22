# -*- coding: utf-8 -*-

"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。
"""


def reversK(strs, k):
    if not strs: return
    left, mid, right = 0, k, 2*k
    res = ""
    while len(res) < len(strs):
        res += strs[left: mid][::-1] + strs[mid: right]
        left, mid, right = left + 2*k, mid + 2*k, right + 2*k
    return res


a = "abcdefg"
print(reversK(a, 2))


