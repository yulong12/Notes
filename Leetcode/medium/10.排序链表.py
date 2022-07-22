# -*- coding: utf-8 -*-


"""
链表排序: 归并
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def lianbiaosort(Nodelist):
    if not Nodelist or not Nodelist.next:
        return Nodelist
    slow = Nodelist
    fast = Nodelist
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = lianbiaosort(Nodelist)
    right = lianbiaosort(mid)
    return merge(left, right)


def merge(left, right):
    res = ListNode(0)
    p = res
    l = left
    r = right
    while l and r:
        if l.val < r.val:
            p.next = l
            l = l.next
            p = p.next
        else:
            p.next = r
            r = r.next
            p = p.next
    if l:
        p.next = l
    if r:
        p.next = r
    return res.next


a = ListNode(4)
b = ListNode(8)
c = ListNode(1)
a.next = b
b.next = c


# print(lianbiaosort(a).val)



