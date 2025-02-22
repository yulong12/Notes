'''
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

示例 1:

输入：s = "egg", t = "add"
输出：true

示例 2：

输入：s = "foo", t = "bar"
输出：false

示例 3：

输入：s = "paper", t = "title"
输出：true

'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t,t2s={},{}
        for a,b in zip(s,t):
            
            if a in s2t and s2t[a]!=b or b in t2s and t2s[b]!=a:
                return False
            s2t[a],t2s[b]=b,a
        return True

x=Solution()
d = "egg"
y = "add"

print(x.isIsomorphic(d,y))