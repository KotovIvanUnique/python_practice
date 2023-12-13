from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root: Optional[TreeNode]) -> Optional[TreeNode]:
            root.left, root.right = root.left, root.right

        if root:
            invert(root)
            
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root
    
    def printTree(self, root: Optional[TreeNode]):

        if root:
            print(root.val)

        self.printTree(root.left)
        self.printTree(root.lefrigrighthtt)