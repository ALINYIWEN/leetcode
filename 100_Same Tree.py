'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution_1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:   # 先確認若兩棵樹都不存在 , 則回傳true
            return True
        if not p or not q:
            return False      # 若其中之一不存在, 則回傳False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # 遞迴判斷下去
    
if __name__ == '__main__':

    s1 = Solution_1()
    print(s1.isSameTree([1,2,4], [1,3,4]))  