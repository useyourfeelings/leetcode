class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bits = [0] * 32
        sign = 0
        for num in A:
            if num < 0:
                num *= -1
                sign += 1
            for i in range(0, 32):
                bits[i] += (num >> i) & 1
        
        victim = 0
        for i in range(0, 32):
            bits[i] %= 3
            if bits[i]:
                victim |= (1 << i)
        
        if sign % 3:
            victim *= -1
        return victim
