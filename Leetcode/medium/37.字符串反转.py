# -*- coding: utf-8 -*-

"""
发表《A	Comparative	Study》（SCI）
反转:
表发《Study Comparative A》)ICS(
"""


def ReverseStr(strs):
    if not strs: return
    left = right = 0
    while right < len(strs):
        if strs[right] == "<":
            strs[left: right] = strs[left: right][::-1]
            left = right + 1
        elif strs[right] == ">":
            strs[left: right] = strs[left: right][::-1]
            strs[right+1:] = strs[right+1:][::-1]
        right += 1
    return strs


strs = ["发", "表", "<", "A", "Comparative", "Study", ">", "(", "S", "C", "I", ")"]
print(ReverseStr(strs))


