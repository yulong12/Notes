# -*- coding: utf-8 -*-

"""
编写函数 从左至右遍历二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

"""
递归
"""
def leveltravel(root, depth):
    res = []
    if root is None:
        return
    if len(res) == depth:
        res.append([])
    res[depth].append(root.value)
    leveltravel(root.left, depth+1)
    leveltravel(root.right, depth+1)
    return res


"""
非递归
"""
def leveltravels(root):
    res, layer = [], [root]
    while layer:
        cur = []
        next_layer = []
        for node in layer:
            cur.append(node.value)
            if node.left: next_layer.append(node.left)
            if node.right: next_layer.append(node.right)
        res.append(cur)
        layer = next_layer
    return res


