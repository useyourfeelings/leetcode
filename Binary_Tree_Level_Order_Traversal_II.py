# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result = []
        players = []
        if root:
            players.append(root)
        
        while len(players) != 0:
            result.insert(0, [])
            new_players = []
            for node in players:
                result[0].append(node.val)
                if node.left:
                    new_players.append(node.left)
                if node.right:
                    new_players.append(node.right)
        
            players = new_players
        return result
