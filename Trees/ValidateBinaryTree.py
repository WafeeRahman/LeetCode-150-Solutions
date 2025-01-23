# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lower, upper):
            #If theres no root, return True, as empty trees are 
            #BSTS
            if not root:
                return True
            
            #For each subtree, there is a lower and upper limit
            if not (lower < root.val < upper):
                return False
            
            #For the left, the upper limit is the current root
            #The Lower is -infinity, as items can be as low as they can get

            #For the right, the upper limit is the current root
            #The upper limit is +infinity, as items can get as high as infinity
            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
        
        return dfs(root, float('-inf'), float('inf'))
        
