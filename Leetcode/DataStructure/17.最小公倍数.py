# -*- coding: utf-8 -*-


def mingongbeishu(a, b):
    if a > b:
        res = a
    else:
        res = b
    while(True):
        if(res % a == 0) and (res % b == 0):
            break
        res += 1
    return res


print(mingongbeishu(4, 3))

def maxgongyueshu(a, b):
    if a > b:
        res = b
    else:
        res = a
    while(True):
        if (a % res == 0) and (b % res == 0):
            break
        res -= 1
    return res


print(maxgongyueshu(6, 8))


