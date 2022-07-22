# -*- coding: utf-8 -*-


"""
最长公共字串
"""


def longerStr(s1, s2):
    dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    maxx = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1] > maxx:
                    maxx = dp[i+1][j+1]
                    p += i
    return s1[p-maxx:p], maxx


print(longerStr('abcdef', 'ssabcef'))


