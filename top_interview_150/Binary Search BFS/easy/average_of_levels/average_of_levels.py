# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        ans = []
        bfs = [root]
        while bfs:
            children = []
            avg = 0

            for node in bfs:
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
                avg += node.val
            
            ans.append(round(avg/len(bfs), 5))
            bfs = children
        
        return ans