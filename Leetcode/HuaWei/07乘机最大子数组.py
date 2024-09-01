'''
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续
子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

'''
class Solution(object):
    def maxProduct(self, nums):
        size = len(nums)
        if size == 1:
            return nums[0]
        maxRes = curMax = curMin = nums[0]
        for i in range(1, size):
            if nums[i] < 0:
                curMax, curMin = curMin, curMax
            curMax = max(curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], nums[i])
            maxRes = max(maxRes, curMax)
        return maxRes

x=Solution()
numbes=[2,3,-2,4,6,2]
print(x.maxProduct(numbes))