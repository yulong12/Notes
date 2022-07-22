# -*- coding: utf-8 -*-



def maopao(lists):
    if len(lists) == 0:
        return None
    n = len(lists)
    for i in range(n):
        for j in range(1, n-i):
            if lists[j-1] > lists[j]:
                lists[j-1], lists[j] = lists[j], lists[j-1]
    return lists


ll = [-1, -8, 4, 5, 3, -3, 9]
# print(maopao(ll))


