# -*- coding: utf-8 -*-

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) – 将元素 x 推入栈中。
pop() – 删除栈顶的元素。
top() – 获取栈顶元素。
getMin() – 检索栈中的最小元素。
"""


class MinStrack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x):
        if x is None:
            pass
        else:
            self.stack.append(x)
        if self.min is None or self.min > x:
            self.min = x

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            del(self.stack[-1])
        if len(self.stack) > 0 and self.min >= min(self.stack):
            self.min = min(self.stack)

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        return self.min


# stack = MinStrack()
# stack.push(a)
# print(stack.min)

