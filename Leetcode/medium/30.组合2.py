# -*- coding: utf-8 -*-

"""
40 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


def cominationsums(lists, target):
    res = []
    lists.sort()

    def backstrack(lists, tmp, target, start):
        if target == 0 and tmp not in res:
            res.append(tmp)
        for i in range(start, len(lists)):
            if target < lists[i]:
                continue
            backstrack(lists, tmp+[lists[i]], target-lists[i], i+1)
    backstrack(lists, [], target, 0)
    return res


print(cominationsums([2,5,2,1,2], 5))


def combinesss(lists, target):
    if not lists: return
    res = []
    def backstrack(tmp, lists, target, start):
        if target == 0:
            res.append(tmp)
        for i in range(start, len(lists)):
            if lists[i] > target:
                continue
            backstrack(tmp+[lists[i]], lists, target-lists[i], i+1)
    backstrack([], lists, target, 0)
    return res

print(combinesss([2,5,2,1,2], 5))