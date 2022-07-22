# -*- coding: utf-8 -*-

"""
四数之和
input:  [1, 0, -1, 0, -2, 2] target:0
output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""


def fourcombines(lists, target):
    lists.sort()
    res = []
    n = len(lists)
    for i in range(n-3):
        if i > 0 and lists[i] == lists[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and lists[j] == lists[j-1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                sums = lists[i] + lists[j] + lists[left] + lists[right]
                if sums == target:
                    res.append([lists[i], lists[j], lists[left], lists[right]])
                    left +=1
                    right -=1
                    while left < right and lists[left] == lists[left-1]:
                        left += 1
                    while left < right and lists[right] == lists[right+1]:
                        right -= 1
                elif sums > target:
                    right -= 1
                else:
                    left += 1
    return res


l1 = [1, 0, -1, 0, -2, 2]
tt = 0
print(fourcombines(l1, tt))
