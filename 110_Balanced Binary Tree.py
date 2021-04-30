'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution_1:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root: TreeNode) -> int:
            if root == None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1+ max(left, right)
        return check(root)
    
if __name__ == '__main__':

    s1 = Solution_1()
    print(s1.isBalanced([1,2,4], [1,3,4]))  