# -*- coding: utf-8 -*-

"""
组合总和
"""
res = []


candidates = [2, 3, 6, 7]
target = 7


def combinationsss(lists, target):
    if len(lists) == 0:
        return
    res = []
    def backstrack(tmp, target, start, lists):
        if target == 0:
            res.append(tmp)
        for i in range(start, len(lists)):
            if target < lists[i]:
                return
            backstrack(tmp+[lists[i]], target-lists[i], i, lists)
    backstrack([], target, 0, lists)
    return res


print(combinationsss(candidates, target))


def combins(lists, target):
    if not lists: return
    res = []
    def backstrack(lists, start, target, tmp):
        if target == 0:
            res.append(tmp)
        for i in range(start, len(lists)):
            if target < lists[i]:
                return
            backstrack(lists, i, target-lists[i], tmp+[lists[i]])
    backstrack(lists, 0, target, [])
    return res


print(combins(candidates, target))