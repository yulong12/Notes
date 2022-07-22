# -*- coding: utf-8 -*-


# def BinarySearch(lists, target):
#     left = 0
#     right = len(lists) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if lists[mid] == target:
#             return mid
#         elif lists[mid] < target:
#             left = mid + 1
#         elif lists[mid] > target:
#             right = mid - 1
#         else:
#             return "-1"


# sqort_list = [1, 2, 3, 6, 7, 9, 10]
# print(BinarySearch(sqort_list, 9))

#
def serach(ls, left, right, target):
    mid = (left + right) // 2
    if left > right:
        return "-1"
    if target == ls[mid]:
        return mid
    elif target > ls[mid]:
        left = mid + 1
    elif target < ls[mid]:
        right = mid - 1
    else:
        return "-1"
    return serach(ls, left, right, target)


ll = [1, 2, 3, 5, 6, 8]
print(serach(ll, 0, len(ll)-1, 5))

