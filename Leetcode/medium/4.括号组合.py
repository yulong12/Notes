# -*- coding: utf-8 -*-

"""
括号生成
"""


def generatekuohao(n):
    res = []

    def backstrack(tmp, left, right):
        if len(tmp) == 2*n:
            res.append("".join(tmp))
        if left < n:
            tmp.append("(")
            backstrack(tmp, left+1, right)
            tmp.pop()
        if right < left:
            tmp.append(")")
            backstrack(tmp, left, right+1)
            tmp.pop()

    backstrack([], 0, 0)
    return res


print(generatekuohao(3))


