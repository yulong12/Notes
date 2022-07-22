# -*- coding: utf-8 -*-


"""
最长公共子序列
"""


def LCS(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    arr = []
    x, y = len2, len1

    while res[x][y] > 0:
        if res[x][y] == res[x-1][y]:
            x -= 1
        elif res[x][y] == res[x][y-1]:
            y -= 1
        else:
            x -= 1
            y -= 1
            arr.append(string2[x])
    return "".join(arr[::-1])


print(LCS("helloworld","hewoedld"))


