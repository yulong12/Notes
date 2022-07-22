# -*- coding: utf-8 -*-

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, a, b):
        if a == None or b == None:
            return False
        return self.dfs(a, b) or self.dfs(a.left, b) or self.dfs(a.right, b)

    def dfs(self, a, b):
        if a == None:
            return False
        if b is None:
            return True
        return a.val == b.val and self.dfs(a.left, b.left) and self.dfs(a.right, b.right)