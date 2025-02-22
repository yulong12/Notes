'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sortFunc(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))
        def merge(head1, head2):
                    dummyHead = ListNode(0)
                    temp, temp1, temp2 = dummyHead, head1, head2
                    while temp1 and temp2:
                        if temp1.val <= temp2.val:
                            temp.next = temp1
                            temp1 = temp1.next
                        else:
                            temp.next = temp2
                            temp2 = temp2.next
                        temp = temp.next
                    if temp1:
                        temp.next = temp1
                    elif temp2:
                        temp.next = temp2
                    return dummyHead.next
        return sortFunc(head, None)
    
head = [-1,5,3,4,0]
x=Solution
# x.sortList(head)
x.sortList(head)