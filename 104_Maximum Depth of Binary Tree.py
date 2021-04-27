# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, tree_root):
        if not tree_root:
            return 0
        return max(self.maxDepth(tree_root.left), self.maxDepth(tree_root.right)) + 1


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(2)

s = Solution()
answer = s.maxDepth(node)
print(answer)