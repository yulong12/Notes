class LeetCode(object):
    def finSubStrNoRepeat(str):
        '''
        给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度
        例子1:
            输入: s = "abcabcbb"
            输出: 3 
            解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3
        例子2:
            输入: s = "bbbbb"
            输出: 1
            解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
        例子3:
            输入: s = "pwwkew"
            输出: 3
            解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
                请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
        '''
        n=len(str)
        rk,ans=-1,0
        subSet=set()
        for i in range (n):
            if i!=0:
                subSet.remove(str[i-1])
            while rk+1<n and str[rk+1] not in subSet:
                subSet.add(str[rk+1])
                rk+=1
            ans=max(ans,len(subSet))
        return ans

x=LeetCode
print(x.finSubStrNoRepeat("abcabcbb"))