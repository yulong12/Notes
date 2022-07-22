# -*- coding: utf-8 -*-

"""
给定括号，判定是否有效
1. 左括号必须用相同类型的右括号闭合
2. 左括号必须以正确的顺序闭合
"""


def isValid(strs):
    d = {')': '(', ']': '[', '}': '{'}
    stack = []
    for s in strs:
        if s not in d:
            stack.append(s)
        else:
            tops = d[s]
            if len(stack) == 0 or tops != stack[-1]:
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        return False
    else:
        return True


strsss= "{[()(()}](()))"
# strsss = "()"
print(isValid(strsss))


def isvalidss(strs):
    if not strs: return
    d = {"}": "{", ")": "(", "]": "["}
