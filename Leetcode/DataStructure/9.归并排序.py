# -*- coding: utf-8 -*-

"""
归并排序
"""


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    mid = round(len(lists)/2)
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res = res + left[i:] + right[j:]
    return res


ll = [-1, -8, 4, 5, 3, -3, 9]
# print(merge_sort(ll))
