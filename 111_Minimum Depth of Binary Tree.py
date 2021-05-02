'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
       

import collections
from typing import Collection

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])    # 初始化一個queue 用deue實作, 並給他一個list做初始化
        while queue:
            n, d = queue.popleft()                # 節點n, 與深度d
            if n:                                 # 若有東西才做
                if not n.left and not n.right:       # 若n是葉節點, 就回傳深度
                    return d
                else:
                    queue.append((n.left, d + 1))
                    queue.append((n.right, d + 1))
                      
if __name__ == '__main__':
    
    list = [2,None,3,None,4,None,5,None,6]
    s = Solution()
    print(s.minDepth(list))     
                    