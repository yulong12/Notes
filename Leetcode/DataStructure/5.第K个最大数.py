# -*- coding: utf-8 -*-

"""
查找第K个最大的数
"""

def findk(lists, k):
    if not lists: return
    n = len(lists)
    key = round(n / 2)
    al = [i for i in lists[:key] + lists[key + 1:] if i < lists[key]]
    bl = [i for i in lists[:key] + lists[key + 1:] if i >= lists[key]]
    if len(bl) == k:
        return key
    elif len(bl) > k:
        findk(bl, k)
    else:
        findk(al, k - len(bl))


ll = [1, 8, 4, 5, 2, 3, 9]
print(findk(ll, 3))

