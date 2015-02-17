class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        e = len(matrix) - 1
        s = 0
        while s < e:
            c = int((s + e + 1) / 2)
            if target < matrix[c][0]:
                e = c - 1
            elif target > matrix[c][0]:
                s = c
            else:
                return True
        
        t = s
        s = 0
        e = len(matrix[s]) - 1
        while s < e:
            c = int((s + e + 1) / 2)
            if target < matrix[t][c]:
                e = c - 1
            elif target > matrix[t][c]:
                s = c
            else:
                return True
        
        return matrix[t][s] == target
