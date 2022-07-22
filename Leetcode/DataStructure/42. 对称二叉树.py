# -*- coding: utf-8 -*-
"""
请实现一个函数，用来判断一棵二叉树是不是对称的。
如果一棵二叉树和它的镜像一样，那么它是对称的
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def IsSymmertric(root):

    def ispair(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return ispair(left.left, right.right) and ispair(left.right, right.left)
    return ispair(root.left, root.right) if root else True



