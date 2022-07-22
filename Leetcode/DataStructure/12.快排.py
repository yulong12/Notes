# -*- coding: utf-8 -*-


def part(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        v[low] = key
    return low


def quicklysort(List, left, right):
    if left < right:
        p = part(List, left, right)
        quicklysort(List, left, p-1)
        quicklysort(List, p+1, right)
    return List


ll = [-1, -8, 4, 5, 3, -3, 9]
# print(quicklysort(ll, 0, len(ll)-1))



