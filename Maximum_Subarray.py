class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        length = len(A)
        result = sum = 0
        max_negative = A[0]
        have_positive = False 
        for i in range(0, length):
            if A[i] < 0:
                max_negative = max(A[i], max_negative)
            else:
                have_positive = True
            
            sum += A[i]
            if sum <= 0:
                sum = 0
            result = max(sum, result)

        if not have_positive:
            return max_negative
        return result
