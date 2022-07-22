# -*- coding: utf-8 -*-

"""
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""


def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    len1, len2 = len(haystack), len(needle)
    for start in range(len1 - len2 + 1):
        if haystack[start: start+len2] == needle:
            return start
    return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))


