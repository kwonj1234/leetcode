# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return False
        
        left_descendant = self.lowestCommonAncestor(root.left, p, q)
        right_descendant = self.lowestCommonAncestor(root.right, p, q)

        if type(left_descendant) is TreeNode:
            return left_descendant
        elif type(right_descendant) is TreeNode:
            return right_descendant

        if left_descendant is True and right_descendant is True:
            return root
        elif left_descendant is True and (root == p or root == q):
            return root
        elif right_descendant is True and (root == p or root == q):
            return root

        if root == p or root == q:
            return True
        elif left_descendant is True or right_descendant is True:
            return True

        return False