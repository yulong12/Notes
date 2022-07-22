# -*- coding: utf-8 -*-


"""
求一个二叉树的最大深度
"""


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def TreeDeep(root):
    if not root:
        return 0
    else:
        max(TreeDeep(root.left)+1, TreeDeep(root.right)+1)



