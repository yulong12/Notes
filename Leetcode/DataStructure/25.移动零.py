# -*- coding: utf-8 -*-

"""
移动零
input: [0,1,0,3,12]
output:[1,3,12,0,0]
"""

def movezeros(lists):
    if len(lists) == 0:
        return
    slow = 0
    for fast in range(len(lists)):
        if lists[fast] != 0:
            lists[slow], lists[fast] = lists[fast], lists[slow]
            slow += 1
    return lists


ls = [2, 0, 1, 0, 3, 12]
# print(movezeros(ls))


