# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currentSum=0) -> bool:
        if root is None:
            return False

        currentSum += root.val
        if currentSum == targetSum and root.left is None and root.right is None:
            return True
        
        left = False
        right = False
        if root.left is not None:
            left = self.hasPathSum(root.left, targetSum, currentSum)
        if root.right is not None:
            right = self.hasPathSum(root.right, targetSum, currentSum)

        return left or right