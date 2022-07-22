# -*- coding: utf-8 -*-
"""
如何仅用递归函数和栈操作逆序一个栈
题目：
一个栈依次压入1，2，3，4，5，那么从栈顶到栈底分别为5，4，3，2，1。
将这个栈转置后，从栈顶到栈底为1，2，3，4，5，也就是实现栈中元素的逆序，
但是只能用递归函数来实现，不能用其他数据结构。
"""


class solutions:

    def GetElement(self, stack):
        res = stack.pop()
        if not stack:
            return res
        else:
            i = self.GetElement(stack)
            stack.append(res)
            return i

    def ReverseStack(self, stack):
        if not stack:
            return
        else:
            i = self.GetElement(stack)
            self.ReverseStack(stack)
            stack.append(i)


stack = [1, 2, 3, 4, 5]
solu = solutions()
solu.ReverseStack(stack)
print(stack)