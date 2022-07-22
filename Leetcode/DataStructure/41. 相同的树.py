# -*- coding: utf-8 -*-
"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""


class Treenode:
    def __init__(self, root, left, right):
        self.val = root
        self.left = None
        self.right = None


def isSametree(l1, l2):

    def pretravel(root):
        if not root:
            return [None]
        else:
            return root.val + pretravel(root.left) + pretravel(root.right)
    return pretravel(l1) == pretravel(l2)

