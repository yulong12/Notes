# -*- coding: utf-8 -*-

"""
三数之和
"""

def threesum(lists, target):
    lists.sort()
    result_list = []
    for i in range(len(lists)-2):
        if i > 0 and lists[i] == lists[i-1]:
            continue
        left = i + 1
        right = len(lists) - 1
        first = lists[i]
        while left < right:
            second = lists[left]
            third = lists[right]
            sum = first + second + third
            if sum == target:
                result_list.append([first, lists[left], lists[right]])
                left += 1
                while left < right and lists[left] == lists[left-1]:
                    left += 1
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
    return result_list


ll = [-1, -8, 4, 5, 3, -3, 9]
print(threesum(ll, -1))





