# -*- coding: utf-8 -*-



def select_sort(lists):
    if len(lists) == 0: return None
    n = len(lists)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if lists[j] < lists[min]:
                min = j
        lists[i], lists[min] = lists[min], lists[i]
    return lists


ll = [-1, -8, 4, 5, 3, -3, 9]
# print(select_sort(ll))


