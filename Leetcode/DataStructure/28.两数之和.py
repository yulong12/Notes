# -*- coding: utf-8 -*-

"""
两数之和

input: [2, 7, 11, 15] target: 9
output: [0,1]
"""


def twoaddnums(lists, target):
    if len(lists) == 0:
        return
    res = []
    d = dict()
    for i in range(len(lists)):
        rs = target - lists[i]
        if rs in d:
            res.append([d[rs],i])
        d[lists[i]] = i
    return res


ls = [2, 7, 11, 15, 3, 6]
print(twoaddnums(ls, 9))

