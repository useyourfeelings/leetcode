# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []
            
        result = []
        nodes = [root]
        
        while len(nodes) != 0:
            node = nodes.pop()
            result.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        
        return result
