# -*- coding: utf-8 -*-

"""
给定一个2维网格图，其中“1”(陆地)和“0”(水)，计算岛屿的数量
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
"""


def islandnums(grid):
    islandnum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                islandnum += 1
                dfs(grid, i, j)
    return islandnum


def dfs(grid, i, j):
    grid[i][j] = 0
    if i-1 >= 0 and grid[i-1][j] == 1:
        dfs(grid, i-1, j)
    if i+1 < len(grid) and grid[i+1][j] == 1:
        dfs(grid, i+1, j)
    if j-1 >= 0 and grid[i][j-1] == 1:
        dfs(grid, i, j-1)
    if j+1 < len(grid[0]) and grid[i][j+1] == 1:
        dfs(grid, i, j+1)


island = [[1,1,0,0,0],
          [1,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,1]]
# print(islandnums(island))


