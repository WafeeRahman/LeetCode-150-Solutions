# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #Use an array to store each value and null node in preorder traversal
        res = []

        def dfs(root):
            nonlocal res
            if not root:
                #Mark child as null
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        
        #Build Res
        dfs(root)

        #Stringify Data
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preOrder = data.split(",")
      #Use a global variable to traverse the preorder traversal
      #So that the current index is preserved between recursive calls
      preIndex = 0
        def dfs():
            nonlocal preIndex
            if preOrder[preIndex] == "N":
                preIndex+=1
                return None

            node = TreeNode(int(preOrder[preIndex]))
            #Move to next node
            preIndex+=1
            #Set each left child in preorder traversal
            node.left  = dfs()
            #Return Calls from the left subtree will bring us back to build the left subtree
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
