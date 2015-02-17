# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        
        nodes = [root]
        depth = 1
        
        while True:
            new_nodes = []
            for node in nodes:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                    
            nodes = new_nodes
            depth += 1
