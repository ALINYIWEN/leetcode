'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 

which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Dynamic Programming
class Solution:
    def minPathSum(self, grid):
        
        row, column = len(grid), len(grid[0])  
            
        for i in range(1, row): # 先處理掉row[0]與column[0]
            grid[i][0] = grid[i][0] + grid[i-1][0]  # 初始化
        for j in range(1, column):
            grid[0][j] = grid[0][j] + grid[0][j-1]
        
        for i in range(1, row):          # 1 已經不用做了
            for j in range(1, column):
               grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
               
        return grid[-1][-1]
           
if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    print(s.minPathSum(grid))     
  