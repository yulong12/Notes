# -*- coding: utf-8 -*-



def charusort(lists):
    n = len(lists)
    if n == 0: return None
    for i in range(1, n):
        key = i - 1
        mark = lists[i]
        while key >= 0 and lists[key] > mark:
            lists[key+1] = lists[key]
            key -= 1
        lists[key+1] = mark
    return lists


ll = [-1, -8, 4, 5, 3, -3, 9]
# print(charusort(ll))

