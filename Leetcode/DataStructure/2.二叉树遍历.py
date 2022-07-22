# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    '''
    前序遍历
    '''
    if root == None:
        return None
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)



def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return None
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return None
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


root = TreeNode("A",TreeNode("D",TreeNode("ld"),TreeNode("rd")), TreeNode("E",TreeNode("le"),TreeNode("re")))

# preTraverse(root)
# midTraverse(root)
afterTraverse(root)

"""
非递归
"""

def preorder(root):
    track = []
    while track or root:
        while root:
            print(root.value)
            track.append(root)
            root = root.left
        root = track.pop()
        root = root.right


# preorder(root)
def midorder(root):
    track = []
    while track or root:
        while root:
            track.append(root)
            root = root.left
        root = track.pop()
        print(root.value)
        root = root.right

# midorder(root)


def postorder(root):
    track = []
    while track or root:
        while root:
            track.append(root)
            root = root.left if root.left else root.right
        root = track.pop()
        print(root.value)
        if track and track[-1].left == root:
            root = track[-1].right
        else:
            root = None



