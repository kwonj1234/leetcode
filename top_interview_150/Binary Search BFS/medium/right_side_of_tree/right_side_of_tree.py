# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        bfs = [root]

        while bfs:
            ans.append(bfs[-1].val)
            children = []
            for node in bfs:
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)

            bfs = children
        
        return ans
