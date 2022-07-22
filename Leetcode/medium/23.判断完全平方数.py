# -*- coding: utf-8 -*-

"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
"""


"""
任意一个完全平方数都可以表示成一组奇数序列的和
"""
def issqurtsss(ints):
    i = 1
    while ints > 0:
        ints -= i
        i += 2
    return ints == 0


print(issqurtsss(16))



