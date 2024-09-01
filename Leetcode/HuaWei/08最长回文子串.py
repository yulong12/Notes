'''
给你一个字符串 s,找到 s 中最长的回文子串
示例 1:
输入:s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2:
输入:s = "cbbd"
输出："bb"
回文子串：子串从后往前读和从前往后读一样
'''

class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

s = "babad"
x=Solution()
print(x.longestPalindrome(s))

'''
Solution:
我们枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长回文串长度。
我们对所有的长度求出最大值，即可得到最终的答案。

'''