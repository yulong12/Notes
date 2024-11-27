def findStr(str):
    # 输入: s = "abcabcbb"
    # 输出: 3 
    # 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    length=len(str)
    rk,ans=-1,0
    occ=set()
    for i in range(length):
        if i!=0:
            occ.remove(str[i-1])
        while rk+1<length and str[rk+1] not in occ:
            occ.add(str[rk+1])
            rk=rk+1
        ans=max(ans,len(occ))
    return ans
s="abcabcbb"
x=findStr(s)
print(x)

