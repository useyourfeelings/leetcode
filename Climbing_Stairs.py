class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        ways = [0] * (n + 1)
        
        ways[0] = ways[1] = 1
        
        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
            
        return ways[n]
