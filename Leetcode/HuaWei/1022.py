class Demo(object):
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
        ans,rk=0,-1
        n=len(str)
        occ=set()
        for i in range(n):
            if i!=0:
                occ.remove(str[i-1])
            while rk+1<n and str[rk+1] not in occ:
                occ.add(str[rk+1])
                rk+=1
            ans=max(ans,rk-i+1)
        return ans
    def lengthOfLongestSubstringTwoDistinct(str):
        '''
        给你一个字符串 s ，请你找出至多包含两个不同字符的最长子串，并返回该子串的长度。
        示例：
        示例 1:
        输入:s = "eceba"
        输出:3
        解释：满足题目要求的子串是 "ece" ，长度为 3 。
        示例 2:
        输入:s = "ccaabbb"
        输出:5
        解释：满足题目要求的子串是 "aabbb" ，长度为 5 。
        '''
        n=len(str)
        if n<3:
            return n
        hashmap={}
        max_size=2
        left,right=0,0
        while right<n:
            hashmap[str[right]]=right
            right+=1
            if len(hashmap)==3:
                del_index=min(hashmap.values())
                del hashmap[str[del_index]]
                left=del_index+1
            max_size=max(max_size,right-left)
        return max_size
            
            
        

x=Demo
print(x.finSubStrNoRepeat("abcabcbb"))
print(x.lengthOfLongestSubstringTwoDistinct("eceba"))
    