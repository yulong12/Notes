# -*- coding: utf-8 -*-

"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。
"""


def sumNumbers(self, root):
    self.res = 0

    def helpers(root, tmp):
        if not root:
            return
        if not root.left and not root.right:
            self.res += int(tmp + str(root.val))
            return
        helpers(root.left, tmp + str(root.val))
        helpers(root.right, tmp + str(root.val))

    helpers(root, "")
    return self.res



