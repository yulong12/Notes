# -*- coding: utf-8 -*-
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def FindTreeCommon(root, a, b):
    if not root or root == a or root == b:
        return root
    left = FindTreeCommon(root.left, a, b)
    right = FindTreeCommon(root.right, a, b)
    if not left: return right
    if not right: return left
    return root
