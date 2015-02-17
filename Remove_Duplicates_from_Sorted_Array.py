class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        total_len = len(A)
        i = 0
        result_i = 0
        
        if total_len == 0:
            return 0
        
        while True:
            if i >= total_len:
                break
            
            A[result_i] = A[i]
            
            while i + 1 < total_len and A[i + 1] == A[i]:
                i += 1
                
            if i + 1 >= total_len:
                break
            
            i += 1
            result_i += 1

        A = A[0:result_i + 1]
        return result_i + 1
