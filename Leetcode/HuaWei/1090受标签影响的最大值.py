'''
以两个整数数组  values 和 labels 给定 n 个项的值和标签,并且给出两个整数 numWanted 和 useLimit 。

你的任务是从这些项中找到一个值的和 最大 的子集使得:

    项的数量 最多 为 numWanted。
    相同标签的项的数量 最多 为 useLimit。

返回最大的和。

示例 1:

输入:values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1

输出:9

解释:

选择的子集是第一个、第三个和第五个项,其值之和为 5 + 3 + 1。

示例 2:

输入:values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2

输出:12

解释:

选择的子集是第一个、第二个和第三个项,其值之和为 5 + 4 + 3。

示例 3:

输入:values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1

输出:16

解释:

选择的子集是第一个和第四个项,其值之和为 9 + 7。


'''

'''
方法一:贪心 + 排序 + 哈希表

根据题目描述,我们需要从 n 个元素的集合中选出一个子集,子集元素个数不超过 numWanted,且子集中最多有相同标签的 useLimit 项,使得子集的值之和最大。
因此,我们应该贪心地选择集合中值较大的元素,同时记录每个标签出现的次数,当某个标签出现的次数达到 useLimit 时,我们就不能再选择该标签对应的元素了。
具体地,我们先将集合中的元素按照值从大到小进行排序,然后从前往后遍历排序后的元素。
在遍历的过程中,我们使用一个哈希表 cnt 记录每个标签出现的次数,如果某个标签出现的次数达到了 useLimit,那么我们就跳过该元素,
否则我们就将该元素的值加到最终的答案中,并将该标签出现的次数加 1。
同时,我们用一个变量 num 记录当前子集中的元素个数,当 num 达到 numWanted 时,我们就可以结束遍历了。

遍历结束后,我们就得到了最大的分数。


'''

from collections import Counter


class Solution:

    def largestValsFromLabels(

        self, values, labels, numWanted, useLimit):

        ans = num = 0

        cnt = Counter()

        for v, l in sorted(zip(values, labels), reverse=True):

            if cnt[l] < useLimit:

                cnt[l] += 1

                num += 1

                ans += v

                if num == numWanted:

                    break

        return ans

x=Solution()
values = [9,8,8,7,6]
labels = [0,0,0,1,1]
numWanted = 3
useLimit = 1
ans=x.largestValsFromLabels(values,labels,numWanted,useLimit)
print(ans)