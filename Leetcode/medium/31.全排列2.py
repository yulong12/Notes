# -*- coding: utf-8 -*-

"""
47 给定一个可包含重复数字的序列，返回所有不重复的全排列。
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def alluniques(lists):
    if len(lists) == 0:
        return
    res = []
    def backstrack(lists, tmp):
        if len(lists) == 0 and tmp not in res:
            res.append(tmp)
        for i in range(len(lists)):
            backstrack(lists[:i]+lists[i+1:], tmp+[lists[i]])
    backstrack(lists, [])
    return res


print(alluniques([1, 1, 2]))


