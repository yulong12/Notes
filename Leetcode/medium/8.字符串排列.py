# -*- coding: utf-8 -*-


"""
字符串排列，一个字符串 有多少种排列方式
"""

def StrArray(s):
    if len(s) == 0: return
    strs = list(s)
    res = []

    def backtrack(strs, tmp):
        if not strs:
            res.append("".join(tmp))
        for i in range(len(strs)):
            if i > 0 and strs[i] == strs[i-1]:
                continue
            backtrack(strs[:i]+strs[i+1:], tmp+[strs[i]])

    backtrack(strs, [])
    return res


print(StrArray("abc"))

"""
全排列
"""
def allpailie(lists):
    res = []

    def backtrack(lists, tmp):
        if len(lists) == 0:
            res.append(tmp)
        for i in range(len(lists)):
            backtrack(lists[:i]+lists[i+1:], tmp+[lists[i]])
    backtrack(lists, [])
    return res


ll = [1,3,5]
print(allpailie(ll))

