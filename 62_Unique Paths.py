'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 

The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Input: m = 7, n = 3
Output: 28

Input: m = 3, n = 3
Output: 6

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Dynamic Programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(n)] for j in range(m)] # 建立一個空的二維陣列 : n個0的陣列, 重複m次
        
        for i in range(m):
            dp[i][0] = 1    # 初始化最左邊的值 = 1
        for j in range(n):
            dp[0][j] = 1    # 初始化最上面的值 = 1
        
        for i in range(1, m):          # 1 已經不用做了
            for j in range(1, n):
               dp[i][j] = dp[i-1][j] + dp[i][j-1]     # 每一格都是左邊一格跟上面一格來的
               
        return dp[-1][-1]    # 回傳最後一格 也可以 dp[m-1][n-1]   
            
        
if __name__ == '__main__':

    s = Solution()
    print(s.uniquePaths(7, 3))     
  