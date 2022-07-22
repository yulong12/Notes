# -*- coding: utf-8 -*-

"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
输入: num = “1432219”, k = 3
输出: “1219”
"""


def removeKstr(strs, k):
    if len(strs) <= k:
        return "0"
    if k == 0:
        return strs
    stack, count = [], 0
    for i, x in enumerate(strs):
        if len(stack) > 0 and x < stack[-1]:
            stack.pop()
            count += 1
            if count == k:
                return "".join(stack)+strs[i:]
        stack.append(x)
    return "".join(stack[:len(strs)-k])


num = "1432219"
print(removeKstr(num, 3))


