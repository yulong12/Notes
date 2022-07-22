# -*- coding: utf-8 -*-

"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
"""


def mindepthTree(root):
    if not root: return 0
    queen = [(1, root)]
    while queen:
        depth, node = queen.pop(0)
        if not node.left and not node.right:
            return depth
        if node.left:
            queen.append((depth + 1, node.left))
        if node.right:
            queen.append((depth + 1, node.right))



