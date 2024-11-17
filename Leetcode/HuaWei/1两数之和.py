from collections import defaultdict  
def twoSum(list,target):
    dic={}
    for j,x in enumerate(list):
        if target-x in dic:
            return [dic[target-x],j]
        dic[x]=j
def numIdenticalPairs(list):
    dic=defaultdict(int)
    ans=0
    for x in list:
        ans+=dic[x]
        dic[x]+=1
    return ans
# list=[2,7,11,15]
# print(twoSum(list,9))
def containsNearbyDuplicate(list,k):
    dic={}
    for j,x in enumerate(list):
        if x in dic and abs(dic[x]-j)<=k:
            return True
        dic[x]=j
    return False
# nums = [1,2,3,1]
# k = 3
# print(containsNearbyDuplicate(nums,k))
def maxProfit(list):
    max_price=0
    min_price=list[0]
    for x in list:
        max_price=max(max_price,x-min_price)
        min_price=min(min_price,x)
    return max_price
price=[7,1,5,3,6,4]
print(maxProfit(price))