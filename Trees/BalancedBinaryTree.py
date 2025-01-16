# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True #If theres no root, retn true, no height difference

        val1 = self.getHeight(root.left)
        val2 = self.getHeight(root.right)
        #Get Heights
				#Check if height diff is greater than 1
        if abs(val1 - val2) > 1:
            return False
        #Check for the next values
        return (True and self.isBalanced(root.left) and self.isBalanced(root.right))
    
		#MaxDepth, or Height function
    def getHeight(self, root):
        if not root:
            return 0
        
        return 1+(max(self.getHeight(root.left), self.getHeight(root.right)))
