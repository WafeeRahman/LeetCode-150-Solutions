# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Level Order Traversal, every RIGHTMOST node in each level is what we can
        #Observe when looking at the tree from the right
        #In other words, we need to construct a result arr with 
        #The last value of each level of the tree
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val) 
        return res   
            
                
