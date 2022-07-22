# -*- coding: utf-8 -*-

"""
合并两个有序链表
"""

class NodeList:
    def __init__(self,x):
        self.val = x
        self.next = None


def combinelianbiao(ls1, ls2):
    head = NodeList(0)
    curlist = head
    while ls1 is not None and ls2 is not None:
        if ls1.val < ls2.val:
            head.next = ls1
            ls1 = ls1.next
        else:
            head.next = ls2
            ls2 = ls2.next
        head = head.next
    if ls1 is None:
        head.next = ls2
    if ls2 is None:
        head.next = ls1
    return curlist.next



