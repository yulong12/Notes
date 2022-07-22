# -*- coding: utf-8 -*-
"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
输入: [7,1,5,3,6,4]
输出: 5
"""


def maxProfit(lists):
    if not lists:
        return
    dp = [0] * len(lists)
    for i in range(1, len(lists)):
        dp[i] = max(dp[i-1], lists[i] - min(lists[:i]))
    return dp[-1]


prices = [7,1,5,3,6,4]
print(maxProfit(prices))



