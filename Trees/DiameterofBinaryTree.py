# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def dfs(root):
            nonlocal res
            if not root:
                return
            
            res = max(res, (self.maxDepth(root.left)+ self.maxDepth(root.right)))
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res
        
   
    def maxDepth(self, root):
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
