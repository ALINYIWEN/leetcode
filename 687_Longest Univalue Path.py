'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

687. Longest Univalue Path

Given the root of a binary tree, return the length of the longest path, 

where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: root = [5,4,5,1,1,5]
Output: 2

Input: root = [1,4,5,4,4,5]
Output: 2

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
  
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
           
if __name__ == '__main__':
    
    list = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.productExceptSelf(list))     
                    