# -*- coding: utf-8 -*-

"""
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。
如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。
你必须输出所有学生中的已知的朋友圈总数。
"""


def friendsnum(grid):
    res = 0
    seen = set()

    def dfs(row):
        for col, val in enumerate(grid[row]):
            if val and col not in seen:
                seen.add(col)
                dfs(col)

    for i in range(len(grid)):
        if i not in seen:
            dfs(i)
            res += 1
    return res


fr = [[1,0,1],
      [0,1,1],
      [1,1,1]]
print(friendsnum(fr))

