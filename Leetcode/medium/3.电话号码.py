# -*- coding: utf-8 -*-

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dicnum = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

    def iters(digits):
        res = []
        if len(digits) == 0:
            return [""]
        i = int(digits[0])
        for s in dicnum[i]:
            tmp = iters(digits[1:])
            for k in tmp:
                res.append(s + k)
        return res
    rel = iters(digits)
    return rel


print(letterCombinations("23"))


def disnumbers(iters):
    dicnum = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    def pairs(iters):
        res = []
        if len(iters) == 0:
            return [""]
        i = int(iters[0])
        for vs in dicnum[i]:
            tmp = pairs(iters[1:])
            for k in tmp:
                res.append(vs+k)
        return res
    return pairs(iters)


print(disnumbers("23"))