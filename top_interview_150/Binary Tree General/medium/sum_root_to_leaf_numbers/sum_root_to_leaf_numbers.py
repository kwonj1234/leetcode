class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_leaves = 0

        def find_leaf_numbers(node, current_val):
            new_val = (current_val * 10) + node.val
            if node.left is None and node.right is None:
                sum_leaves += new_val
            if node.left is not None:
                find_leaf_numbers(node.left, new_val)
            if node.right is not None:
                find_leaf_numbers(node.right, new_val)
        
        find_leaf_numbers(root, 0)

        return sum_leaves