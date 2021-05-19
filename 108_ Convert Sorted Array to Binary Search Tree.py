# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(index_first, index_last):
            if index_first > index_last:
                return None

            index_mid = (index_first + index_last)//2  # 先找到root
            
            node = TreeNode(nums[index_mid]) # 建立中間的root
            node.left = dfs(index_first, index_mid - 1)
            node.right = dfs(index_mid + 1, index_last)
            return node

        return dfs(0, len(nums)-1)