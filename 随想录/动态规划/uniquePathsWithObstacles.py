"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        if dp[0][0] == 0:
            return 0
        for i in range(1, col):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]