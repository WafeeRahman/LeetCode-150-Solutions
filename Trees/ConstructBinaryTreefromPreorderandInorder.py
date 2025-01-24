# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        #Populate a hashmap with the 
        #Inorder values and their indexes
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        #Traverse the preorder array with a global index pointer
        i = 0
        def dfs(left, right):
            nonlocal i
            #If we're out of bounds, 
            #Or left > right, that tells us we're in the wrong subtree
            if i == len(inorder) or left > right:
                return
            
            #Preorder Node is the root node
            Node = TreeNode(preorder[i])
            #In inorder traversal, everything to the left of the
            #current node is in its left subtree, and all items to the right
            #are values of the right subtree
            mid = inorderMap[preorder[i]]
            
            #Increment Ith pointer to add the next value
            i+=1
            #The left subtree is all nodes from the beginning to the location
            #Of the root node in the inorder traversal
            Node.left = dfs(left, mid-1)

            #The right subtree is all nodes from the root node to the end of the
            #Inorder array
            Node.right = dfs(mid+1, right)

            #Return node to previous call
            return Node
        
        return dfs(0, len(inorder)-1)
            
            
        
