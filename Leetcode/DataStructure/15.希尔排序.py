# -*- coding: utf-8 -*-


def xiersort(lists):
    n = len(lists)
    gap = round(n/2)

    while gap >= 1:
        for i in range(gap, n):
            temp = lists[i]
            j = i
            while j - gap >= 0 and lists[j - gap] > temp:
                lists[j] = lists[j - gap]
                j -= gap
            lists[j] = temp
        gap = round(gap / 2)
    return lists


ll = [-1, -8, 4, 5, 3, -3, 9]
# print(xiersort(ll))

