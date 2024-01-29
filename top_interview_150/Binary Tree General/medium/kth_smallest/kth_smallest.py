# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1 * k

        k = self.kthSmallest(root.left, k)
        if k < 0 and k == -1:
            return root.val
        elif k >= 0:
            return k

        return self.kthSmallest(root.right, abs(k) - 1)