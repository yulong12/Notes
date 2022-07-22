# -*- coding: utf-8 -*-

"""
链表反转
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    cur = head
    pre = None
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre


def reverseListV2(head):
    cur = head
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
a.next = b
b.next = c

# print(reverseListV2(a).val)



