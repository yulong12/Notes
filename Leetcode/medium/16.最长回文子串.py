# -*- coding: utf-8 -*-


"""
最长回文子串
"""


def maxsubhuiwenstr(strs):
    strlen = len(strs)
    maxlenth = 0
    start = 0
    for i in range(strlen):
        # 如果当前循环次数-当前最大长度大于等于1  并  字符串[当前循环次数-当前最大长度-1:当前循环次数+1]  == 取反后字符串
        if i - maxlenth >= 1 and strs[i-maxlenth-1: i+1] == strs[i-maxlenth-1: i+1][::-1]:
            start = i - maxlenth - 1
            # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
            maxlenth += 2
            continue
        # 如果当前循环次数-当前最大长度大于等于0  并  字符串[当前循环次数-当前最大长度:当前循环次数+1]  == 取反后字符串
        if i - maxlenth >= 0 and strs[i-maxlenth: i+1] == strs[i-maxlenth: i+1][::-1]:
            start = i - maxlenth
            # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
            maxlenth += 1
    return strs[start: start+maxlenth]


s = "babaddjdda"
print(maxsubhuiwenstr(s))


