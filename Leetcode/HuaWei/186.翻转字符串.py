'''
给你一个字符数组 s ，反转其中 单词 的顺序。

单词 的定义为：单词是一个由非空格字符组成的序列。s 中的单词将会由单个空格分隔。

必须设计并实现 原地 解法来解决此问题，即不分配额外的空间。

 

示例 1：

输入：s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出：["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

示例 2：

输入：s = ["a"]
输出：["a"]

'''

class Solution:
    def __init__(self,s) -> None:
        self.s=s
    def reverseWords(self, s):
        """
        Do not return anything, modify str in-place instead.
        """
        i = 0
        for j in range(len(s)): # aT bT c
            if s[j] != ' ': continue
            self.reverse(s, i, j)
            i = j + 1
        self.reverse(s, i, len(s)) # aT bT cT
        self.reverse(s, 0, len(s)) # c b a
        return s
    def reverse(self, s, i, j):
        l, r = i, j - 1  # 因为j对应的是空格字符的索引，要往前推一位
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == "__main__":
        s=["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        x=Solution(s)
        s1=x.reverseWords(s)
        print(s1)