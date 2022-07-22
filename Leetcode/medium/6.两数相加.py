# -*- coding: utf-8 -*-

"""
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def allTwoNumbers(lista, listb):

    carry = 0
    list3 = ListNode(None)
    head = list3
    while lista is not None or listb is not None or carry > 0:
        total = carry
        if lista is not None:
            total += lista.val
            lista = lista.next

        if listb is not None:
            total += listb.val
            listb = listb.next

        node = ListNode(total % 10)
        list3.next = node
        list3 = list3.next
        carry = total // 10
    return head.next


a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
a.next = b
b.next = c

d = ListNode(7)
e = ListNode(6)
f = ListNode(0)
d.next = e
e.next = f


# res = allTwoNumbers(a, d)
# while res:
#     result = res.val
#     res = res.next
#     print(result)




