# -*- coding: utf-8 -*-

"""
八皇后问题
"""

def solvequeens(n):
    res = []
    line = "." * n

    def backstrack(i, tmp, x, y, z):
        if i == n:
            res.append(tmp)
            return
        for j in range(n):
            if x and y and z and (j in x or i+j in y or i-j in z):
                continue
            backstrack(i+1, tmp+[line[:j]+"Q"+line[j+1:]], x+[j], y+[i+j], z+[i-j])
    backstrack(0, [], [], [], [])
    return res


print(solvequeens(4))

