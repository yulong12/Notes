# -*- coding: utf-8 -*-

"""
判断一个链表中是否有环
"""

class NodeList:
    def __init__(self,x):
        self.val = x
        self.next = None


def judgelianbiao(head):

    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


