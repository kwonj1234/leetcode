# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            elif left_node is None \
                or right_node is None \
                or left_node.val != right_node.val:
                return False
            return symmetry(left_node.left, right_node.right) \
                and symmetry(left_node.right, right_node.left)

        return symmetry(root.left, root.right)