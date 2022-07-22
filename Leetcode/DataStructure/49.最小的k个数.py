# -*- coding: utf-8 -*-

"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
"""


def findMinKlists(lists, k):
    if not lists: return
    keyv = lists[0]
    al = [lists[i] for i in range(len(lists)) if lists[i] <= keyv]
    bl = [lists[i] for i in range(len(lists)) if lists[i] > keyv]
    if len(al) == k:
        return al
    elif len(al) > k:
        return findMinKlists(al, k)
    else:
        return al + findMinKlists(bl, k - len(al))


ls = [4, 5, 1, 6, 2, 7, 3, 8]
print(findMinKlists(ls, 4))
