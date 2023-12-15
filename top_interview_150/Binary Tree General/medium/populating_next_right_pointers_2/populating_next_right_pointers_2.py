"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
            
        def bfs_connect(children):
            if not children:
                return

            next_row = []
            for i, child in enumerate(children):
                if child.left:
                    next_row.append(child.left)
                if child.right:
                    next_row.append(child.right)

                if i == len(children) - 1:
                    break
                child.next = children[i+1]
            
            bfs_connect(next_row)

        bfs_connect([root])

        return root