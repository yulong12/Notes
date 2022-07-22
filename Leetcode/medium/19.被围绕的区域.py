# -*- coding: utf-8 -*-

"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
"""


def xxoo(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1) and (grid[i][j] == "o"):
                dfs(grid, i, j)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = "o" if grid[i][j] == "T" else "x"
    return grid


def dfs(grid, x, y):
    grid[x][y] = "T"
    if x-1 >= 0 and grid[x-1][y] == "o":
        dfs(grid, x-1, y)
    if x+1 < len(grid) and grid[x+1][y] == "o":
        dfs(grid, x+1, y)
    if y-1 >= 0 and grid[x][y-1] == "o":
        dfs(grid, x, y-1)
    if y+1 < len(grid) and grid[x][y+1] == "o":
        dfs(grid, x, y+1)


island = [["x","x","x","x"],
          ["x","o","o","x"],
          ["x","x","o","x"],
          ["x","o","x","x"]]
# print(xxoo(island))


