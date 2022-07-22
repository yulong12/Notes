# -*- coding: utf-8 -*-

"""
合并两个二叉树的数值
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
"""


class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


def MergeTree(t1, t2):
    if t1 and not t2:
        return t1
    if t2 and not t1:
        return t2
    if t1 and t2:
        t1.val += t2.val
        t1.left = MergeTree(t1.left, t2.left)
        t1.right = MergeTree(t1.right, t2.right)
    return t1




