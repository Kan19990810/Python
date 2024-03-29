"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1： 输入： 2 输出： 2 解释： 有两种方法可以爬到楼顶。

1 阶 + 1 阶
2 阶
示例 2： 输入： 3 输出： 3 解释： 有三种方法可以爬到楼顶。

1 阶 + 1 阶 + 1 阶
1 阶 + 2 阶
2 阶 + 1 阶
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        m = 2
        for j in range(n + 1):
            for step in range(1, m + 1):
                 if j >= step:
                     dp[j] += dp[j - step]
        return dp[n]