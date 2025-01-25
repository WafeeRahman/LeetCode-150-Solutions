# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathS = float("-inf")
        def dfs(root):
            nonlocal maxPathS 
            if not root:
                return 0
            #Get the pathSums of the left and right
            #Since negative values are possible, overwrite any negative values
            #With zeros, as we dont need to include the left or right in the path
            pathSumLeft = max(dfs(root.left), 0)
            pathSumRight = max(dfs(root.right), 0)
            
            #Get The Current Path Sum between the root and its left and right subtrees
            #As all nodes are adj by one edge
            currentPathSumTripleSum = root.val + pathSumLeft + pathSumRight
            #Take the Max
            maxPathS = max(maxPathS, currentPathSumTripleSum)
            
            #Return up the greatest sum possible between the root and left and right subtree
            return root.val + max(pathSumLeft, pathSumRight)
        dfs(root)
        return maxPathS

            
        
