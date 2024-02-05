# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root is None:
            return ans

        level = [root]

        while level:
            temp = []
            new_level = []
            for node in level:
                temp.append(node.val)
                
                for child in [node.left, node.right]:
                    if child is not None:
                        new_level.append(child)
            ans.append(temp)
            level = new_level
        
        return ans