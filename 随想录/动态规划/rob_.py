"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        val1 = self.roblist(nums[1:])
        val2 = self.roblist(nums[:-1])
        return max(val1, val2)
    def roblist(self, nums):
        l = len(nums)
        dp = [0] * l
        dp[0] = nums[0]
        for i in range(1, l):
            if i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            else:
                dp[i] = max(dp[i -1], dp[i - 2] + nums[i])
        return dp[-1]