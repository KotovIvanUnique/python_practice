from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = {1}

        if not root:
            return 0
        
        counter = 1

        def dive(node: Optional[TreeNode], counter):
            if not node:
                return 0
            new_counter = counter + 1
            depths.add(new_counter)
            dive(node.left, new_counter)
            dive(node.right, new_counter)

        dive(root.left, counter)
        dive(root.right, counter)

        return max(depths)