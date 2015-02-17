# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidWithLimits(self, root, minV, maxV):
        if root == None:
            return True
        if minV != None:
            if root.val <= minV:
                return False
        if maxV != None:
            if root.val >= maxV:
                return False

        leftResult = rightResult = True
        leftResult = self.isValidWithLimits(root.left, minV, root.val)
        rightResult = self.isValidWithLimits(root.right, root.val, maxV)
        return leftResult and rightResult
                
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidWithLimits(root, None, None)
