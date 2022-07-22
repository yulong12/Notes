# -*- coding: utf-8 -*-

"""
字符串匹配
"""
def StringMatching(str, substr):
    for i in range(len(str)-len(substr)+1):
        index = i
        for j in range(len(substr)):
            if str[index] == substr[j]:
                index += 1
        if index - i == len(substr):
            return i
    return "-1"


a = "abefcdefghijklmn"
b = "efgh"
print(StringMatching(a, b))



