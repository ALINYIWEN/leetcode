'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Dynamic Programming
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1:  # 若第一格就有障礙物, 直接回傳0
            return 0
        m, n  = len(obstacleGrid), len(obstacleGrid[0])  # 取得二維陣列長寬
        dp = [[0]*n for _ in range(m)]                   # 產出空陣列
        dp[0][0] = 1                                     # 先初始化 第一格就是一種方法
        
        for i in range(m):    
            for j in range(n):
                if obstacleGrid[i][j] == 0:  # 若該格 非障礙物
                    if i - 1 >= 0:           # 確認是不是最左邊那排
                        dp[i][j] += dp[i-1][j]
                    if j - 1 >= 0:           # 確認是不是最上面那排
                        dp[i][j] += dp[i][j-1]    
   
               
        return dp[-1][-1]    # 回傳最後一格 也可以 dp[m-1][n-1]   
                 
if __name__ == '__main__':

    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))   