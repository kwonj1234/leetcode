
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My solution
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if root is None:
#             return None
        
#         root.right = self.flatten(root.right)
#         root.left = self.flatten(root.left)

#         if root.left is not None:
#             node = root.left
#             temp_node = root.left
#             while temp_node.right is not None:
#                 temp_node = temp_node.right
#             temp_node.right = root.right

#             root.right = node
#             root.left = None

#         return root

# Better solution. Keep track of the previous linked list.
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)  # Recursively flatten the right subtree
        self.flatten(root.left)  # Recursively flatten the left subtree
        root.right = self.prev  # Set the right child to the previously flattened node
        root.left = None  # Set the left child to None
        self.prev = root  # Update the previously flattened node to be the current node