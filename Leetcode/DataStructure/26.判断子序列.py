# -*- coding: utf-8 -*-

"""
判断是否是子序列
input:  s="abc"   t="anhdblscds"
output: True
"""

def IsSubSequence(str1, str2):
    slow = 0
    for fast in range(len(str2)):
        if slow < len(str1) and str1[slow] == str2[fast]:
            slow += 1
    if slow == len(str1):
        return True
    else:
        return False


s1 = "abc"
s2 = "ahbgdc"
print(IsSubSequence(s1, s2))



