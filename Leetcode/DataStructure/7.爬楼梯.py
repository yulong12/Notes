# -*- coding: utf-8 -*-
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

def climbStairs(n):
    # 爬楼梯
    if n < 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    pre_one, pre_two = 1, 2
    for i in range(3, n+1):
        result = pre_one + pre_two
        pre_one = pre_two
        pre_two = result
    return result


print(climbStairs(4))

