# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {val: i for i, val in enumerate(inorder)}

        def partition(postorder, start, end):
            if not postorder or start < 0 or end > len(inorder):
                return None

            val = postorder[-1]
            i = val_to_index[val]
            if i < start or i > end:
                return None
            
            postorder.pop()
            node = TreeNode(val=val)
            node.right = partition(postorder, i+1, end)
            node.left = partition(postorder, start, i-1)

            return node

        return partition(postorder, 0, len(inorder))