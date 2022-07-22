# -*- coding: utf-8 -*-

"""
编写一个函数查找字符串数组中的最长公共前缀
input = ["flower", "flow", "flight"]
output: "fl
"""


def longestCommonPrefix(s):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not s:
        return ""
    res = s[0]
    i = 1
    while i < len(s):
        while res not in s[i]:
            res = res[0:len(res) - 1]
        i += 1
    return res


ls = ["flower", "flow", "flowight"]
# ls = ["cl", "cl"]
print(longestCommonPrefix(ls))

