# -*- coding: utf-8 -*-


def huiwenshu(x):
    if x < 0:
        return False
    s = ""
    for i in str(x):
        s = i + s
    print(s)

# huiwenshu(12345)

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    res, tmp = 0, x
    while tmp > 0:
        res = 10 * res + tmp % 10
        tmp = tmp // 10
    if res == x:
        return True
    else:
        return False


print(isPalindrome(-10))


