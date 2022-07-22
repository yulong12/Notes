# -*- coding: utf-8 -*-


def concatlist(a, b):
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            res.append(b[0])
            del b[0]
            if len(b) == 0:
                res.extend(a)
                break
        else:
            res.append(a[0])
            del a[0]
            if len(a) == 0:
                res.extend(b)
                break
    return res


# list1 = [1, 2, 3, 6, 9, 10, 102]
# list2 = [3, 5, 6, 7, 111]
# print(concatlist(list1, list2))


def mergeList(a, b):
    if not a or not b:
        yield from (a+b)
        return
    if a[0] <= b[0]:
        yield a[0]
        yield from mergeList(a[1:], b)

    else:
        yield b[0]
        yield from mergeList(a, b[1:])


list1 = [1, 2, 3, 6, 9]
list2 = [3, 5, 6, 7]
res = list(mergeList(list1, list2))
print(res)

def listslianjie(a, b):
    res = []
    def brack(a, b):
        if not a or not b:
            res.extend(a + b)
            return
        if a[0] < b[0]:
            res.append(a[0])
            brack(a[1:], b)
        else:
            res.append(b[0])
            brack(a, b[1:])
    brack(a, b)
    return res


print(listslianjie(list1, list2))



