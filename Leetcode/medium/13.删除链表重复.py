# -*- coding: utf-8 -*-

"""
删除链表中重复的元素
"""


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def removedupval(head):
    if not head:
        return head
    p = head
    q = head.next
    while q:
        if p.val == q.val:
            p.next = q.next
            q = q.next
        else:
            p = p.next
            q = q.next
    return head


a = ListNode(4)
b = ListNode(4)
c = ListNode(1)
d = ListNode(1)
a.next = b
b.next = c
c.next = d

print(removedupval(a).next.val)



