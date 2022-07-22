# -*- coding: utf-8 -*-

"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点的值相加等于目标和
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sums):
    if not root: return False
    sums -= root.val
    if not root.left and not root.right and sums == 0: return True
    left = hasPathSum(root.left, sums)
    right = hasPathSum(root.right, sums)
    return left or right



