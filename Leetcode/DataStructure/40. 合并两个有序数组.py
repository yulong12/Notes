# -*- coding: utf-8 -*-

"""
88. 给你两个有序整数数组 nums1 和 nums2，
请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
"""


def mergess(nums1, m, nums2, n):

    res = nums1[:m]
    nums1 = []
    i = j = 0
    while i < m and j < n:
        if res[i] < nums2[j]:
            nums1.append(res[i])
            i += 1
        else:
            nums1.append(nums2[j])
            j += 1
    if i < m:
        nums1.extend(res[i:])
    if j < n:
        nums1.extend(nums2[j:])
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
print(mergess(nums1, 3, nums2, 3))