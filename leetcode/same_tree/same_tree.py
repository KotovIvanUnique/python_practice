from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        def dive(node: Optional[TreeNode], vals: set):
            if not node:
                vals.append(None)
                return
            vals.append(node.val)
            dive(node.left, vals)
            dive(node.right, vals)

        p_vals = []
        p_vals.append(p.val)
        dive(p.left, p_vals)
        dive(p.right, p_vals)

        q_vals = []
        q_vals.append(q.val)
        dive(q.left, q_vals)
        dive(q.right, q_vals)

        return p_vals == q_vals