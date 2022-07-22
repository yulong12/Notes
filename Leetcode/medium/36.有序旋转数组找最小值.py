# -*- coding: utf-8 -*-

"""
从有序旋转的数组中找出最小值
input = [3,4,5,1,2]
output = 1
"""


def findMin(lists):
    if not lists: return
    low, high = 0, len(lists) - 1
    while low < high:
        mid = (low + high) // 2
        if lists[mid] > lists[high]:
            low = mid + 1
        elif lists[mid] < lists[high]:
            high = mid
        else:
            high -= 1
    return lists[low]


ll = [3, 4, 5, 1, 2]
print(findMin(ll))
