# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        sum = 0
        if not root:
            return sum
            
        nodes = [root]
        while len(nodes) != 0:
            new_nodes = []
            
            for node in nodes:
                if not node.left and not node.right:
                    sum += node.val
                else:
                    if node.left:
                        node.left.val = node.left.val + 10 * node.val
                        new_nodes.append(node.left)
                    if node.right:
                        node.right.val = node.right.val + 10 * node.val
                        new_nodes.append(node.right)
                        
            nodes = new_nodes
            
        return sum
