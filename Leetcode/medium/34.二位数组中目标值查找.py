# -*- coding: utf-8 -*-

"""
在一个 n * m 的二维数组中，
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def find_matrix_number(matrix, target):
    if not matrix: return
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        else:
            return True
    return False


matrix = [[0, 1, 2, 4],
          [1, 2, 3, 5],
          [2, 3, 5, 6],
          [5, 8, 9, 11]]
print(find_matrix_number(matrix, 5))


